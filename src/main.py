from textnode import TextNode
from blocks_markdown import generate_page
import os
import shutil

def copy_paths_to_target_dir(destination, origin):
    dirs = os.listdir(origin)
    for directory in dirs:
        if os.path.isdir(os.path.join(origin, directory)):
            if not os.path.exists(os.path.join(destination, directory)):
                os.mkdir(os.path.join(destination, directory))
            copy_paths_to_target_dir(os.path.join(destination, directory), os.path.join(origin, directory))
        if os.path.isfile(os.path.join(origin, directory)):
            shutil.copy(os.path.join(origin, directory), os.path.join(destination, directory))

def copy_directory_to_directory(destination, origin):
    dir_path = os.path.join(os.getcwd(), destination)
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    copy_paths_to_target_dir(destination, origin)

def main():
    copy_directory_to_directory("public", "static")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()

