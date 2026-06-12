#!/usr/bin/env bash
# Weekly link-rot check for tools.panshi.io dataset.
# Dead (000/404/410/5xx) -> P3 digest via send_alert; 403/429 listed as bot-blocked (manual review), no alert by themselves.
set -u
DIR="/home/ubuntu/paseo-workspace/incubation/agentobs-directory"
OUT="/tmp/agentobs-linkcheck.$$"
python3 -c "import json;[print(t['name']+'\t'+t['url']) for t in json.load(open('$DIR/data/tools.json'))]" > "$OUT.urls"

ALLOW_FAIL="atla-ai.com|freeplay.ai|quotientai.co"  # JS/framer 站对 curl 返回 404/000 的已核实误报

check_one() {
  local name url code
  name="${1%%$'\t'*}"; url="${1#*$'\t'}"
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 -L \
    -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36" "$url" 2>/dev/null)
  case "$url" in *atla-ai.com*|*freeplay.ai*|*quotientai.co*) return;; esac
  case "$code" in
    2*|3*) ;;
    403|429) echo "BLOCKED	$code	$name	$url" ;;
    *) echo "DEAD	$code	$name	$url" ;;
  esac
}
export -f check_one

nice -n 19 bash -c 'while IFS= read -r line; do check_one "$line" & while [ "$(jobs -r | wc -l)" -ge 4 ]; do wait -n; done; done < "$1"; wait' _ "$OUT.urls" > "$OUT.report"

DEAD=$(grep -c '^DEAD' "$OUT.report" || true)
BLOCKED=$(grep -c '^BLOCKED' "$OUT.report" || true)
TOTAL=$(wc -l < "$OUT.urls")

if [ "$DEAD" -gt 0 ]; then
  printf 'tools.panshi.io 周度链接检查: %s dead / %s bot-blocked / %s total\n%s\n处理: 修 data/tools.json (改 URL 或标 sunset) -> python3 build.py -> cp -r site docs -> git push\n' \
    "$DEAD" "$BLOCKED" "$TOTAL" "$(grep '^DEAD' "$OUT.report")" \
    | /usr/local/lib/alert/send_alert.sh P3 incubation agentobs-linkrot-weekly
fi
echo "linkcheck done: ${DEAD} dead, ${BLOCKED} blocked, ${TOTAL} total"
rm -f "$OUT.urls" "$OUT.report"
