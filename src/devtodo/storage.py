"""Persistência em JSON no diretório home do usuário."""
import json
from pathlib import Path

DEFAULT_PATH = Path.home() / ".devtodo" / "tasks.json"


def carregar(caminho: Path = DEFAULT_PATH) -> list[dict]:
    if not caminho.exists():
        return []
    with caminho.open("r", encoding="utf-8") as f:
        return json.load(f)


def salvar(tarefas: list[dict], caminho: Path = DEFAULT_PATH) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)