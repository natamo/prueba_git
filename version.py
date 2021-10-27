#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from git import Repo
import time


local_repo_directory = os.path.join(os.getcwd(), 'prueba_1')
destination = 'main'

def chdirectory(path):
    os.chdir(path)


#def push_changes(repo):
#    print("Push changes")
#    repo.git.push("--set-upstream", 'origin', destination)

def versioning(repo):
    print("versioning...")
    repo.git.tag("-a", "v2", "7a5ebcd", "-m", "version1")
    #repo.git.push("origin", tagname)

def main():

    repo = Repo(local_repo_directory)

    #pushing changes
    versioning(repo)

if __name__ == "__main__":
    main()
