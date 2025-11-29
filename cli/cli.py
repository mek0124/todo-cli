

import click


@click.group(name="todo")
def cli() -> None:
    """
    Something here
    """
    pass


if __name__ == '__main__':
    cli()