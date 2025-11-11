import click

@click.command()
@click.option('--count', default=1)
def say(count):
    for time in range(count):
        click.echo("hello there")
