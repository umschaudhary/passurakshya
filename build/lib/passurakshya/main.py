from ast import literal_eval
import os
from datetime import datetime
import pyperclip as pc
from getpass import getpass
from termcolor import colored

dict = {}
file = ".file.txt"
path = os.path.join(os.path.expanduser("~"))
today = datetime.now()


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
    print(colored("=====WELCOME TO PASSURAKSHYA======", "green"))
    print(colored("===================================", "blue"))
    print(colored("===================================", "blue"))
    print(colored(" Date and Time is :%s" % today, "green"))
    dict = startup()
    print(colored("\t1.Save Username and password", "yellow"))
    print(colored("\t2.Retrieve password", "yellow"))
    print(colored("\t3.Update Password", "yellow"))
    print(colored("\t4.Exit ", "yellow"))
    print(colored("===================================", "blue"))
    print(colored("===================================", "blue"))
    choice = int(input(colored(" Enter your choice : ", "yellow")).strip())
    while True:
        if choice == 1:

            username = input(colored(" Enter username : ", "yellow").strip())
            while username == "":
                print (colored(" ***Please Enter Username***", "red"))
                username = input(colored(" Enter Username : ", "yellow").strip())
            while username in dict:
                print(colored(" ***Username already exits*** ", "red"))
                username = input(colored(" Enter username : ", "yellow").strip())

            password = getpass(prompt=' Enter Password :').strip()
            while password == "":
                password = getpass(prompt=' Password Required: ').strip()
            cpassword = getpass(prompt=' Confirm Password : ').strip()

            while password != cpassword:
                print(colored("** Password Don't matches ***", "red"))
                password = getpass(prompt=' Enter Password : ').strip()
                cpassword = getpass(prompt=' Confirm Password : ').strip()

            dict = save(username, password)
            print(colored(" Username and Password saved ", "green"))
            while input(colored(" Save Another one (y/n): ", "yellow")).lower() == 'y':
                break
            else:
                print(colored("\n\n=======================", "blue"))
                print(colored(" 1. Retrieve Your Password", "yellow"))
                print(colored(" 2. Update password ", "yellow"))
                print(colored(" 3. Exit ", "yellow"))
                print(colored("\n=======================", "blue"))

                xchoice = input(colored("\n Your Choice : ", "yellow"))
                if int(xchoice) == 1:
                    choice = 2
                if int(xchoice) == 2:
                    choice = 3

                elif int(xchoice) == 3:
                    print(colored(" !! Thank you !!\n ", "green"))
                    print(colored(" ==========================\n", "green"))
                    exit()

        elif choice == 2:
            dict = get_directory()
            ask = input(colored(" Enter username : ", "yellow")).strip()
            while ask not in dict:
                print (colored(" Username Not Found !", "red"))
                ask = input(colored(" Enter Username : ", "yellow")).strip()

            passs = dict[ask]
            print(colored(" Password For : %s : copied to clipboard . " % ask, "green"))
            print(colored(" You Can Paste using 'ctrl+v' Where You Want", "green"))
            try:
                pc.copy(passs)
            except Exception:
                print(Exception)

            if input(colored(" Retrive Another Password (y/n) :  ", "yellow")).lower() == "y":
                choice = 2
            else:
                user()

        elif choice == 3:
            dict = get_directory()
            ask = input(colored(" Enter username : ", "yellow")).strip()
            while ask=="":
                print(colored(" **Username required : ", "red"))
                ask = input(colored(" Enter username : ", "yellow")).strip()
            while ask not in dict:
                print (colored(" Username Not Found !", "red"))
                ask = input(colored(" Enter Username : ", "yellow")).strip()
            passs = dict[ask]
            opassword = getpass(prompt=' Enter old password : ')
            while opassword != passs:
                print(colored(' ***Password doesnot matched*** :', 'red'))
                opassword = getpass(prompt=' Enter old password : ').strip()
            npass = getpass(prompt=' Enter new password : ').strip()
            while npass == "":
                print(colored(" ***Password can't be Empty*** :", "red"))
                npass = getpass(prompt=' Enter new password : ').strip()
            cpass=getpass(prompt=' Confirm Password :').strip()
            while cpass != npass:
                print(colored("**Password doesn't Matched **", "red"))
                npass = getpass(prompt=' Enter new Password : ').strip()
                cpass = getpass(prompt=' Confirm Password : ').strip()
            save(ask, npass)

            if input(colored(" Update Another Password (y/n) :  ", "yellow")).lower() == "y":
                choice = 3
            else:
                user()

        else:
            print(colored("!!!Thank you !!!\n", "green"))
            print(colored(" ============================\n", "green"))
            exit()

def main():
    user()


if __name__ == '__main__':
    main()
