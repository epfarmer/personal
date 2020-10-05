import os
from PIL import Image


def convert_images_to_webm(images):
    max_width = 1080
    for image_path in images:
        img = Image.open(image_path).convert('RGB')
        # remove file extension
        name, ext = os.path.splitext(image_path)
        # only resize if mp3 cover is too big
        if '[FLAC]' not in name and name[-5:] == 'cover' and img.size[0] > max_width:
            print(f"{'Resizing ':10}{image_path}")
            img.thumbnail((max_width, -1), resample=Image.LANCZOS)
            img.save(f"{name}.webp", 'webp', lossless=True)
            os.remove(image_path)
        # else keep min(jpg, webp), replace png
        else:
            img.save(f"{name}.webp", 'webp', lossless=True)
            if ext == '.jpg' and os.stat(f"{name}.webp").st_size > os.stat(image_path).st_size:
                print(f"{'Keeping ':10}{image_path}")
                os.remove(f"{name}.webp")
            else:
                print(f"{'Replacing ':10}{image_path}")
                os.remove(image_path)


def rename_jpgs(path):
    extensions = (".JPG", ".JPEG", ".jpeg")
    bad_jpgs = [
        os.path.join(root, name) for root, dirs, files in os.walk(path)
        for name in files if name.endswith(extensions)
    ]
    for jpg in bad_jpgs:
        os.rename(f"{jpg}", f"{os.path.splitext(jpg)[0]}.jpg")
