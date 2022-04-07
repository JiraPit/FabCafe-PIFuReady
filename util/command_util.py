import os

OUT=".."

def command(cmd : str):
    print(cmd)
    ret = os.system(cmd)
    print(ret)

def change_directory(directory : str):
    print("chdir {0}".format(directory))
    ret = os.chdir(directory)
    print(ret)