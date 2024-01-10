from importlib import metadata

import typer

from s_lang import run as run_code


def read_file(path: str) -> str:
    with open(path, mode="r") as file:
        return file.read()


app = typer.Typer()
__version__ = metadata.version(__package__)


def version_callback(value: bool) -> None:
    if value:
        print(__version__)
        raise typer.Exit()


@app.callback()
def callback(
    _: bool = typer.Option(None, "--version", "-v", callback=version_callback)
) -> None:
    ...


@app.command()
def run(
    path: str = typer.Argument(help="Path to S lang code to run"),
    inputs: list[int] = typer.Argument(default=None, help="Input variables"),
) -> None:
    inputs = inputs or []
    code = read_file(path)

    result: int = run_code(code, inputs)
    typer.echo(f">>> {result}")
