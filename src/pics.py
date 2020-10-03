import os
from PIL import Image


def convert_images_to_webm(images):
    max_width = 1080
    for image_path in images:
        img = Image.open(image_path).convert('RGB')
        # remove file extension
        image_name = os.path.splitext(image_path)[0]

        # resize if MP3 and cover too large
        if '[FLAC]' not in image_name and img.size[0] > max_width:
            print(f"Resizing {image_path}")
            factor = (max_width / float(img.size[0]))
            height = int((float(img.size[1]) * float(factor)))
            img = img.resize((max_width, height), resample=Image.LANCZOS)
            img.save(f"{image_name}.webp", 'webp', lossless=True)
            os.remove(image_path)
        # keep smaller if FLAC or cover not too large
        else:
            img.save(f"{image_name}.webp", 'webp', lossless=True)
            if os.stat(f"{image_name}.webp").st_size > os.stat(image_path).st_size:
                print(f"Keeping {image_path}")
                os.remove(f"{image_name}.webp")
            else:
                print(f"Replacing {image_path}")
                os.remove(image_path)
