import os
import pics
import logging


def get_top_dirs(path):
    return [path + dirs for dirs in next(os.walk(path))[1]]


def get_files(path_list, extensions):
    return [
        os.path.join(root, name) for path in path_list for root, dirs, files in os.walk(path)
        for name in files if name.endswith(extensions)
    ]


def remove_files(path, extensions):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(extensions):
                os.remove(os.path.join(root, name))


def rename_jpgs(path):
    extensions = (".JPG", ".JPEG", ".jpeg")
    bad_jpgs = get_files(get_top_dirs(path), extensions)
    for jpg in bad_jpgs:
        os.rename(f"{jpg}", f"{os.path.splitext(jpg)[0]}.jpg")


def main():

    logging.captureWarnings(True)
    logging.basicConfig(filename='errors.txt', filemode='w')

    path = "E:\\Music\\"
    start = 0

    rename_jpgs(path)
    pictures = get_files(get_top_dirs(path)[start:], ('.jpg', '.png'))
    pics.convert_images_to_webm(pictures)


if __name__ == '__main__':
    main()
