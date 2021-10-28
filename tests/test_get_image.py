import unittest
import os
from PIL import Image

from src import get_image


class GetImageTest(unittest.TestCase):

    def test_image(self):
        self.image = get_image.image(
            lat=29.78, lon=-95.33, date='2018-01-01',
            dim=0.15, api_key='DEMO_KEY'
        )
        self.image_test = Image.open(
            os.path.join('tests', 'images_test', 'testimage1.png')
        )
        self.assertEqual(
            list(self.image.getdata()), list(self.image_test.getdata())
        )


if __name__ == '__main__':
    unittest.main()
