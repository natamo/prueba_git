#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from git import Repo
import time


local_repo_directory = os.path.join(os.getcwd(), 'prueba_1')
destination = 'main'

def chdirectory(path):
    os.chdir(path)


def add_and_commit_changes(repo):
    print("Commiting changes")
    repo.git.add(update=True)
    repo.git.commit("-m", "Adding a new line to the file.txt")

def main():

    repo = Repo(local_repo_directory)

    #add and commit changes
    add_and_commit_changes(repo)


if __name__ == "__main__":
    main()
