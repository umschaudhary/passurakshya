
from ast import literal_eval
import os
from datetime import date
from datetime import time
from datetime import datetime
import pyperclip as pc


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
    print("Current Date and Time is :%s" % today)
    dict = startup()
    print("1.Save Username and password")
    print("2.Retrieve password")
    print("3.Exit")
    choice = int(input("enter your choice : ").strip())
    while True:
        if choice == 1:

            username = input("enter username : ").strip()
            password = input("enter password : ").strip()
            dict[username] = password

            dict = save(username, password)

            while input("do you want to continue").lower() == 'y':
                break
            else:

                xchoice = input("\n1. Retrieve Your Password  \n2. Exit \nChoice : ")
                if int(xchoice) == 1:
                    choice = 2

                elif int(xchoice) == 2:
                    print("Thanks you ")
                    exit()

        elif choice == 2:
            dict = get_directory()
            ask = input("enter username : ").strip()
            while ask not in dict:
                ask = input("Username Incorrect enter username again : ").strip()

            passs = dict[ask]
            print("Your password is : %s"%(passs))
            try:
                pc.copy(passs)
            except Exception:
                print(Exception)
            
                
            if input("enter y to retrive another password :  ").lower() == "y":
                choice = 2
            else:
                user()

        else:
            exit()


user()
