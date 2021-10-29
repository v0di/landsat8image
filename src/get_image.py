import argparse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import os
import requests


def image(
    lat: float, lon: float, date: str = None, 
    dim: float = 0.15, info: bool = False,
    api_key: str = None) -> Image.Image:
    """
    Parameters:
            lat: latitude (float)
            lon: longitude (float)
            date: date in the yyyy-mm-dd format. Defaults to most recent date (str)
            dim: width and height of image in degrees. Defaults to 0.15 (float)
            info: write onto the image the latitude and the longitude. Defaults to False (bool)
            api_key: your NASA API key (str)
    Returns:
            An Image.Image object
    """
    if not date:
        date = datetime.now().strftime(r'%Y-%m-%d')

    payload = {
        'lat':lat,
        'lon':lon,
        'date':date,
        'dim':dim,
        'api_key':api_key,
    }
    response = requests.get(
        'https://api.nasa.gov/planetary/earth/imagery', 
        params=payload, 
        stream=True,
    )
    img = Image.open(response.raw)

    if info:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('arial.ttf', 46)
        draw.text((10, 10), f'LAT {lat}  LON {lon}', font=font, fill=(255, 0, 0))

    return img


def main():

    # -------------------- Command-Line Arguments Parsing -------------------- #
    parser = argparse.ArgumentParser(
        description="""
            Retrieves the Landsat 8 image for the supplied location and date
            from the Nasa Earth API.
        """
    )
    parser.add_argument('-lat', '-LAT', type=float, help='Latitude')
    parser.add_argument('-lon', '-LON', type=float, help='Longitude')
    parser.add_argument(
        '--date', '-DATE', nargs='?', type=str, help='Date in yyyy-mm-dd format. Defaults to today'
        )
    parser.add_argument(
        '--dim', '-DIM', nargs='?', default=0.15, type=float, 
        help='Width and height of image in degrees. Defaults to 0.15',
        )
    parser.add_argument(
        '--info', '-INFO', action='store_true', help='Writes lat and lon information onto the image'
        )
    parser.add_argument(
        '--save', '-SAVE', nargs='?', const='', help='Saves the image.'
        )
    args = parser.parse_args()
    # -------------------- End of Command-Line Arguments Parsing -------------------- #
    try:
        img = image(
            args.lat, args.lon, args.date, 
            args.dim, args.info, os.environ['NASA_API_KEY']
        )
        if args.save:
            try:
                img.save(args.save)
                print('Image saved successfully!')
            except ValueError:
                print('[ERROR] Unknown file extension. Image not saved!')
            except FileNotFoundError:
                print('[ERROR] Directory not found. Image not saved!')
        img.show()
    except UnidentifiedImageError:
        print('Could not fetch image. Try adjusting the parameters.')


if __name__ == '__main__':
    main()
