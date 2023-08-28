import os
import unittest

from tempfile import TemporaryDirectory

import pystac

from click import Group
from click.testing import CliRunner
from stactools.pointcloud.commands import create_pointcloud_command


class CreateItemTest(unittest.TestCase):

    def test_create_item(self):
        href = f"{os.path.dirname(__file__)}/data-files/autzen_trim.las"
        with TemporaryDirectory() as directory:
            runner = CliRunner()
            runner.invoke(
                create_pointcloud_command(Group()),
                ["create-item", href, directory],
            )
            jsons = [p for p in os.listdir(directory) if p.endswith('.json')]
            self.assertEqual(len(jsons), 1)
            item_path = os.path.join(directory, jsons[0])
            item = pystac.read_file(item_path)
        item.validate()
