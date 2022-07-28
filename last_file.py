import glob
import os

def run():
    list_of_files = glob.glob('./saved/*') # * means all files in the folder
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file=latest_file[8::]
    a=latest_file.split(".")
    return a[0]