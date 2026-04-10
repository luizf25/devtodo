# devtodo

![CI](https://github.com/luizf25/devtodo/actions/workflows/ci.yml/badge.svg)

Gerenciador de tarefas CLI para desenvolvedores. Versão **1.0.0**.

## 🎯 Problema real

Desenvolvedores perdem foco ao alternar entre o terminal e apps de tarefas
como Notion, Trello ou Todoist. Cada troca de contexto quebra o fluxo e
reduz a produtividade. Estudos sobre *context switching* mostram que
reengajar em uma tarefa após interrupção pode levar vários minutos.

## 💡 Solução

O **devtodo** vive no mesmo terminal onde o dev já trabalha. Adicionar,
listar e concluir tarefas leva segundos, sem sair do ambiente de trabalho.
Os dados ficam em `~/.devtodo/tasks.json`, seguindo a convenção Unix de
dotfiles no home.

## 👥 Público-alvo

Desenvolvedores, sysadmins, cientistas de dados e estudantes de computação
que passam a maior parte do tempo em terminal.

## ✨ Funcionalidades

- Adicionar tarefa com prioridade (`alta`, `media`, `baixa`) e tag
- Listar tarefas com filtros por tag, prioridade e status
- Marcar tarefa como concluída
- Remover tarefa individual ou limpar todas as concluídas
- Estatísticas rápidas (total, pendentes, concluídas)
- Saída colorida no terminal via `rich`

## 🛠️ Tecnologias

- **Python 3.10+**
- [Typer](https://typer.tiangolo.com/) — construção do CLI
- [Rich](https://rich.readthedocs.io/) — saída colorida
- [pytest](https://pytest.org/) — testes automatizados
- [ruff](https://docs.astral.sh/ruff/) — linting e análise estática
- **GitHub Actions** — integração contínua

## 📦 Instalação

```bash
git clone https://github.com/luizf25/devtodo.git
cd devtodo
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## ▶️ Uso

```bash
devtodo add "Revisar PR #42" --prio alta --tag trabalho
devtodo add "Estudar GitHub Actions" --prio media --tag estudos
devtodo list
devtodo done 1
devtodo stats
devtodo clear-done
devtodo version
```

## 🧪 Rodar os testes

```bash
pytest -v
```

## 🔍 Rodar o lint

```bash
ruff check .
```

## 📌 Versão

**1.0.0** — declarada em `pyproject.toml` e em `src/devtodo/__init__.py`,
seguindo [versionamento semântico](https://semver.org/lang/pt-BR/).

## 👤 Autor

Luiz Felipe Formiga Soares

## 🔗 Repositório

https://github.com/luizf25/devtodo