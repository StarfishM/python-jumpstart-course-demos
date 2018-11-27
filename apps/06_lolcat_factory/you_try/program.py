import os
import platform
import subprocess

import cat_service


def main():
    print_the_header()
    folder = get_or_create_output_folder()
    print('found or created folder' + folder)
    download_cats(folder)
    display_cats(folder)


def print_the_header():
    print('-------------------------')
    print("      LOLCat Factory")
    print('-------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = "Cat_Pictures"
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('making new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('contacting server to download your funny cats')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print('downloading cat ' + name)
        cat_service.get_cat(folder, name)


print('done')


def display_cats(folder):
    # open folder
    print('Displaying your content now...')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print('Sorry mate, we do not support your OS, what the heck are you on?' + platform.system())


if __name__ == '__main__':
    main()
