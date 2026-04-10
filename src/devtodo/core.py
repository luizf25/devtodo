"""Lógica de negócio do devtodo. Funções puras, sem I/O."""
from datetime import datetime
from typing import Optional

PRIORIDADES_VALIDAS = {"alta", "media", "baixa"}


class DevtodoError(Exception):
    """Erro de domínio do devtodo."""


def novo_id(tarefas: list[dict]) -> int:
    """Retorna o próximo ID sequencial (1 se vazio)."""
    if not tarefas:
        return 1
    return max(t["id"] for t in tarefas) + 1


def adicionar_tarefa(
    tarefas: list[dict],
    texto: str,
    prioridade: str = "media",
    tag: Optional[str] = None,
) -> dict:
    """Adiciona uma tarefa à lista e retorna a tarefa criada."""
    if not texto or not texto.strip():
        raise DevtodoError("O texto da tarefa não pode ser vazio.")
    if prioridade not in PRIORIDADES_VALIDAS:
        raise DevtodoError(
            f"Prioridade inválida: '{prioridade}'. "
            f"Use uma de: {', '.join(sorted(PRIORIDADES_VALIDAS))}."
        )
    tarefa = {
        "id": novo_id(tarefas),
        "texto": texto.strip(),
        "prioridade": prioridade,
        "tag": tag,
        "concluida": False,
        "criada_em": datetime.now().isoformat(timespec="seconds"),
    }
    tarefas.append(tarefa)
    return tarefa


def marcar_concluida(tarefas: list[dict], tarefa_id: int) -> dict:
    """Marca uma tarefa como concluída pelo ID."""
    for t in tarefas:
        if t["id"] == tarefa_id:
            t["concluida"] = True
            return t
    raise DevtodoError(f"Tarefa com id={tarefa_id} não encontrada.")


def remover_tarefa(tarefas: list[dict], tarefa_id: int) -> dict:
    """Remove uma tarefa pelo ID e retorna a removida."""
    for i, t in enumerate(tarefas):
        if t["id"] == tarefa_id:
            return tarefas.pop(i)
    raise DevtodoError(f"Tarefa com id={tarefa_id} não encontrada.")


def filtrar_tarefas(
    tarefas: list[dict],
    tag: Optional[str] = None,
    prioridade: Optional[str] = None,
    apenas_concluidas: bool = False,
    apenas_pendentes: bool = False,
) -> list[dict]:
    """Retorna uma nova lista filtrada conforme os critérios."""
    resultado = list(tarefas)
    if tag is not None:
        resultado = [t for t in resultado if t.get("tag") == tag]
    if prioridade is not None:
        if prioridade not in PRIORIDADES_VALIDAS:
            raise DevtodoError(f"Prioridade inválida: '{prioridade}'.")
        resultado = [t for t in resultado if t["prioridade"] == prioridade]
    if apenas_concluidas:
        resultado = [t for t in resultado if t["concluida"]]
    if apenas_pendentes:
        resultado = [t for t in resultado if not t["concluida"]]
    return resultado


def limpar_concluidas(tarefas: list[dict]) -> int:
    """Remove todas as tarefas concluídas. Retorna quantas foram removidas."""
    antes = len(tarefas)
    tarefas[:] = [t for t in tarefas if not t["concluida"]]
    return antes - len(tarefas)


def estatisticas(tarefas: list[dict]) -> dict:
    """Retorna um resumo das tarefas."""
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["concluida"])
    pendentes = total - concluidas
    por_prioridade = {p: 0 for p in PRIORIDADES_VALIDAS}
    for t in tarefas:
        if not t["concluida"]:
            por_prioridade[t["prioridade"]] += 1
    return {
        "total": total,
        "concluidas": concluidas,
        "pendentes": pendentes,
        "pendentes_por_prioridade": por_prioridade,
    }