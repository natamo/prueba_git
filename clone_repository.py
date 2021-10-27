#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from git import Repo 

local_repo_directory = os.path.join(os.getcwd(), 'prueba_1')
destination = 'main'


def clone_repo():
    if os.path.exists(local_repo_directory):
        print("Directory exists, pulling changes from main branch")
        repo = Repo(local_repo_directory)
        origin = repo.remotes.origin
        origin.pull(destination)
    else:
        print("Directory does not exists, cloning")
        Repo.clone_from("https://github.com/natamo/prueba_git.git",
                        local_repo_directory, branch=destination)

def main():

    # Clone repository 
    clone_repo()

if __name__ == "__main__":
    main()
