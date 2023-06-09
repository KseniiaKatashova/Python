"""This module provides UI for phone_book"""

from pathlib import Path
from phone_book import __app_name__, __version__, model, config, ERRORS
import typer
from typing import Optional

from typing_extensions import Annotated

#створюємо екземпляр Typer.
app = typer.Typer()

@app.command()
def init(db_path: str = typer.Option(str(model.DEFAULT_DB_FILE_PATH), "--db-path", "-db", prompt="Phone_book database location?")) -> None:
   """Initialize the Phone_book database."""
   app_init_error = config.init_app(db_path)
   print("app_init_error ", app_init_error)
   if app_init_error:
      typer.secho(
         f'Creating config file failed with "{ERRORS[app_init_error]}"', fg=typer.RED
      )
      raise typer.Exit(1)
   db_init_error = model.init_database(Path(db_path))
   if db_init_error:
      typer.secho(
         f'Creating database failed with "{ERRORS[db_init_error]}"',
         fg=typer.colors.RED
      )
      raise typer.Exit(1)
   else:
      typer.secho(
         f'The Phone_book database location is {db_path}',
         fg=typer.colors.GREEN
      )

def _version_callback(value) :
   if value:
       typer.echo(f"{__app_name__} v{__version__}")
       raise typer.Exit()


@app.callback()
def main(
   version: Annotated[
      Optional[bool], 
      typer.Option("--version",  "-v", help="Show the application's version and exit.",  callback=_version_callback, is_eager=True)
   ] = None
   ) -> None:
   return