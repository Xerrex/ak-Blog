import os
import click


@click.group()
def translate():
    """Translation and localization commands."""
    pass

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language.

    Takes a language code argument where muliple language
    translations exist. ie flask translate english
    """

    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel init -i messages.pot -d my_core/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')

@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d my_core/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')

@translate.command()
def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d my_core/translations'):
        raise RuntimeError('compile command failed')

def cli_init_app(app):
    """register commands with flask app

    Args:
        app (Flask): Flask app instance
    """
    app.cli.add_command(translate)
    