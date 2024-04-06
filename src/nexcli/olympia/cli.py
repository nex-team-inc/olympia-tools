import click

from . import apksigner, cms, deviceid

@click.group("olympia")
def cli():
    """Olympia commands."""
    pass

cli.add_command(deviceid.decode_tracking_id)
cli.add_command(cms.create_release, 'release-apk')
cli.add_command(apksigner.cli)