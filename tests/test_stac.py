import datetime
import os
import unittest

from pystac.extensions.pointcloud import PointcloudExtension
from pystac.extensions.projection import ProjectionExtension
from stactools.pointcloud.stac import create_item


class StacTest(unittest.TestCase):

    def test_create_item(self):
        path = f"{os.path.dirname(__file__)}/data-files/autzen_trim.las"
        item = create_item(path)
        self.assertEqual(item.id, "autzen_trim")
        self.assertEqual(item.datetime, datetime.datetime(2015, 9, 10))

        ProjectionExtension.validate_has_extension(item)
        pointcloud_ext = PointcloudExtension.ext(item)
        self.assertEqual(pointcloud_ext.count, 110000)
        self.assertEqual(pointcloud_ext.type, "lidar")
        self.assertEqual(pointcloud_ext.encoding, "las")
        self.assertEqual(pointcloud_ext.statistics, None)
        self.assertTrue(pointcloud_ext.schemas)

        item.validate()

    def test_create_item_with_statistic(self):
        path = f"{os.path.dirname(__file__)}/data-files/autzen_trim.las"
        item = create_item(path, compute_statistics=True)
        pointcloud_ext = PointcloudExtension.ext(item, add_if_missing=True)
        self.assertNotEqual(pointcloud_ext.statistics, None)

    def test_create_item_from_url(self):
        url = "https://github.com/PDAL/PDAL/raw/2.2.0/test/data/las/autzen_trim.las"
        item = create_item(url)
        item.validate()

    def test_create_item_with_custom_crs(self):
        path = f"{os.path.dirname(__file__)}/data-files/moon.las"
        item = create_item(path, a_srs="IAU_2015:30100")
        self.assertEqual(item.id, "moon")
        ProjectionExtension.validate_has_extension(item)
        pointcloud_ext = PointcloudExtension.ext(item)
        # Check that the lunar radius is in the proj string.
        self.assertIn('1737400', item.properties['proj:wkt2'])
        self.assertEqual(pointcloud_ext.count, 5538)
        self.assertEqual(pointcloud_ext.type, "lidar")
        self.assertEqual(pointcloud_ext.encoding, "las")
        self.assertEqual(pointcloud_ext.statistics, None)
        self.assertTrue(pointcloud_ext.schemas)
