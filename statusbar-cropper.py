from sys import argv, exit
from pathlib import Path
from imghdr import what

from PIL import Image


def crop_statusbar(image_list):
    for image_str in image_list:
        image_path = Path(image_str)

        if what(image_path) is None:
            continue

        image = Image.open(image_path)
        w, h = image.size
        if w != 750 or h != 1334:
            continue

        image_crop = image.crop((0, 32, w, h))

        image_crop.save(Path("result/" + image_path.name), quality=95)


def main():
    if len(argv) < 2:
        exit()

    image_list = argv[1:]

    if not Path("result").is_dir():
        Path("result").mkdir()
    crop_statusbar(image_list)


if __name__ == '__main__':
    main()
