#!/usr/bin/env python3

import os

LOGO = """
           _ _
          (_) |
 ___  __ _ _| |_
/ __|/ _` | | __|
\__ \ (_| | | |_
|___/\__, |_|\__|
      __/ |
     |___/

"""

def clone():

    print("Please enter the name of the user/organization that owns the GitHub repository")
    user = input("> ")

    print()

    print("Please enter the name of the repository")
    repo = input("> ")

    url = f"git@github.com:{user}/{repo}"

    print("\n\n")
    os.system(f"git clone  {url}")
    print("\n\n")

def init():

    print("Please enter your GitHub username/organization name")
    user = input("> ")

    print()

    print("Please enter the name of the repository")
    repo = input("> ")

    print()

    print("Please enter the name of the main branch")
    mainBranch = input("> ")

    url = f"git@github.com:{user}/{repo}"

    print("\n\n")
    os.system("git init")
    print("\n\n")
    os.system(f"git remote add origin {url}")
    print("\n\n")
    os.system(f"git branch -M {mainBranch}")
    print("\n\n")

def commit():

    print("Please enter the commit message")
    message = input("> ")

    print("\n\n")
    os.system("git add *")
    print("\n\n")
    os.system(f"git commit -m '{message}' -S")
    print("\n\n")

def push():

    print("Please enter the name of the remote")
    remote = input("> ")

    print()

    print("Please enter the name of the branch")
    branch = input("> ")

    print("\n\n")
    os.system(f"git push -u {remote} {branch}")
    print("\n\n")

def pull():

    print("\n\n")
    os.system("git pull")
    print("\n\n")

def mainMenu():
    options = [
        "clone",
        "init",
        "commit",
        "push",
        "pull",
    ]
    for option in options:
        print(f"- {option}")
    while True:
        print("\nEnter name the option you want to pick")
        answer = input("> ")
        if answer not in options:
            print("That is not an option!")
            continue
        return answer

def main():
    print(LOGO)
    mode = mainMenu()

    if   mode == 'clone':   clone()
    elif mode == 'init':    init()
    elif mode == 'commit':  commit()
    elif mode == 'push':    push()
    elif mode == 'pull':    pull()
    else: # Shouldn't happen
        print("WTF did you do, this shouldn't happen!")


if __name__ == '__main__':
    main()
