from app import create_app, cli

app = create_app(None)
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return


if __name__ == '__main__':
    app.run()
