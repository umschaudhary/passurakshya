
from ast import literal_eval
import os
from datetime import date
from datetime import time
from datetime import datetime
import pyperclip as pc
from getpass import getpass
from termcolor import colored


dict = {}
file = ".file.txt"
path = os.path.join(os.path.expanduser("~"))
today=datetime.now()


def search(file, path):
    for root, dirs, files in os.walk(path):
        if file in files:
            return 1
        else:
            return 0


def save(username, password):
    d = get_directory()
    d[username] = password
    with open(os.path.join(os.path.expanduser("~"), file), "w+") as f:
        f.write("%s" % (d))
    return d


def get_directory():
    d = {}
    with open(os.path.join(os.path.expanduser("~"), file), "r+") as f:
        for files in f:
            if files == " ":
                d = {}
            else:
                d = literal_eval(files.strip())
    return d


def startup():
    if search(file, path) == 0:
        with open(os.path.join(os.path.expanduser("~"), file), "w+") as f:
            return {}
    else:
        return get_directory()


def user():
    print(colored("===================================","blue"))
    print(colored("===================================","blue"))
    print(colored(" Date and Time is :%s" % today,"green"))
    dict = startup()
    print(colored("\t1.Save Username and password","yellow"))
    print(colored("\t2.Retrieve password","yellow"))
    print(colored("\t3.Exit","yellow"))
    print(colored("===================================","blue"))
    print(colored("===================================","blue"))
    choice = int(input(colored(" Enter your choice : ","yellow")).strip())
    while True:
        if choice == 1:

            username = input(" Enter username : ").strip()
            while username == "":
                username = input(" UserName Required : ").strip()

            password = getpass(prompt=' Enter Password :').strip()
            while password == "":
                password = getpass(prompt=' Password Required: ').strip()
            cpassword=getpass(prompt=' Confirm Password : ').strip()

            while password!=cpassword:
                print("** Password Donot matched ***")
                password = getpass(prompt=' Enter Password : ').strip()
                cpassword=getpass(prompt=' Confirm Password : ').strip()
                

            
            dict = save(username, password)

            while input(" Save Another one (y/n): ").lower() == 'y':
                break
            else:
                print("\n\n=======================")
                print("1. Retrieve Your Password")
                print("2. Exit ")
                print("\n=======================")

                xchoice = input("\n Your Choice : ")
                if int(xchoice) == 1:
                    choice = 2

                elif int(xchoice) == 2:
                    print("\n Thank you !! ")
                    exit()

        elif choice == 2:
            dict = get_directory()
            ask = input(" Enter username : ").strip()
            while ask not in dict:
                ask = input(" Username Not Found !\n Enter Username : ").strip()

            passs = dict[ask]
            print(" Password For : %s : copied to clipboard . " % (ask))
            print(" You Can Paste using 'ctrl+v' Where You Want :) ")
            try:
                pc.copy(passs)
            except Exception:
                print(Exception)
            
                
            if input(" Retrive Another Password (y/n) :  ").lower() == "y":
                choice = 2
            else:
                user()

        else:
            exit()


user()
