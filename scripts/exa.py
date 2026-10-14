"""
Exa web-search API helper. Raw requests, no SDK dependency.
Mirrors the scripts/the CRM.py pattern.

Canonical reference: https://exa.ai/docs/reference/search-api-guide-for-coding-agents
  - POST https://api.exa.ai/search   (find + optionally retrieve content)
  - POST https://api.exa.ai/contents (content for URLs you already have)
  - POST https://api.exa.ai/answer   (grounded answer, question-first UIs)
Auth: x-api-key header, value = EXA_API_KEY from .env

Usage from Python:
    from scripts.exa import exa_search, exa_contents, exa_answer

    res = exa_search("latest AI safety news", num_results=10)
    for r in res["results"]:
        print(r["title"], r["url"], r.get("highlights"))

Usage from CLI (prints JSON):
    python scripts/exa.py "latest AI safety news"
    python scripts/exa.py "latest AI safety news" --num 5 --text
    python scripts/exa.py --contents "https://example.com/a" "https://example.com/b"
    python scripts/exa.py --answer "What is the latest in AI safety?"
"""

import os
import sys
import json
import argparse
from pathlib import Path

import requests

# Load .env from the repo root
_repo_root = Path(__file__).parent.parent
_env_path = _repo_root / ".env"

if _env_path.exists():
    for line in _env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

BASE_URL = os.environ.get("EXA_BASE_URL", "https://api.exa.ai")
API_KEY = os.environ.get("EXA_API_KEY", "")


def _post(path: str, body: dict) -> dict:
    """POST JSON to an Exa endpoint, return parsed JSON."""
    if not API_KEY:
        raise RuntimeError(
            "EXA_API_KEY not set. Add it to the repo root .env as EXA_API_KEY=..."
        )
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    url = BASE_URL.rstrip("/") + path
    resp = requests.post(url, headers=headers, json=body)

    try:
        resp.raise_for_status()
    except requests.HTTPError as e:
        print(f"Exa API error {resp.status_code}: {resp.text}", file=sys.stderr)
        raise

    return resp.json()


def exa_search(
    query: str,
    *,
    type: str = "auto",
    num_results: int = 10,
    highlights: bool = True,
    text: bool = False,
    text_max_chars: int = 20000,
    include_domains=None,
    exclude_domains=None,
    max_age_hours=None,
    output_schema=None,
    system_prompt=None,
    extra: dict = None,
) -> dict:
    """Search the web. Returns parsed Exa /search response.

    Defaults to highlights (token-efficient). Pass text=True for full content.
    output_schema + system_prompt request grounded structured synthesis.
    """
    contents = {}
    if highlights:
        contents["highlights"] = True
    if text:
        contents["text"] = {"maxCharacters": text_max_chars}

    body = {
        "query": query,
        "type": type,
        "numResults": num_results,
    }
    if contents:
        body["contents"] = contents
    if include_domains:
        body["includeDomains"] = list(include_domains)
    if exclude_domains:
        body["excludeDomains"] = list(exclude_domains)
    if max_age_hours is not None:
        body["maxAgeHours"] = max_age_hours
    if output_schema is not None:
        body["outputSchema"] = output_schema
    if system_prompt is not None:
        body["systemPrompt"] = system_prompt
    if extra:
        body.update(extra)
    return _post("/search", body)


def exa_contents(
    urls,
    *,
    highlights: bool = True,
    text: bool = False,
    text_max_chars: int = 20000,
    max_age_hours=None,
) -> dict:
    """Get content for URLs you already have. Returns parsed /contents response."""
    contents = {}
    if highlights:
        contents["highlights"] = True
    if text:
        contents["text"] = {"maxCharacters": text_max_chars}

    body = {"urls": list(urls)}
    if contents:
        body.update(contents)
    if max_age_hours is not None:
        body["maxAgeHours"] = max_age_hours
    return _post("/contents", body)


def exa_answer(query: str, *, model: str = "exa-pro", extra: dict = None) -> dict:
    """Grounded answer with citations. Returns parsed /answer response."""
    body = {"query": query, "model": model}
    if extra:
        body.update(extra)
    return _post("/answer", body)


def _format_results(res: dict, text: bool) -> str:
    """Human-readable rendering for CLI use."""
    out = []
    if "output" in res:
        out.append("=== Synthesized output ===")
        out.append(json.dumps(res["output"].get("content"), indent=2, ensure_ascii=False))
        grounding = res["output"].get("grounding") or []
        if grounding:
            out.append("\n--- grounding ---")
            for g in grounding:
                cites = [c.get("url") for c in g.get("citations", [])]
                out.append(f"{g.get('field')}: {', '.join(cites)}")
        return "\n".join(out)

    for r in res.get("results", []):
        out.append(f"### {r.get('title', '(no title)')}")
        out.append(r.get("url", ""))
        if r.get("highlights"):
            out.append("\n".join(f"> {h}" for h in r["highlights"]))
        if text and r.get("text"):
            out.append("\n" + r["text"][:1500] + ("..." if len(r["text"]) > 1500 else ""))
        if r.get("summary"):
            out.append(f"\nsummary: {r['summary']}")
        out.append("")
    return "\n".join(out) or json.dumps(res, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Exa web-search helper.")
    ap.add_argument("query", nargs="?", help="Search query (or question with --answer).")
    ap.add_argument("--num", type=int, default=10, help="Number of results.")
    ap.add_argument("--type", default="auto", help="Search type: auto|fast|instant|deep|deep-lite|deep-reasoning.")
    ap.add_argument("--highlights", action="store_true", default=True, help="Return highlights (default on).")
    ap.add_argument("--text", action="store_true", help="Return full text instead of/in addition to highlights.")
    ap.add_argument("--max-chars", type=int, default=20000, help="Text max characters.")
    ap.add_argument("--include-domains", nargs="*", default=None)
    ap.add_argument("--exclude-domains", nargs="*", default=None)
    ap.add_argument("--max-age-hours", type=int, default=None, help="Cache freshness threshold; 0 = always livecrawl.")
    ap.add_argument("--contents", nargs="+", metavar="URL", help="Get contents for known URLs instead of searching.")
    ap.add_argument("--answer", action="store_true", help="Get a grounded answer (question-first) instead of search results.")
    ap.add_argument("--json", action="store_true", help="Print raw JSON response.")
    args = ap.parse_args()

    if args.contents:
        result = exa_contents(args.contents, highlights=args.highlights, text=args.text, text_max_chars=args.max_chars)
    elif args.answer:
        if not args.query:
            ap.error("--answer requires a query")
        result = exa_answer(args.query)
    elif args.query:
        result = exa_search(
            args.query,
            type=args.type,
            num_results=args.num,
            highlights=args.highlights,
            text=args.text,
            text_max_chars=args.max_chars,
            include_domains=args.include_domains,
            exclude_domains=args.exclude_domains,
            max_age_hours=args.max_age_hours,
        )
    else:
        ap.error("Provide a query, or --contents with URLs.")

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(_format_results(result, args.text))
