#!/usr/bin/env python3
"""Search the knowledge base. No dependencies, no API, no embeddings.

    python3 scripts/knowledge_search.py "how do I open a short-form video"
    python3 scripts/knowledge_search.py -k 8 --full "creative fatigue"

Ranks pages by term overlap in the title, the headings, and the body, then prints
the path, the title, and the matching lines. Read the top two or three hits only.
"""
import argparse, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "knowledge")
STOP = set("a an the and or of to in on for with is are be it its this that how do i my you your what when "
           "why which can should would could will not no yes at as by from we they he she them".split())

def pages():
    for sub in ("playbooks", "lessons", "concepts"):
        d = os.path.join(ROOT, sub)
        if not os.path.isdir(d): continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md") and f != "INDEX.md":
                yield sub, f[:-3], os.path.join(d, f)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("query", nargs="+")
    ap.add_argument("-k", type=int, default=6, help="how many pages to return")
    ap.add_argument("--full", action="store_true", help="print each hit's full text")
    a = ap.parse_args()

    terms = [t for t in re.findall(r"[a-z0-9]+", " ".join(a.query).lower()) if t not in STOP and len(t) > 2]
    if not terms:
        print("no usable search terms"); sys.exit(2)

    hits = []
    for sub, slug, path in pages():
        raw = open(path, encoding="utf-8", errors="ignore").read()
        low = raw.lower()
        heads = " ".join(re.findall(r"(?m)^#{1,6} (.+)$", low))
        score = 0
        for t in terms:
            score += 10 * slug.lower().count(t)
            score += 4 * heads.count(t)
            score += min(6, low.count(t))
        if score: hits.append((score, sub, slug, path, raw))

    hits.sort(key=lambda h: -h[0])
    if not hits:
        print("no matches. try fewer or broader words, or grep knowledge/INDEX.md"); return

    for score, sub, slug, path, raw in hits[:a.k]:
        title = (re.search(r"(?m)^#\s+(.+)$", raw) or [None, slug])[1]
        upd = (re.search(r"(?m)^updated:\s*(\S+)", raw) or [None, "-"])[1]
        conf = (re.search(r"(?m)^confidence:\s*(\S+)", raw) or [None, "-"])[1]
        print(f"\n=== {sub}/{slug}.md  [{score}]  updated {upd}, confidence {conf}")
        print(f"    {title}")
        if a.full:
            print(raw)
        else:
            for line in raw.split("\n"):
                if any(t in line.lower() for t in terms) and len(line.strip()) > 30:
                    print("    " + line.strip()[:200])

if __name__ == "__main__":
    main()
