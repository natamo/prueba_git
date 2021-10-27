#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from git import Repo
import time


local_repo_directory = os.path.join(os.getcwd(), 'prueba_1')
destination = 'main'

def chdirectory(path):
    os.chdir(path)


def update_file():
    print("Modifying the file")
    chdirectory(local_repo_directory) #como un cd /directorio
    opened_file = open("file.txt", 'a') #agrega al final del archivo
    opened_file.write("{0} added at {1} \n".format(
        "I am a new string", str(time.time())))



def main():

    #update file 
    update_file()

if __name__ == "__main__":
    main()
