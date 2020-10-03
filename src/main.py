import os
import pics
import warnings
import logging



def get_files(path, extensions):
    return [
        os.path.join(root, name) for root, dirs, files in os.walk(path)
        for name in files if name.lower().endswith(extensions)
    ]


def remove_files(path, extensions):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(extensions):
                os.remove(os.path.join(root, name))


def main():

    logging.captureWarnings(True)
    logging.basicConfig(filename='errors.txt', filemode='w')
    path = "G:/Card/"
    extensions = ("cover.jpg", "cover.jpeg", "cover.png", "cover.webp")
    # extensions = (".webp")
    pictures = get_files(path, extensions)
    print(pictures)
    pics.convert_images_to_webm(pictures)
    # remove_files(path, extensions)


if __name__ == '__main__':
    main()
