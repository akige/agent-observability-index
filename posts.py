# Blog posts for tools.panshi.io. Plain data; build.py renders them.
# Each post: slug, title, description, date (ISO), tags, body (HTML), faq [(q,a)].

POSTS = [
{
 "slug": "geo-case-study-ai-tools-directory",
 "title": "How we made a 116-tool directory citable by AI answer engines",
 "description": "A concrete GEO (Generative Engine Optimization) case study: the exact five changes we made to tools.panshi.io so ChatGPT, Perplexity and Google AI Overviews can cite it — with the research behind each.",
 "date": "2026-06-13",
 "tags": ["GEO", "case study", "AI search"],
 "body": """
<div class="bg-slate-900 border-l-4 border-emerald-500 rounded-r-lg px-5 py-4 mb-8">
<p class="text-sm font-semibold text-emerald-400">TL;DR</p>
<p class="text-slate-300 mt-1">We applied five evidence-backed GEO techniques to this directory: front-loaded verdicts, FAQ schema on 130 pages, structured comparison data, objective GitHub-derived maturity scores, and a published methodology. None of it is keyword tricks — it is making the facts an answer engine can lift directly. Here is exactly what we changed, and the research behind each.</p>
</div>

<p class="text-slate-400">Traditional SEO optimizes to rank as a blue link a human clicks. <strong class="text-slate-200">GEO (Generative Engine Optimization)</strong> optimizes so an AI answer engine — ChatGPT, Perplexity, Google AI Overviews, Claude — quotes your content inside its generated answer. Often there is no click: the citation <em>is</em> the win. The mechanics differ enough to be worth doing deliberately, and most of the winning moves are simply good, well-structured, well-sourced content.</p>

<p class="text-slate-400 mt-4">We rebuilt <a class="text-emerald-400" href="/index.html">this directory</a> with GEO in mind. Five concrete changes:</p>

<h2 class="text-xl font-semibold text-white mt-10">1. Front-load the verdict</h2>
<p class="text-slate-400 mt-2">The Princeton <em>GEO</em> paper (KDD 2024) found that adding clear statements, statistics and citations measurably lifts how often generative engines surface a page; separate citation studies find roughly 44% of LLM citations are pulled from the first 30% of a page. So every comparison page now opens with a one-sentence "Quick verdict" generated from verified data — the exact answer an engine can quote — before the detail table.</p>

<h2 class="text-xl font-semibold text-white mt-10">2. FAQ blocks with FAQPage schema</h2>
<p class="text-slate-400 mt-2">Answer engines lean heavily on Q&amp;A-shaped content. Every tool and comparison page now carries a short FAQ ("Is X open source?", "Can I self-host X?", "Is X OpenTelemetry-native?") rendered both for humans and as <code>FAQPage</code> JSON-LD — 130 pages of it. Every answer is generated from primary-source-verified fields, never invented.</p>

<h2 class="text-xl font-semibold text-white mt-10">3. Structured, comparable facts — not marketing copy</h2>
<p class="text-slate-400 mt-2">For all 116 tools we track open-source status, self-hostability, pricing model, framework integrations and licensing — each checked against the tool's own primary source. Tables and "best/vs" comparisons are cited by AI engines far more than prose, because the facts are unambiguous and liftable.</p>

<h2 class="text-xl font-semibold text-white mt-10">4. Objective, reproducible scores</h2>
<p class="text-slate-400 mt-2">We added a maturity signal computed only from public GitHub data (log of stars + last-commit recency + license) with the formula published openly. And we flagged which tools are genuinely OpenTelemetry-native — 29 of the 37 tracing/observability tools speak OTLP natively (no proprietary-SDK lock-in), 8 do not. That single fact changes a buyer's migration cost more than any feature list, and no vendor listicle will tell you.</p>

<h2 class="text-xl font-semibold text-white mt-10">5. A public methodology</h2>
<p class="text-slate-400 mt-2">Trust is the whole product for a neutral directory, so <a class="text-emerald-400" href="/methodology.html">the methodology</a> spells out exactly how every field and score is produced. Engines (and humans) reward auditable sources.</p>

<h2 class="text-xl font-semibold text-white mt-10">The honest part</h2>
<p class="text-slate-400 mt-2">GEO is real but over-hyped at the edges. The most credible independent benchmark (Conductor, 1,215 enterprise domains) puts AI-referral traffic at ~1% of total today — small, but high-intent (Ahrefs saw AI traffic convert to signups far above its share). And skip the fads: <code>llms.txt</code> is not consumed by search engines (Google compared it to the dead keywords meta tag), and keyword stuffing tests negative. GEO that lasts is just authority plus well-structured, well-sourced, comparison-shaped content.</p>

<div class="bg-slate-900 rounded-xl p-6 border border-slate-800 mt-10">
<p class="text-slate-200 font-semibold">We do this as a service.</p>
<p class="text-slate-400 mt-2">We applied this to our own directory first — it is the testbed and the reference case. If you want your content surfaced by AI answer engines with <em>measured</em> citation tracking (not vague "AI visibility"), email <a class="text-emerald-400" href="mailto:hi@panshi.io">hi@panshi.io</a>.</p>
</div>
""",
 "faq": [
   ("What is GEO (Generative Engine Optimization)?",
    "GEO is optimizing content so AI answer engines like ChatGPT, Perplexity and Google AI Overviews cite or surface it inside their generated answers, rather than ranking it as a link a human clicks."),
   ("Does llms.txt help with GEO?",
    "No. Major search/answer engines do not consume llms.txt; Google has compared it to the long-dead keywords meta tag. It is only useful for feeding coding assistants documentation."),
   ("How much traffic does AI search actually send?",
    "Today it is small — around 1% of total referral traffic per the most credible independent benchmark (Conductor, 1,215 domains) — but it converts at a much higher rate than its share, so it is high-intent rather than high-volume."),
   ("What is the single highest-ROI GEO action?",
    "Publish and keep fresh opinionated, benchmarked best/vs comparison pages with hard statistics, named sources and tables, with the conclusion front-loaded in the first paragraph."),
 ],
},
{
 "slug": "opentelemetry-native-llm-observability-lock-in",
 "title": "OpenTelemetry-native or not: the lock-in question in LLM observability",
 "description": "Of the 37 LLM tracing/observability tools we track, 29 are OpenTelemetry-native and 8 are not. Here is why that single fact decides your migration cost — and how to tell the difference.",
 "date": "2026-06-13",
 "tags": ["OpenTelemetry", "observability", "lock-in"],
 "body": """
<div class="bg-slate-900 border-l-4 border-emerald-500 rounded-r-lg px-5 py-4 mb-8">
<p class="text-sm font-semibold text-emerald-400">Quick answer</p>
<p class="text-slate-300 mt-1">If a tool is OpenTelemetry-native — it ingests or emits OTLP and follows the OTel GenAI semantic conventions — switching off it later costs you almost nothing, because your instrumentation stays the same and you just repoint the endpoint. If it relies on a proprietary SDK or trace format, every line of instrumentation is a switching cost. Of the 37 tracing/observability tools we track, <strong class="text-slate-200">29 are OpenTelemetry-native and 8 are not.</strong></p>
</div>

<p class="text-slate-400">"Does it integrate with X?" is the wrong first question when you pick an LLM observability tool. The question that actually decides your future migration bill is: <strong class="text-slate-200">is it OpenTelemetry-native, or does it lock you into a proprietary SDK?</strong></p>

<h2 class="text-xl font-semibold text-white mt-10">Why it matters</h2>
<p class="text-slate-400 mt-2">OpenTelemetry (OTel) is the vendor-neutral standard for traces and metrics. When an observability tool speaks OTLP natively, your app emits standard OTel spans and you simply point them at that tool. Outgrow it, or want to send the same data to two backends? You change an endpoint, not your code. When a tool instead ships its own SDK and trace format, your instrumentation <em>is</em> the lock-in: leaving means re-instrumenting everything.</p>

<h2 class="text-xl font-semibold text-white mt-10">How to tell the difference</h2>
<p class="text-slate-400 mt-2">We checked each tool's own docs and repository, not its marketing. A tool counts as OTel-native only if OTLP / the OpenTelemetry SDK / GenAI semantic conventions are a first-class path — not a secondary "integration." Native examples include Arize Phoenix (built on OTel), SigNoz (OTel-first since day one), Pydantic Logfire (a thin wrapper over OTel), OpenLIT and Traceloop/OpenLLMetry (whose conventions were upstreamed into OTel itself), plus managed platforms that expose a native OTLP endpoint (Langfuse, Datadog, New Relic, Grafana, Dynatrace). Proprietary-first examples include tools whose primary path is their own decorator SDK or a logging proxy rather than OTLP.</p>

<h2 class="text-xl font-semibold text-white mt-10">The nuance</h2>
<p class="text-slate-400 mt-2">OTel-native is not automatically "better" — a proprietary SDK can offer richer, opinionated capture. And in our own instrumentation-overhead benchmark, the per-span cost of all tested SDKs was negligible against real LLM latency (well under 0.05% of a typical call), though it varied about 7x between the lightest OTel path and a richer proprietary one. So treat OTel-native as a <em>strategic</em> property — it caps your downside and keeps you portable — rather than a performance verdict.</p>

<p class="text-slate-400 mt-4">Every tool page in <a class="text-emerald-400" href="/index.html">our index</a> flags OpenTelemetry-native status, and our <a class="text-emerald-400" href="/methodology.html">methodology</a> explains how we verified it.</p>
""",
 "faq": [
   ("What does OpenTelemetry-native mean for an LLM observability tool?",
    "It means the tool ingests or emits OpenTelemetry (OTLP) and follows the OTel GenAI semantic conventions as a first-class path, so you instrument with standard OpenTelemetry rather than a proprietary SDK — and can repoint or dual-export without rewriting code."),
   ("How many LLM observability tools are OpenTelemetry-native?",
    "Of the 37 tracing/observability tools tracked on this index, 29 are OpenTelemetry-native and 8 rely on a proprietary SDK or trace format."),
   ("Is OpenTelemetry-native always the better choice?",
    "Not always. A proprietary SDK can capture richer, more opinionated data. OTel-native is best understood as a strategic property that minimizes lock-in and keeps you portable, not as a performance ranking."),
   ("Does instrumentation overhead differ much between tools?",
    "In our micro-benchmark the per-span overhead of all tested SDKs was negligible versus real LLM latency (under 0.05% of a typical 500ms call), though it varied roughly 7x between the lightest OpenTelemetry path and a richer proprietary one."),
 ],
},
]
