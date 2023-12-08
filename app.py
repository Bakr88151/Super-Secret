import sqlite3
import sys
from utils import secret_message
import getpass
from colorama import Fore, Style
import hashlib

def main():
    un, pw = get_info()
    if len(check_user(un, pw)) == 0:
        print(Fore.RED + "Acess denied" + Style.RESET_ALL)
        sys.exit(2)
    else:
        print(Fore.GREEN + "Acess granted!" + Style.RESET_ALL)
        secret_message()
        sys.exit(0)


def get_info():
    if len(sys.argv) == 3:
        return sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 1:
        un = input("Please input your User_name: ")
        pw = getpass.getpass("Enter your password: ")
        return un, pw
    else:
        print(Fore.RED + "Too many arguments" + Style.RESET_ALL)
        sys.exit(1)


def check_user(un, pw):
    con = sqlite3.connect('secret.db')
    cur = con.cursor()
    hased_pw = hashlib.md5(pw.encode()).hexdigest()
    res = cur.execute(f"SELECT * FROM users WHERE username = '{un}' AND password = '{hased_pw}';")
    return list(res)


if __name__ == "__main__":
    main()