import os
from PIL import Image


def convert_image(images):
    max_width = 1080
    for image_path in images:
        img = Image.open(image_path).convert('RGB')
        # split the image path (to avoid the .jpg or .png being part of the image name):
        image_name = os.path.splitext(image_path)[0]

        if ' [FLAC]\\' not in image_name and img.size[0] > max_width:
            print(f"Resizing: {image_name}")
            factor = (max_width / float(img.size[0]))
            height = int((float(img.size[1]) * float(factor)))
            img = img.resize((max_width, height), resample=Image.LANCZOS)
        print(f"Converting: {image_name}")
        img.save(f"{image_name}.webp", 'webp', lossless=True)
        os.remove(image_path)


def main():

    path = "E:/Music/Black Metal/Lamp of Murmuur/(2020-10) Heir of Ecliptical Romanticism [FLAC]"

    pics = [
        os.path.join(root, name) for root, dirs, files in os.walk(path)
        for name in files if name.endswith((".jpg", ".jpeg", ".png"))
    ]
    convert_image(pics)


if __name__ == '__main__':
    main()
