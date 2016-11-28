import click
from api.cli import pass_context
@click.command()
@pass_context
def command(ctx):
    """Show the api version information"""
    from api import __version__
    ctx.log('api:')
    ctx.log(' Version:      %s' % __version__)