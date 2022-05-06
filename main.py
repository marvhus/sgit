#!/usr/bin/env python3

import os

LOGO = """









                                                          7YJ.
                                                          P@@:             ?P5.
                                                          :^:              P@@:
                 .~?Y555Y?!.        ^?Y55J! ~?7.     .????777.        :????B@@J?????^
                ?#@B5YYY5G&!      ^G@@PYY5BBB@@^     .5PPP&@@:        ^PPPP#@@PPPPPP!
               :@@G       ..     ^&@B:     J@@@^          P@&:             5@&:
               .B@@Y!^:.         P@@~       G@@^          P@&:             5@&:
                .75B#&&&#G?.     B@&:       5@@^          P@&:             5@&:
                    ..^!Y@@B.    P@@~       G@@^          P@&:             P@&:
               ..        P@@^    ^&@B:     J@@@^          P@&.             Y@@~
               ~&B5J?7?YB@&?      ^G@@GYY5BBG@@^    :YYYYJ#@@5JYYY!        :B@&PYYYY~
               .!J5PGGGPY!.         ^?Y55J! 5@@:    ^YYYYYYYYYYYY57          ~7JYYY5~
                                   .       ^&@5
                                  .BBPYJJYG@&Y.
                                   ~7JY55Y?~.









"""

def config():
    print("Please enter your desired git username")
    name = input("> ")

    print()

    print("Please enter your desired git email")
    email = input("> ")
    
    print("\n#-----#\n")
    os.system(f'git config --local user.name "{name}"')
    print("\n#-----#\n")
    os.system(f'git config --local user.email "{email}"')

def clone():
    config()
  
    print()
  
    print("Please enter the name of the user/organization that owns the GitHub repository")
    user = input("> ")

    print()

    print("Please enter the name of the repository")
    repo = input("> ")

    url = f"https://github.com/{user}/{repo}.git"

    print("\n#-----#\n")
    os.system(f"git clone {url}")
    print("\n#-----#\n")

def init():
    config()
    
    print()
  
    print("Please enter your GitHub username/organization name")
    user = input("> ")

    print()

    print("Please enter the name of the repository")
    repo = input("> ")

    print()

    print("Please enter the name of the main branch")
    mainBranch = input("> ")

    url = f"https://github.com/{user}/{repo}.git"
    
    print("\n#-----#\n")
    os.system("git init")
    print("\n#-----#\n")
    os.system("git add *")
    print("\n#-----#\n")
    os.system('git commit -m "inital" -S')
    print("\n#-----#\n")
    os.system(f"git remote add origin {url}")
    print("\n#-----#\n")
    os.system(f"git branch -m {mainBranch}")
    print("\n#-----#\n")

def commit():
    print("Please enter the commit message")
    message = input("> ")

    print()

    print("Do you want to fetch before commiting?")
    fetch = input("(y/N) > ")

    if fetch == '':
        print("\n\n")
        os.system("git fetch")

    print("\n#-----#\n")
    os.system("git add -A")
    print("\n#-----#\n")
    os.system(f'git commit -m "{message}" -S')
    print("\n#-----#\n")

def push():
    print("Please enter the name of the remote")
    remote = input("> ")

    print()

    print("Please enter the name of the branch")
    branch = input("> ")

    print("\n#-----#\n")
    os.system(f"git push -u {remote} {branch}")
    print("\n#-----#\n")

def pull():
    print("\n#-----#\n")
    os.system("git pull")
    print("\n#-----#\n")

def mainMenu():
    options = [
        "config",
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

    if   mode == 'config':  config()
    elif mode == 'clone':   clone()
    elif mode == 'init':    init()
    elif mode == 'commit':  commit()
    elif mode == 'push':    push()
    elif mode == 'pull':    pull()
    else: # Shouldn't happen
        print("WTF did you do, this shouldn't happen!")

if __name__ == '__main__':
    main()
