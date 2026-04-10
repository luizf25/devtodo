"""Interface de linha de comando do devtodo."""
import typer
from rich.console import Console
from rich.table import Table

from devtodo import __version__, core, storage

app = typer.Typer(help="devtodo — tarefas CLI para devs.")
console = Console()

CORES_PRIO = {"alta": "red", "media": "yellow", "baixa": "green"}


@app.command()
def add(texto: str, prio: str = "media", tag: str = None):
    """Adiciona uma nova tarefa."""
    tarefas = storage.carregar()
    try:
        t = core.adicionar_tarefa(tarefas, texto, prio, tag)
    except core.DevtodoError as e:
        console.print(f"[red]Erro:[/red] {e}")
        raise typer.Exit(code=1)
    storage.salvar(tarefas)
    console.print(f"[green]✓[/green] Tarefa #{t['id']} adicionada.")


@app.command("list")
def listar(tag: str = None, prio: str = None, done: bool = False):
    """Lista tarefas (pendentes por padrão)."""
    tarefas = storage.carregar()
    filtradas = core.filtrar_tarefas(
        tarefas, tag=tag, prioridade=prio,
        apenas_concluidas=done, apenas_pendentes=not done,
    )
    if not filtradas:
        console.print("[dim]Nenhuma tarefa encontrada.[/dim]")
        return
    tabela = Table(title="devtodo")
    tabela.add_column("ID", justify="right")
    tabela.add_column("Prio")
    tabela.add_column("Tag")
    tabela.add_column("Tarefa")
    for t in filtradas:
        cor = CORES_PRIO.get(t["prioridade"], "white")
        marca = "[strike]" if t["concluida"] else ""
        fim = "[/strike]" if t["concluida"] else ""
        tabela.add_row(
            str(t["id"]),
            f"[{cor}]{t['prioridade']}[/{cor}]",
            t.get("tag") or "-",
            f"{marca}{t['texto']}{fim}",
        )
    console.print(tabela)


@app.command()
def done(tarefa_id: int):
    """Marca uma tarefa como concluída."""
    tarefas = storage.carregar()
    try:
        core.marcar_concluida(tarefas, tarefa_id)
    except core.DevtodoError as e:
        console.print(f"[red]Erro:[/red] {e}")
        raise typer.Exit(code=1)
    storage.salvar(tarefas)
    console.print(f"[green]✓[/green] Tarefa #{tarefa_id} concluída.")


@app.command()
def rm(tarefa_id: int):
    """Remove uma tarefa."""
    tarefas = storage.carregar()
    try:
        core.remover_tarefa(tarefas, tarefa_id)
    except core.DevtodoError as e:
        console.print(f"[red]Erro:[/red] {e}")
        raise typer.Exit(code=1)
    storage.salvar(tarefas)
    console.print(f"[green]✓[/green] Tarefa #{tarefa_id} removida.")


@app.command("clear-done")
def clear_done():
    """Remove todas as tarefas concluídas."""
    tarefas = storage.carregar()
    n = core.limpar_concluidas(tarefas)
    storage.salvar(tarefas)
    console.print(f"[green]✓[/green] {n} tarefa(s) removida(s).")


@app.command()
def stats():
    """Mostra estatísticas das tarefas."""
    s = core.estatisticas(storage.carregar())
    console.print(f"Total: {s['total']} | Pendentes: {s['pendentes']} | Concluídas: {s['concluidas']}")
    console.print(f"Pendentes por prioridade: {s['pendentes_por_prioridade']}")


@app.command()
def version():
    """Mostra a versão."""
    console.print(f"devtodo v{__version__}")


if __name__ == "__main__":
    app()