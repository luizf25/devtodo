# devtodo

![CI](https://github.com/luizf25/devtodo/actions/workflows/ci.yml/badge.svg)
[![Release](https://img.shields.io/github/v/release/luizf25/devtodo)](https://github.com/luizf25/devtodo/releases)

📦 **[Última release no GitHub](https://github.com/luizf25/devtodo/releases/latest)** — baixe o wheel para instalar.

Gerenciador de tarefas CLI para desenvolvedores. Versão **1.1.0**.

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
- Consulta de feriados públicos via API Nager.Date (`devtodo feriados`)

## 🛠️ Tecnologias

- **Python 3.10+**
- [Typer](https://typer.tiangolo.com/) — construção do CLI
- [Rich](https://rich.readthedocs.io/) — saída colorida
- [requests](https://requests.readthedocs.io/) — cliente HTTP para a integração com API
- [pytest](https://pytest.org/) — testes automatizados
- [responses](https://github.com/getsentry/responses) — mock de HTTP nos testes de integração
- [ruff](https://docs.astral.sh/ruff/) — linting e análise estática
- **GitHub Actions** — integração contínua e deploy automático via Releases
- **API externa**: [Nager.Date](https://date.nager.at/) — feriados públicos de mais de 100 países

## 📦 Instalação

### Via release (wheel)

```bash
pip install https://github.com/luizf25/devtodo/releases/download/v1.1.0/devtodo-1.1.0-py3-none-any.whl
```

Ou baixe o arquivo `.whl` na página de [releases](https://github.com/luizf25/devtodo/releases) e:

```bash
pip install devtodo-1.1.0-py3-none-any.whl
```

### A partir do código-fonte (para desenvolvimento)

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

# Consultar feriados públicos (integração com a API Nager.Date)
devtodo feriados                       # feriados BR do ano atual
devtodo feriados --ano 2025 --pais US  # feriados dos EUA em 2025
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

**1.1.0** — declarada em `pyproject.toml` e em `src/devtodo/__init__.py`,
seguindo [versionamento semântico](https://semver.org/lang/pt-BR/).

### Changelog

- **1.1.0** — Integração com a API pública [Nager.Date](https://date.nager.at/);
  novo comando `devtodo feriados`; testes de integração; deploy via GitHub Releases.
- **1.0.0** — Versão inicial (add, list, done, rm, clear-done, stats).

## 👤 Autor

Luiz Felipe Formiga Soares

## 🔗 Repositório

https://github.com/luizf25/devtodo