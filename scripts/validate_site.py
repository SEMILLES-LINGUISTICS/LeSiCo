from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
IGNORADOS = ("http://", "https://", "mailto:", "tel:", "#", "javascript:")


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag in {"a", "link", "script", "img", "iframe"}:
            value = values.get("href") or values.get("src")
            if value:
                self.links.append(value)


def destino(base: Path, link: str) -> Path | None:
    if link.startswith(IGNORADOS):
        return None
    path = urlsplit(link).path
    if not path:
        return None
    result = ROOT / path.lstrip("/") if path.startswith("/") else base / path
    result = result.resolve()
    if result.is_dir() or path.endswith("/"):
        result = result / "index.html"
    return result


def main() -> None:
    errores: list[str] = []
    html_files = sorted(ROOT.rglob("*.html"))
    for html in html_files:
        parser = Links()
        parser.feed(html.read_text(encoding="utf-8"))
        for link in parser.links:
            target = destino(html.parent, link)
            if target and not target.exists():
                errores.append(f"{html.relative_to(ROOT)} -> {link}")

    for json_file in ROOT.rglob("*.json"):
        try:
            json.loads(json_file.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            errores.append(f"JSON inválido: {json_file.relative_to(ROOT)}: {error}")

    if errores:
        print("Errores de validación:")
        print("\n".join(f"- {error}" for error in errores))
        raise SystemExit(1)
    print(f"Sitio válido: {len(html_files)} páginas HTML y enlaces locales resueltos.")


if __name__ == "__main__":
    main()
