import pytest
from devtodo.core import (
    adicionar_tarefa, marcar_concluida,
    filtrar_tarefas, limpar_concluidas, estatisticas, DevtodoError,
)


def test_adicionar_tarefa_caminho_feliz():
    tarefas = []
    t = adicionar_tarefa(tarefas, "Estudar CI", "alta", "estudos")
    assert t["id"] == 1
    assert t["texto"] == "Estudar CI"
    assert t["concluida"] is False
    assert len(tarefas) == 1


def test_adicionar_tarefa_texto_vazio_falha():
    with pytest.raises(DevtodoError):
        adicionar_tarefa([], "   ")


def test_adicionar_tarefa_prioridade_invalida_falha():
    with pytest.raises(DevtodoError):
        adicionar_tarefa([], "Tarefa", prioridade="urgentissima")


def test_marcar_concluida_inexistente_falha():
    with pytest.raises(DevtodoError):
        marcar_concluida([], 99)


def test_filtrar_lista_vazia_retorna_vazio():
    assert filtrar_tarefas([], tag="x") == []


def test_limpar_concluidas_e_estatisticas():
    tarefas = []
    adicionar_tarefa(tarefas, "A", "alta")
    adicionar_tarefa(tarefas, "B", "baixa")
    marcar_concluida(tarefas, 1)
    removidas = limpar_concluidas(tarefas)
    assert removidas == 1
    assert len(tarefas) == 1
    s = estatisticas(tarefas)
    assert s["pendentes"] == 1 and s["concluidas"] == 0