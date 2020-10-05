import os
import pics
import logging


def get_files(path, extensions, start=0):
    top_dirs = [path + dirs for dirs in next(os.walk(path))[1]]

    return [
        os.path.join(root, name) for top_dir in top_dirs[start:] for root, dirs, files in os.walk(top_dir)
        for name in files if name.endswith(extensions)
    ]


def remove_files(path, extensions):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(extensions):
                os.remove(os.path.join(root, name))


def main():

    logging.captureWarnings(True)
    logging.basicConfig(filename='errors.txt', filemode='w')

    # needs ending \\
    path = "E:\\Music\\"
    start = 0
    # pics.rename_jpgs(path)
    pictures = get_files(path, ('.jpg', '.png'), start)
    # print(pictures)
    pics.convert_images_to_webm(pictures)


if __name__ == '__main__':
    main()
