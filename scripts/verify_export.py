#!/usr/bin/env python3
"""Fail when the standalone creative brain leaks private context or ships dead wiring."""

import argparse
import hashlib
import re
import sys
from pathlib import Path


PRIVATE_FINGERPRINTS = {
    "de2e11360a4a7a96ba0073cfa351b134d8437747af815e4885b31f804bf880b4",
    "cb9d5527d97619f4001db71e1d3cfd9000f09ad291455cf9f9c2669a0dba312c",
    "c1c4e6982de51313e2647666d96eb6f7f4a671ac876bb43dcc9e721dd957b797",
    "6013de0381f648b7f21518885c02b40b7583adfb33c6d9b64d3aed52c3934798",
    "9d3ad95284f4677ad0f4062ca6ef4f1377d55e31de61b573ffa454e4b9d3201c",
    "46a0fbc474cf6ace43bf0e3e5e3a1d2de7e5a4ef450840c9f4b75d00a0079356",
    "a4e63bcacf6c172ad84f9f4523c8f1acaf33676fa76d3258c67b7e7bbf16d777",
    "6da675dc22dc488103d37a7d70f9cc7f80e5522261dcf673f7e90daa3b11389b",
    "e24da440c3c30f4a7b7c1c62e91b7ff45b073e1106c26887d708b1bf7fda752d",
    "755c4ca4ff7c6bd5027e45974e574850da06c23e42d7bea715a642304406b172",
    "79ee2860ad2544f1750eae19570f6ac88f3cc17194d5d928cca3e38ea6253072",
    "63be8044d77188f24a0076e342b1efbd70725f5663bed28f468e311e6c9123a4",
    "33f19a2378973c210f302d1a592d4b7851480125c229bd489e7efa333caba268",
    "fe821f2513f09efa6a8d68669c31bd29e47736608f35f3e4d2b132af09755822",
    "c07806b39321186fc61f16dc4f0102695c8dd60e4664e13e098f15dc6fa2bf50",
    "36fb6d59dbaee696819020472a58678116ded305216dbc966e6d2f9e3f700adc",
    "d20bdc7a25498f56ee303856c60a08a668ff6922e0223d6f4f8183c7985fe520",
    "cb9f09a3b77c2c30af6ff532e62c5759dfc67ce926f94d720294b09f29645d26",
    "71e00981c75c4d02b4bb12066123921ce1e55744fa069886059a309c2839ad7f",
    "d233633d9524e84c71d6fe45eb3836f8919148e4a5fc2234cc9e6494ec0f11c2",
    "f3fe5a51a2be8c6dc715028858fcba82ee021be7687e4f95b45086b8ffb1a23f",
    "867417e00dd66c36596429f00517ef68e64c9759fbf416af29726838258b1550",
    "827476bcf14fecd3bc1d7e1fd1c749259642aed550a2f65990bf75405d35503e",
    "048f2e7fea27c07f232fba298a99d752a1274fa25686cc7ae831a73edd20df7c",
    "750d0b67aa321709c5595ef7ce571181ea53cc4e5ebdd23fd15f192a9313d91b",
    "88f1f48c8d48ce514dab29e1cdba03d5ee6b04ebd5795275c2384819f55227ce",
    "6fd1efd8dfbf87eb11524695cbf5948d9185ceff16e7518c06df6b4369bd74b4",
    "611352da2971d3cf2829775961726530296b972b38a7ba83bfd53896d6f5f672",
    "4003e7b2e0f53a0357f45375e68b4b8e469f41e54947f2472af76d4e906ccd3e",
    "b57ea19289ebdb141fadf779482a05c3153f80faf29e71b9f4da7650eee91880",
    "a9a57ad44a7eec0d93b2094a1447b86a7766e862f85b961ad26cf59dc1c4a739",
    "f88e3def18c11e8ca14a797c6f1c72e9694d6a047d2d5910724caa1e425d6ea5",
    "bb527b1ed178e754edcf9d9f6ec669b6d9f0a9e8133c97fd03ce76d69a05d6f3",
    "2a2207565c69d65a12c0101180ef7f3a232b9492f634f0f383391ede05ac8edf",
    "f70bebef131245dbdbb19082fc0507356487b968b032f1a6a224e2691c1b1c27",
    "de94d2e5f57918db575826202942c70447514190ce21620fbcc0d7fe4385d7ef",
    "2537d53a4d8e26e4fedb36b9f4baebcdf4917a0e8dfc97bd8d2cfbc91cfb1bcf",
    "950488c270a0c205cd61f5cbf309934f86fccd546bed4561b9c3d004fde57d32",
    "1674cf7b3953b13bc017384616ed94d38258c7372e125562e90b449e2189b6e8",
    "c674b19512d5293763f80488ed2c8dca92f1db7d3cb63776f011944e37a5894b",
    "ce5bc18d6598f3d712c101a1b75cb12973fd23f7af6a4943072b000621a91b20",
}

INTERNAL_PATH = re.compile(
    r"/Users/|~/|(?:^|[ `(])(?:sources|projects|daily|journal|me|network|decisions)/|"
    r"\.claude/(?:skills|rules|crons)|scripts/(?:videoad|post_queue|social_inspo)\.py"
)
MALFORMED_FRONTMATTER = re.compile(r"^(?:type|updated|confidence|sources|provenance)\s*,", re.M)
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\d)\+?\d{1,3}[ -](?:\d[ ()-]*){8,}\d")


def text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.name == "verify_export.py" or any(part in {".git", "tests", "__pycache__"} for part in path.parts):
            continue
        if "last30days" in path.parts:
            continue
        if path.suffix.lower() in {".md", ".txt", ".py", ".json", ".yaml", ".yml", ".sh", ""}:
            yield path


def private_hits(text: str):
    words = re.findall(r"[a-z0-9]+", text.lower())
    for width in (1, 2, 3):
        for start in range(len(words) - width + 1):
            phrase = " ".join(words[start:start + width])
            if hashlib.sha256(phrase.encode()).hexdigest() in PRIVATE_FINGERPRINTS:
                yield phrase


def verify(root: Path):
    errors = []
    required = ("CLAUDE.md", "AGENTS.md", "SUBJECT.md", "VOICE.md", "knowledge", "skills", "rules")
    for name in required:
        if not (root / name).exists():
            errors.append(f"missing required path: {name}")
    if (root / "export").exists():
        errors.append("nested export directory still exists")
    if (root / "skills" / "lead-gen-ad").exists():
        errors.append("removed skill still exists: lead-gen-ad")

    pages = {p.stem for p in (root / "knowledge").rglob("*.md")} if (root / "knowledge").exists() else set()
    skills = {p.name for p in (root / "skills").iterdir() if p.is_dir()} if (root / "skills").exists() else set()
    link_targets = pages | skills

    for path in text_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(root)
        for phrase in sorted(set(private_hits(text))):
            errors.append(f"private identifier in {rel}: {phrase}")
        if INTERNAL_PATH.search(text):
            errors.append(f"private or missing path in {rel}")
        if MALFORMED_FRONTMATTER.search(text):
            errors.append(f"malformed frontmatter in {rel}")
        if EMAIL.search(text) and path.name != ".env.example":
            errors.append(f"email address in {rel}")
        if PHONE.search(text):
            errors.append(f"phone number in {rel}")
        if path.suffix == ".md" and ("knowledge" in path.parts or "skills" in path.parts):
            for target in re.findall(r"\[\[([^\]|#]+)", text):
                if target not in link_targets and target != "wiki-links":
                    errors.append(f"dead wiki link in {rel}: {target}")

    for error in sorted(set(errors)):
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("OK: standalone layout, privacy scan, paths, metadata, and wiki links")
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    raise SystemExit(verify(args.root.resolve()))


if __name__ == "__main__":
    main()
