import os
import sys
import subprocess
import time
import datetime
import multiprocessing
from playsound3 import playsound
from random import randint
from tabulate import tabulate
from os import walk

# System modules
def sys_load(d, s):
    spinner_chars = ['/', '-', '\\', '|']
    start_time = time.time()
    i = 0
    while time.time() - start_time < d:
        sys.stdout.write('\r>' + s + spinner_chars[i % len(spinner_chars)] + ' ')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\n")
    sys.stdout.flush()

def terminalinp(command):
    global termsuccess
    try:
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            shell=True,
            check=True
        )
        termsuccess = True
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f">{e.stderr}")
        termsuccess = False

# Extra modules
def koi(par1="", par2="", par3=""):
    # Fancier file management module
    with open('extras_dir\\koi-mem', 'r') as koimem:
        cl_chk = koimem.read()
        koimem.close()
    if cl_chk == "Enabled":
        status1 = "\033[32m"
        status2 = "\033[32m"
        green = "\033[32m"
        red = "\033[31m"
        yellow = "\033[33m"
        reset = "\033[39m"
    else:
        status1 = "\033[32m"
        status2 = "\033[31m"
        green = "\033[39m"
        red = "\033[39m"
        yellow = "\033[39m"
        reset = "\033[39m"

    if par1 == "":
        return print(f">Koi - The fancy file management module.\n Terminal text color: {status1}Supported" \
        f"\n {reset}Colored text: {status2}{cl_chk}\n {reset}Version 1.5.002\n Created by Fischell Benson, 20XX")
    elif par1 == "dir":
        if par2 == "":
            return print(">Koi is missing an important argument. Please input the target dir parameter.")
        else:
            try:
                with open("userdir_par", "r") as pars:
                    parslist = pars.read().splitlines()
                    parsindex = parslist.index(par2) + 1
                    dirname = parslist[parsindex]
                    pars.close()

                    if par3 == "-root":
                        path = 'D:/Projects/COMMSDOS'
                    else:
                        path = f'D:/Projects/COMMSDOS/{dirname}'
                    files = []
                    dirs = []
                    for (dirpath, dirnames, filenames) in walk(path):
                        dirs.extend(dirnames)
                        files.extend(filenames)
                        break

                    contents = []
                    contents.extend(dirs)
                    contents.extend(files)
                    len_dirs = len(dirs)
                    len_files = len(files)
                    if len(contents) != 0:
                        dirlist = []
                        for i in range(len_dirs):
                            templist = []
                            templist.append(str(i + 1))
                            templist.append(dirs[i])
                            templist.append(f"{green}Directory{reset}")
                            dirlist.append(templist)

                        for i in range(len_files):
                            templist = []
                            templist.append(str(len_dirs + (i+1)))
                            templist.append(files[i])
                            templist.append(f"{yellow}File{reset}")
                            dirlist.append(templist)

                        dirlistheader = ["No.", "Name", "Type"]
                        print(tabulate(dirlist, headers=dirlistheader, tablefmt="heavy_outline"))
                    else:
                        return print(f">Koi has found zero files in directory '{dirname}'.")
            except ValueError:
                return print(f">Koi cannot recognize '{par2}' as a real dir parameter.")
                
    elif par1 == "-dcl":
        with open('extras_dir\\koi-mem', 'w') as koimem:
            koimem.write("Disabled")
            koimem.close()
        return print(">Colored terminal text: Disabled")
    elif par1 == "-ecl":
        with open('extras_dir\\koi-mem', 'w') as koimem:
            koimem.write("Enabled")
            koimem.close()
        return print(">Colored terminal text: Enabled")
    else:
        return print(">Unknown Koi command, please try again.")
    