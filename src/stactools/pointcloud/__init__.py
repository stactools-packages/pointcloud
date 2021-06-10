# flake8: noqa

from stactools.pointcloud.stac import create_item
import stactools.core

stactools.core.use_fsspec()


def register_plugin(registry):
    # Register subcommands

    from stactools.pointcloud import commands

    registry.register_subcommand(commands.create_pointcloud_command)


__version__ = '0.1.5'
