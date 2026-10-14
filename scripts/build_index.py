#!/usr/bin/env python3
"""Generate knowledge/INDEX.md so the agent can find a page without reading 244 files."""
import os, re
K = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "knowledge"))
GROUPS = [
 ("Hooks & Attention", r"hook|attention|scroll|thumbnail|first-(3|three)|retention|curiosity"),
 ("Short-Form Video", r"short-form|video|reel|tiktok|shorts|b-roll|editing|caption|script"),
 ("Ad Creative & Testing", r"^ad-|creative|testing|control|variation|iterat|fatigue|winning|cbo|dynamic"),
 ("Copywriting", r"copy|headline|subject-line|advertorial|testimonial|objection|specificity|personality|storytell"),
 ("Offer & Positioning", r"offer|positioning|price|anchor|guarantee|grand-slam|transformation|identity|benefit"),
 ("Audience & Research", r"customer|research|persona|psychograph|awareness|review-mining|market|survey|voice-of"),
 ("UGC & Creators", r"ugc|creator|influencer|outreach|partnership"),
 ("Content Systems & Cadence", r"content|posting|schedul|system|sop|engine|repurpos|reuse|calendar"),
 ("Funnels & Landing Pages", r"landing|funnel|page|conversion|upsell|checkout|store"),
 ("Case Studies (anonymised)", r"^case-"),
]
def title(p):
    t = open(p, encoding="utf-8").read()
    m = re.search(r"(?m)^#\s+(.+)$", t)
    return m.group(1).strip() if m else os.path.basename(p)[:-3]
def summary(p):
    t = open(p, encoding="utf-8").read()
    t = re.sub(r"(?s)^---.*?---\n", "", t)
    t = re.sub(r"(?m)^#.*$", "", t)
    t = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1).replace("-", " "), t)
    for line in t.split("\n"):
        line = line.strip()
        if len(line) > 40 and not line.startswith(("-", "|", "```", "*")):
            return re.split(r"(?<=[.!?])\s", line)[0][:170]
    return ""
pages = []
for sub in ("playbooks", "lessons", "concepts"):
    d = os.path.join(K, sub)
    if not os.path.isdir(d): continue
    for f in sorted(os.listdir(d)):
        if f.endswith(".md") and f != "INDEX.md":
            pages.append((sub, f[:-3], os.path.join(d, f)))
used, out = set(), ["# Knowledge Index", "",
  f"{len(pages)} distilled pages. Grep this file first, then read only the pages you need.", "",
  "`playbooks/` = repeatable systems. `lessons/` = what a real campaign taught. `concepts/` = single ideas.", ""]
for name, pat in GROUPS:
    rx = re.compile(pat, re.I)
    hits = [p for p in pages if p not in used and rx.search(p[1])]
    if not hits: continue
    out.append(f"## {name}\n")
    for p in hits:
        used.add(p)
        out.append(f"- `{p[0]}/{p[1]}.md` — **{title(p[2])}**. {summary(p[2])}")
    out.append("")
rest = [p for p in pages if p not in used]
if rest:
    out.append("## Everything Else\n")
    for p in rest:
        out.append(f"- `{p[0]}/{p[1]}.md` — **{title(p[2])}**. {summary(p[2])}")
    out.append("")
open(os.path.join(K, "INDEX.md"), "w", encoding="utf-8").write("\n".join(out))
print(f"indexed {len(pages)} pages, {len(pages)-len(rest)} grouped, {len(rest)} in Everything Else")
