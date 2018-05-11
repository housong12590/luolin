import os
import click


def register(app):
    @app.cli.group()
    def translate():
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        pass

    @translate.command()
    def update():
        pass
