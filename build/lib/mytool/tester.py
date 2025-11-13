import click
import os

@click.group()
def cli():
    """Main command group for tool."""
    click.echo("I'm functional")
    pass

@cli.command()
@click.option('--count', default=1)
def say(count):
    for time in range(count):
        click.echo("hello there")

@cli.command()
def myls():
    click.echo(os.listdir(path="."))
    click.secho("listed files", fg = "green", bold = True) 
