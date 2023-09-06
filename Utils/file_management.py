import os

def remove_all_files_from_directory():
    dir = 'Downloads'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

def remove_file_from_directory(directory, file):
    os.remove(os.path.join(directory, file))
