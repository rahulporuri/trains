import glob
import os

list_of_files = glob.glob('del/*-10-*')


for filename in list_of_files:
    os.remove(filename)

list_of_files = glob.glob('del/*-9-*')


for filename in list_of_files:
    os.remove(filename)


list_of_files = glob.glob('del/*_1-11-*')


for filename in list_of_files:
    os.remove(filename)

list_of_files = glob.glob('del/*_2-11-*')


for filename in list_of_files:
    os.remove(filename)
