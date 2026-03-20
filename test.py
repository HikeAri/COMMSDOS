import os
import sys
import subprocess
import time
import datetime
import extras
from random import randint
from tabulate import tabulate
from os import walk

logo_ascii = """
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                                                                                                                        
                                                                                                                          .....                          
                                                                                                                          ;:;;..                         
                                                                                                                          ;::;:.                         
                                                                                                              :;:....::.. .....                          
                                                                                                            .;..      .::.                               
                                                                                                           .:           ::                               
                                                                                                           ;.            +                               
                                                                                                           ::           .:                               
                                                                                                            ::.       ..;.                               
                                                                                                             .::.....:::.                                
                                                                                                                ..::..                                   
                                                                                                            ::::::::.                                    
                                                                                                            +      .::.                                  
                                                                                                            +       ..::.                                
                                                                                                            +          .;.                               
                                                                                                            +           ;.                               
                                                                                                            +           ;.                               
                                                                                                            +           ;.                               
                                                                                                            +           ;.                               
                                                                                                            +           ;.                               
                                                                                                  ....::;;+++           ;.                               
                                                                                         ..:+++;::::::::::::+           ;.                               
                                                                                   .:++;::::::::::::::::::::+           ;.                               
                                                                             ...;;::::::::::::::::::::::::::+           ;.                               
                                                                           .:;::::::::::::::::::::::::::::::+           ;.                               
                                                                         ..;::::::::::::::::::::::::::::::::+           ;.                               
                                                                         .:;::::::::::::::::::::::::::::::::+.          ;.                               
                                                                         .;;::::::::::::::::::;;;;;::::::::..::.        ;.                               
                                                                         .::;;::::::::;;;:::......            .::.      ;.                               
                                                                         .:....;;;+:.....                      ..;;;;;;;+.                               
                                                                         .:.     ..;+:.                       .:                                         
                                                                         .:.          ...:;;:.......          .+:..                                      
                                                                         .:.                   ....:;;;;;::...:;.::.                                     
                                                                         .:.                                      .::.                                   
                                                                          .::.                                      .::.                                 
                                                                           ..:::.                                    ..:..                               
                                                                              ...:;:.                                  ::.                               
                                                                                  ....:;;:.                          .:..                                
                                                                                       .......:;;;;::..            .;..                                  
                                                                                                       ......::;..;.                                     
                                                                                                              .;::.                                      
                                                                                                              .:.                                        




                                                  _______ _            _  __         _          _        ____            _   _                      _____       
                                                 |__   __| |          | |/ /        | |        (_)      |  _ \          | | | |                    / ____|      
                                                    | |  | |__   ___  | ' / ___  ___| |____   ___  ___  | |_) |_ __ ___ | |_| |__   ___ _ __ ___  | |     ___   
                                                    | |  | '_ \ / _ \ |  < / _ \/ __| '_ \ \ / / |/ __| |  _ <| '__/ _ \| __| '_ \ / _ \ '__/ __| | |    / _ \  
                                                    | |  | | | |  __/ | . \ (_) \__ \ | | \ V /| | (__  | |_) | | | (_) | |_| | | |  __/ |  \__ \ | |___| (_) | 
                                                    |_|  |_| |_|\___| |_|\_\___/|___/_| |_|\_/ |_|\___| |____/|_|  \___/ \__|_| |_|\___|_|  |___/  \_____\___(_)
                                                                                                                
                                                                                                                                                                                                                
"""

os.system(f'title ORTHOS-1000B Desktop')
pw_store = ["Adm123"]
sysdir = ["floppy_disks", "dos_storage_dir", "ct_signalcatch", "act_ipfetch", "catalyst_pcie", "encmsg_temp"]
sysdata = ["dosinfo_model", "dosinfo_user", "ota_size.txt", "ota_sv.txt", "sysver", "sysbat.py", "test.py", "userdir_par", "enctempfile"]

def clear_terminal():
    os.system('cls')

def sys_shutdown():
    global sys_pass
    global sys_on
    global breakall
    sys_pass = False
    sys_on = False
    breakall = True

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

def sys_pwseq():
    try:
        with open('dosinfo_user', 'r') as dosinfo:
            global dosinfo_user
            dosinfo_user = dosinfo.read()
            dosinfo.close()
    except FileNotFoundError:
        print("FATAL ERROR: Necessary components/files are absent. Initiating system restart...")
        time.sleep(2)
        return
    sys_pass = True
    global sys_on
    sys_on = False
    while sys_pass == True:
        for i in range(5):
            print(">Enter password.")
            pw = str(input("> "))
            pwcmd = pw.split()
            if i != 4:
                if pw in pw_store:
                    print(f">Password accepted. Welcome {dosinfo_user}.")
                    while True:
                        cmd = str(input("> "))
                        if cmd == "term:kernelntfc.tmx":
                            sys_load(1, "Fetching all necessary components... ")
                            time.sleep(1)
                            for remaining in range(-1, 101, 1):
                                sys.stdout.write("\r>Loading ntfc and inner tmx libraries... [{:.2f}%] ".format(remaining))
                                sys.stdout.flush()
                                time.sleep(0.01)
                            sys.stdout.write("\n")
                            sys.stdout.flush()
                            time.sleep(1)
                            for remaining in range(-1, 101, 1):
                                sys.stdout.write("\r>Loading enc/dnc libraries... [{:.2f}%] ".format(remaining))
                                sys.stdout.flush()
                                time.sleep(0.01)
                            sys.stdout.write("\n")
                            sys.stdout.flush()
                            sys_load(1, "Preparing syntax... ")
                            print("All operations executed successfully.")
                            while True:
                                cmd1 = str(input("> "))
                                if cmd1 == "term:uintfc.tmx":
                                    sys_pass = False
                                    sys_on = True
                                    return
                                else:
                                    print("Invalid command or parameters.")
                        else:
                            print("Invalid command or parameters.")
                elif len(pwcmd) == 0:
                    print(">Incorrect password. Please try again.")
                elif pwcmd[0] == "term:uintfc" and pwcmd[1] == "--std":
                    sys_load(4, "Terminating all processes... ")
                    print(">Shutting down COMMSDOS...")
                    sys_shutdown()
                    time.sleep(0.7)
                    sys_pass = False
                    global breakall
                    breakall = True
                    return
                elif pwcmd[0] == "term:uintfc" and pwcmd[1] == "--rst":
                    sys_load(4, "Terminating all processes and restaring... ")
                    clear_terminal()
                    time.sleep(1)
                    print("Copyright (C) The Koshvic Brothers Co. Ltd., 200X. All rights reserved")
                    print("This version of COMMSDOS is engineered specifically for ORTHOS Desktop Machines.")
                    print("Under the MCHJ COMMS Act VIII Part 1, states: Do not distribute this system anywhere else as it is a private property to the Marshall military and government.")
                    time.sleep(0.7)
                    print("\nLoading sysbat...")
                    time.sleep(3)
                    print("\n>COMMSDOS is currently in Safe Boot Mode.")
                else:
                    print(">Incorrect password. Please try again.")
            else:
                print(">You have attempted 5 incorrect password inputs.")
                for remaining in range(10, 0, -1):
                    sys.stdout.write("\r>System lock initiated. Try again in {:2d} seconds. ".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                sys.stdout.write("\n")
                sys.stdout.flush()
                i += 4

def sysHelp():
    print("""
    List of system commands:
    copyf <dir_paramater(src)> <filename> <dir_parameter>       Copies an existing file from its source directory to a new directory.
    dir                                                         Displays the available files and directory names in the root (system) directory.
    dir <directory_name (or) dir_parameter>                     Displays the available files names on the specified directory.
    dirpars                                                     Displays all the available directory parameters and its names.
    dnc                                                         Executes the Decryption module.
    enc                                                         Executes the Encryption module.
    exec <filename>                                             Executes a programme / software.
    globalprint <text>                                          Globally prints text from host user to other available users nearby.
    help                                                        Displays a list of system and kernel commands.
    localprint <text>                                           Prints text from user into the terminal locally.
    mkdir <dir_name> <dir_parameter>                            Creates a new directory with its specified call parameter.
    mkf <dir_parameter> <filename>                              Creates a new blank file in the specified directory.
    renf <dir_parameter> <current_filename> <new_filename>      Renames a file in a specified directory.
    rmdir <dir_name>                                            Removes a directory.
    rmf <dir_parameter> <filename>                              Removes a file in a specified directory.
    seq <.tmx_file>                                             Displays a terminal sequence from the system.
          
    List of add-on commands:
    [Koi - File Management]
    koi                                                         Checks the current Koi version and TTC status.
    koi dir <dir_parameter>                                     Displays the KoiDir table of the specified directory contents.
    koi -dcl                                                    Disables TTC.
        -ecl                                                    Enables TTC.
                   
    List of kernel commands:                        
    term:kernelntfc                                             System communicates to the kernel to change into DKA mode (Only available before entering DKA mode).
    term:uintfc --std                                           Terminates all system processes and shuts down.
                --rst                                           Terminates all system processes and restarts.
    term:kernelupd.pkg --ota                                    Installs the OTA update to the system kernel.
                       --ota -auto.rst:1                        Auto restarts system after installation to apply the OTA update instantly.
    """)

# Charcodes reference
latinalphas = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
)
charcodes = (
    '01', '02', '03', '04', '05', '11', '12', '13', '14', '15',
    '21', '22', '23', '24', '25', '31', '32', '33', '34', '35',
    '41', '42', '43', '44', '45', '51'
)
n2techarcodes = (
    '1a', '12', '13', '14', '2b', '26', '27', '28', '3c', '39',
    '31', '32', '4d', '43', '44', '45', '5e', '56', '57', '58',
    '6f', '69', '61', '62', '7g', '73'
)
s2techarcodes = (
    '4b', '16', '45', '89', '3a', '5e', '77', '6f', '74', '0a',
    '36', '0e', '90', '41', '1d', '7c', '14', '63', '22', '2f',
    '38', '34', '28', '19', '55', '4e'
)
marshallalphas = (
    '/:', ';)_', '(:\'' , '\';)', 'L:', '|\';', '(;\'', '|:', 'J:', '_|\'',
    '|;', '.||,', '|>;', '|^-', '(;;', '|^', '(;', '|>,', ',)(', '\'|=',
    'L;', '\\;', 'V;', '>:', './/"', '7;-'
)

def enc_seq():
    def encHelp(parameter):
        if parameter == "general":
            print("""
            List of enc commands and parameters:
            start       Start encryption sequence.
            scr -en     Enable terminal scrolling (CTRL+K to scroll upwards, CTRL+L to scroll downwards).
                -ds     Disable terminal scrolling.
            cn          Continue to ecnrypt another message.
            ch          Redirect to CHNNL selection (for sending another message to the same reciever).
            end         Ends encryption sequence.
            at -pr      Automatic search with LPC enabled (List Print Continuation, prints the list until the last available receiver upon pressing Enter).
                  
            General abbreviations:
            act         Allied Comms Tower
            ct          Companion Tablet
            act IP      Allied Comms Tower Identification Protocol
            ct ID       Companion Tablet Unique Identification
            at          Automatic Search          
            ml          Manual Search
            VDS         Vigor Decryption System Channel
            VDS-2       Vigor Decryption System version 2.0 Channel
            GDR         Graphical Decryption (Marshall Alphabet, MA) to Receiver Channel
            N2TE        Number Codes (MA) to Text Encryption Channel
            S2TE        Symbol Cyphers (MA) to Text Encryption Channel
            SPR         Send-Packet Rate (Total Hertz, Estimated Wattage)
            EHK         Encryption Hash Key
            RCVR        Receiver
            AT          Automatic Decryption
            """)
        elif parameter == "chars":
            print("""
            Character codes list:
            [Standard Latin]
                  
                   A     B     C     D     E     F     G     H     I     J
                  ch1   ch2   ch3   ch4   ch5   ch11  ch12  ch13  ch14  ch15

                   K     L     M     N     O     P     Q     R     S     T
                  ch21  ch22  ch23  ch24  ch25  ch31  ch32  ch33  ch34  ch35

                               U     V     W     X     Y     Z
                              ch41  ch42  ch43  ch44  ch45  ch51
                  
            [Marshall Alphabets][SY:N2TE, CS:S2TE]
                  
                   /:      ;)_     (:'     ';)     L:     |';     (;'     |:     J:     _|'
                  sy1a    sy12    sy13    sy14    sy2b   sy26    sy27    sy28   sy3c    sy39
                  cs4b    cs16    cs45    cs89    cs3a   cs5e    cs77    cs6f   cs74    cs0a

                   |;     .||,    |>;     |^-     (;;     |^      (;      |>,   ,)(     '|=
                  sy31    sy32    sy4d    sy43    sy44   sy45    sy5e    sy56   sy57    sy58
                  cs36    cs0e    cs90    cs41    cs1d   cs7c    cs14    cs63   cs22    cs2f

                                   L;      \\;      V;     >:     .//"     7;-
                                  sy6f    sy69    sy61   sy62    sy7g    sy73
                                  cs38    cs34    cs28   cs19    cs55    cs4e
            """)
        elif parameter == "chnnl":
            print("""
            Quick Reference to EC Channels (SPR is Per Character/Symbol):
                  
            VDS: "AXE" > ch1, ch44, ch5 >(EC)> 014505 ---(≥701 Hz, ~0.8W)---> RCVR >(AT)> "AXE"
                  
            VDS-2: "AXE" ---(EHK:01.44.05a , ≥700 Hz, ~0.05W)---> RCVR > "014405a"
                  
            GDR: "/:>:L:" ---(≥680 Hz, ~0.04W)---> RCVR > "/:>:L:"
                  
            N2TE: "/:>:L:" > sy1a, sy62, sy2b >(EC)> 1a622b01 ---(≥800 Hz, ~1.1W)---> RCVR >(AT)> "AXE"

            S2TE: "/:>:L:" ---(EHK:4b193a01 ≥790 Hz, ~1.8W)---> RCVR >(AT)> "AXE" 
            """)
    
    def chnnl_module(chnnl_slc, msg):
        if chnnl_slc == "VDS":
            msg_to_enc = str(msg).lower()
            conv_msg = list(msg_to_enc.lower())
            lenconv_msg = len(conv_msg)
            for i in range(lenconv_msg):
                if conv_msg[i] in latinalphas:
                    indexref = latinalphas.index(conv_msg[i])
                    conv_msg[i] = charcodes[indexref]
                else:
                    conv_msg[i] = " "
            
            prc1 = "".join(conv_msg)
            encrypted_msg = " ".join(prc1.split())

        elif chnnl_slc == "VDS-2":
            msg_to_enc = str(msg).lower()
            conv_msg = list(msg_to_enc.lower())
            lenconv_msg = len(conv_msg)
            for i in range(lenconv_msg):
                if conv_msg[i] in latinalphas:
                    indexref = latinalphas.index(conv_msg[i])
                    conv_msg[i] = charcodes[indexref]
                else:
                    conv_msg[i] = " "
            
            prc1 = "".join(conv_msg)
            encmsg0 = " ".join(prc1.split())
            split_encmsg0 = encmsg0.split()
            len_encmsg0 = len(split_encmsg0)
            final_encmsg = []
            for i in range(len_encmsg0):
                encmsg1bfr = list(split_encmsg0[i])
                if i+1 < 27:
                    encmsg1bfr.extend(latinalphas[i])
                    encmsg1 = "".join(encmsg1bfr)
                    final_encmsg.extend(encmsg1)
                elif i+1 < 53:
                    separator = latinalphas[i - 26] + latinalphas[i - 26]
                    encmsg1bfr.extend(separator)
                    encmsg1 = "".join(encmsg1bfr)
                    final_encmsg.extend(encmsg1)
                else:
                    final_encmsg = []
                    final_encmsg = ["Too many total sentences"]
                    
            encrypted_msg = "O1000B.43359a7262d783264f87237e898::" + "".join(final_encmsg)

        elif chnnl_slc == "GDR":
            msg_to_enc = str(msg).lower()
            conv_msg = list(msg_to_enc.lower())
            lenconv_msg = len(conv_msg)
            for i in range(lenconv_msg):
                if conv_msg[i] in latinalphas:
                    indexref = latinalphas.index(conv_msg[i])
                    conv_msg[i] = marshallalphas[indexref]
                else:
                    continue
            
            encrypted_msg = " ".join(conv_msg)

        elif chnnl_slc == "N2TE":
            msg_to_enc = str(msg).lower()
            conv_msg = list(msg_to_enc.lower())
            lenconv_msg = len(conv_msg)
            for i in range(lenconv_msg):
                if conv_msg[i] in latinalphas:
                    indexref = latinalphas.index(conv_msg[i])
                    conv_msg[i] = n2techarcodes[indexref]
                else:
                    conv_msg[i] = " "
            
            prc1 = "".join(conv_msg)
            encmsg0 = " ".join(prc1.split())
            split_encmsg0 = encmsg0.split()
            len_encmsg0 = len(split_encmsg0)
            final_encmsg = []
            for i in range(len_encmsg0):
                encmsg1bfr = list(split_encmsg0[i])
                if i+1 < 10:
                    encmsg1bfr.extend(str('0') + str(i+1))
                    encmsg2 = "".join(encmsg1bfr)
                    final_encmsg.extend(encmsg2)
                elif i+1 > 9 and i+1 < 100:
                    encmsg1bfr.extend(str(i+1))
                    encmsg2 = "".join(encmsg1bfr)
                    final_encmsg.extend(encmsg2)
                else:
                    final_encmsg = []
                    final_encmsg = ["Too many total sentences"]
            encrypted_msg = "".join(final_encmsg)

        elif chnnl_slc == "S2TE":
            msg_to_enc = str(msg).lower()
            conv_msg = list(msg_to_enc.lower())
            lenconv_msg = len(conv_msg)
            for i in range(lenconv_msg):
                if conv_msg[i] in latinalphas:
                    indexref = latinalphas.index(conv_msg[i])
                    conv_msg[i] = s2techarcodes[indexref]
                else:
                    conv_msg[i] = " "
            
            prc1 = "".join(conv_msg)
            encmsg0 = " ".join(prc1.split())
            conv_msg = list(msg_to_enc.lower())
            lenconv_msg = len(conv_msg)
            for i in range(lenconv_msg):
                if conv_msg[i] in latinalphas:
                    indexref = latinalphas.index(conv_msg[i])
                    conv_msg[i] = marshallalphas[indexref]
                else:
                    continue
            
            encmarshall = " ".join(conv_msg)
            split_encmsg0 = encmsg0.split()
            len_encmsg0 = len(split_encmsg0)
            final_encmsg = []
            for i in range(len_encmsg0):
                encmsg1bfr = list(split_encmsg0[i])
                if i+1 < 10:
                    encmsg1bfr.extend(str('0') + str(i+1))
                    encmsg2 = "".join(encmsg1bfr)
                    final_encmsg.extend(encmsg2)
                elif i+1 > 9 and i+1 < 100:
                    encmsg1bfr.extend(str(i+1))
                    encmsg2 = "".join(encmsg1bfr)
                    final_encmsg.extend(encmsg2)
                else:
                    final_encmsg = []
                    final_encmsg = ["Too many total sentences"]
            encrypted_msg = "O1000B.43359a7262d783264f87237e898::" + "".join(final_encmsg) + "\n" + encmarshall

        return encrypted_msg

    def enc_input():
        encinp = input("> ")
        global inpsplit
        inpsplit = encinp.split()

    while True:
        encmain = input("> ")
        encsplit = encmain.split()
        if encsplit[0] == "help":
            try:
                encHelp(encsplit[1])
            except IndexError:
                print(">Specify the type of help list (general/chars/chnnl). Eg. 'help general'")
        elif encsplit[0] == "start":
            seq2 = False
            while True:
                print(">Please choose the desired type of receiver.")
                enc_input()
                if inpsplit[0].lower() == "act":
                    rcvrtype = "act"
                    seq2 = True
                    seq2 = True
                    seq2a = False
                    seq3 = False
                    break
                elif inpsplit[0].lower() == "ct":
                    rcvrtype = "ct"
                    seq2 = True
                    seq2a = False
                    seq3 = False
                    break
                elif inpsplit[0].lower() == "end":
                    return
                else:
                    print(">Invalid command or parameters.")

            while seq2 == True:
                if rcvrtype == "act":
                    print(">Input the target ACT IP.")
                    enc_input()
                    if inpsplit[0] == "ac":
                        try:
                            dcolon_ins = inpsplit[1]
                            if inpsplit[0] == "ac" and dcolon_ins[0:2] == "::":
                                try:
                                    if inpsplit[2] != 0:
                                        print(">Valid command syntax: ac ::[ACT IP]")
                                        seq2a = False
                                except IndexError:
                                    actIP = inpsplit[1]
                                    seq2a = True
                            elif inpsplit[0] == "end":
                                return
                            else:
                                print(">Valid command syntax: ac ::[ACT IP]")
                                seq2a = False
                        except IndexError:
                            print(">Invalid command or parameters.")
                            seq2a = False
                    elif inpsplit[0] == "end":
                        return
                    else:
                        print(">Invalid command or parameters.")
                        seq2a = False

                    if seq2a == True:
                        try:
                            sys_load(3, "Fetching ACT information... ")
                            with open(f'act_ipfetch\\{actIP[2::]}', 'r') as actfile:
                                actinfo = actfile.readlines()
                                actfile.close()
                            timenow = datetime.datetime.today().strftime("%I:%M %p")
                            print(f">[ONLINE][{timenow}] {"".join(actinfo[0].split('\n'))}")
                            print(f" Accessible ports: {"".join(actinfo[1].split('\n'))}, {"".join(actinfo[2].split('\n'))}")
                            print(" Verify if this ACT is correct (Y/N)")
                            actverify = input("> ").lower()
                            if actverify == "y":
                                targetinfo = actinfo
                                target_name = "".join(targetinfo[0].split("\n"))
                                print(f">Target ACT: {target_name}")
                                seq2 = False
                                seq2a = False
                                seq3 = True
                                break
                            else:
                                sys_load(0.5, "Disconnecting from ACT host... ")
                        except FileNotFoundError:
                            print(">No ACT with matching IP found.")
                        except OSError:
                            print(">No ACT with matching IP found.")
                elif rcvrtype == "ct":
                    print(">CT selected. Please choose the desired device search method.")
                    enc_input()
                    if inpsplit[0].lower() == "ml":
                        print(">Input the target CT ID.")
                        enc_input()
                        if inpsplit[0] == "ct":
                            try:
                                dcolon_ins = inpsplit[1]
                                if inpsplit[0] == "ct" and dcolon_ins[0:2] == "::":
                                    try:
                                        if inpsplit[2] != 0:
                                            print(">Valid command syntax: ct ::[CT ID]")
                                            seq2a = False
                                    except IndexError:
                                        ctID = inpsplit[1]
                                        seq2a = True
                                else:
                                    print(">Valid command syntax: ct ::[CT ID]")
                                    seq2a = False
                            except IndexError:
                                print(">Invalid command or parameters.")
                                seq2a = False
                        elif inpsplit[0] == "end":
                            return
                        else:
                            print(">Invalid command or parameters.")
                            seq2a = False

                        if seq2a == True:
                            try:
                                sys_load(3, "Fetching CT information... ")
                                with open(f'ct_signalcatch\\{ctID[2::]}', 'r') as ctfile:
                                    ctinfo = ctfile.readlines()
                                    ctfile.close()
                                timenow = datetime.datetime.today().strftime("%I:%M %p")
                                print(f">[ONLINE][{timenow}] {"".join(ctinfo[0].split('\n'))}")
                                print(f" Accessible ports: {"".join(ctinfo[1].split('\n'))}, {"".join(ctinfo[2].split('\n'))}")
                                print(" Verify if this CT is correct (Y/N)")
                                ctverify = input("> ").lower()
                                if ctverify == "y":
                                    targetinfo = ctinfo
                                    target_name = "".join(targetinfo[1].split("\n"))
                                    print(f">Target CT: {target_name}")
                                    seq2 = False
                                    seq2a = False
                                    seq3 = True
                                    break
                                else:
                                    sys_load(0.5, "Disconnecting from CT host... ")
                            except FileNotFoundError:
                                print(">No CT with matching ID found.")
                            except OSError:
                                print(">No CT with matching ID found.")
                    elif inpsplit[0].lower() == "at":
                        sys_load(5, "Searching all nearby available CT's...")
                        path = 'C:/Users/user/Desktop/COMMSDOS/ct_signalcatch'
                        ct = []
                        for (dirpath, dirnames, filenames) in walk(path):
                            ct.extend(filenames)

                        len_ct = len(ct)
                        if len(ct) != 0:
                            ctnamelist = []
                            for i in range(len_ct):
                                ctidtemp = ct[i]
                                with open(f'ct_signalcatch\\{ctidtemp}', 'r') as ctf:
                                    ctinfo = ctf.readlines()
                                    ctf.close()

                                ctcatchtemp = []
                                ctcatchtemp.append(str(i+1))
                                ctcatchtemp.append(ctinfo[0].strip("\n"))
                                ctcatchtemp.append(ctidtemp)
                                ctnamelist.append(ctcatchtemp)
                        else:
                            ctnamelist = []
                        
                        if len(ct) != 0 and len(ctnamelist) != 0:
                            cttabledata = ctnamelist
                            cttableheader = ["No.", "Owner", "ID"]
                            print(tabulate(cttabledata, headers=cttableheader, tablefmt="heavy_outline"))
                            while True:
                                print(">Select the row no. of the target CT.")
                                enc_input()
                                if inpsplit[0].isdigit() == True:
                                    if int(inpsplit[0]) < (len(ctnamelist) + 1) and int(inpsplit[0]) > 0:
                                        targetinfo = ctnamelist[int(inpsplit[0]) - 1]
                                        target_ctid = targetinfo[2]
                                        target_name = targetinfo[1]
                                        with open(f'ct_signalcatch\\{target_ctid}', 'r') as ctfile:
                                            ctinfo = ctfile.readlines()
                                            ctfile.close()
                                        timenow = datetime.datetime.today().strftime("%I:%M %p")
                                        print(f">[ONLINE][{timenow}] {target_name}")
                                        print(f" Accessible ports: {"".join(ctinfo[1].split('\n'))}, {"".join(ctinfo[2].split('\n'))}")
                                        print(" Verify if this CT is correct (Y/N)")
                                        ctverify = input("> ").lower()
                                        if ctverify == "y":
                                            print(f">Target CT: {target_name}")
                                            seq2 = False
                                            seq2a = False
                                            seq3 = True
                                            break
                                        else:
                                            sys_load(0.5, "Disconnecting from CT host... ")
                                    else:
                                        print(">Row no. out of range.")
                                else:
                                    print(">Input row no. as integers only.")
                        else:
                            print("No nearby CT's detected.")
                    elif inpsplit[0].lower() == "end":
                        return

            seq3a = False
            while seq3 == True:
                print(">Select EC channel by rotating the CHNNL knob or type it in:")
                enc_input()
                if inpsplit[0].upper() == "VDS":
                    chnnl = "VDS"
                    seq3a = True
                elif inpsplit[0].upper() == "VDS-2":
                    chnnl = "VDS-2"
                    seq3a = True
                elif inpsplit[0].upper() == "GDR":
                    chnnl = "GDR"
                    seq3a = True
                elif inpsplit[0].upper() == "N2TE":
                    chnnl = "N2TE"
                    seq3a = True
                elif inpsplit[0].upper() == "S2TE":
                    chnnl = "S2TE"
                    seq3a = True
                elif inpsplit[0] == "help":
                    try:
                        encHelp(inpsplit[1])
                    except IndexError:
                        print(">Specify the type of help list (general/chars/chnnl). Eg. 'help general'")
                elif inpsplit[0] == "end":
                    if target_name[0:3] == "ACT":
                        sys_load(2, "Disconnecting from ACT host... ")
                    else:
                        sys_load(2, "Disconnecting from CT host... ")
                    return
                else:
                    print(">Invalid selection of EC channel. Type 'help <chars/chnnl>' for EC lists and references, or 'end' to end enc session.")

                while seq3a == True:
                    print(f">EC Channel: {chnnl}")
                    print(">Message here:")
                    enc_msg = input("> ")
                    print(">Confirm message before sending to host (Y/N/C)")
                    msgverify = input("> ").upper()
                    if msgverify == "Y":
                        enc_res = chnnl_module(chnnl, enc_msg)
                        if enc_res == "Too many total sentences":
                            print(">Too many total sentences (>52).")
                            print(f">Last saved message:\n{enc_msg}")
                        else:
                            sys_load(3, "Encrypting text... ")
                            chnnllistref = ['VDS', 'VDS-2', 'GDR', 'N2TE', 'S2TE']
                            chnnlindex = chnnllistref.index(chnnl)
                            timenow = datetime.datetime.today().strftime("%I:%M %p")
                            datenow = datetime.date.today().strftime("%d-%m-%Y")
                            try:
                                with open('encmsg_temp\\enctempfile', 'r') as enctempfile:
                                    tokens = enctempfile.read()
                                    tokens = tokens.split()
                                    enc_no = len(tokens)
                                    enctempfile.close()
                                with open(f"encmsg_temp\\enc{enc_no}{datenow}", 'w') as enctemp:
                                    enctemp.write(f"[899550][{datenow}][{timenow}][{chnnlindex + 1}]")
                                    enctemp.write(f"{enc_res}")
                                    enctemp.close()
                                with open('encmsg_temp\\enctempfile', 'a') as enctempfile:
                                    enctempfile.write(f"[enctoken{randint(1000000000,9999999999)}]\n")
                                    enctempfile.close()
                            except FileNotFoundError:
                                print("FATAL ERROR: [F406] ENC module files missing. Please contact system administrators immediately.")
                                return
                            sys_load(1, "Contacting with host... ")
                            sys_load(3, "Sending EC message to host.. ")
                            print(">Session completed successfully.")
                            return
                    elif msgverify == "C":
                        print(f">Last saved message:\n{enc_msg}")
                        seq3a = False
                        break
                    else:
                        print(f">Last saved message:\n{enc_msg}")
                        
        elif encsplit[0] == "end":
            return
        
def dnc_seq():
    def dnc_input():
        dncinp = input("> ")
        global inpsplit
        inpsplit = dncinp.split()

    with open('dnc_logs\\commslist', 'r') as cl:
        commslist0 = cl.readlines()
        commslist = []
        for i in range(len(commslist0)):
            tempclist = commslist0[i].strip('\n')
            if tempclist == "commslist":
                continue
            else:
                commslist.append(tempclist)
        cl.close()

    def dnclogs():
        path = 'C:/Users/user/Desktop/COMMSDOS/dnc_logs'
        logs = []
        for (dirpath, dirnames, filenames) in walk(path):
            logs.extend(filenames)

        logs.remove('commslist')
        logs.remove('dncftemp')
        global len_logs
        len_logs = len(logs)
        if len_logs != 0:
            global logsdata
            logsdata = []
            for i in range(len_logs):
                logfile = logs[i]
                if logfile[0:3] == "log":
                    with open(f'dnc_logs\\{logfile}', 'r') as lf:
                        commslogid0 = lf.read(7).strip('[')
                        commslogid = commslogid0.strip('\n')
                        lf.close()
                    namereftemp = commslist.index(commslogid) + 1
                    logcatchtemp = []
                    logcatchtemp.append(str(i+1))
                    logcatchtemp.append(logfile)
                    logcatchtemp.append(commslist[namereftemp])
                    logsdata.append(logcatchtemp)
                elif logfile[0:3] == "dnc":
                    with open(f'dnc_logs\\{logfile}', 'r') as lf:
                        commslogid0 = lf.read(14).strip('>[')
                        commslogid = commslogid0.strip('\n')
                        lf.close()
                    logcatchtemp = []
                    logcatchtemp.append(str(i+1))
                    logcatchtemp.append(logfile)
                    logcatchtemp.append(commslogid)
                    logsdata.append(logcatchtemp)
        else:
            print(">No dnc logs found.")
            return

    dnclogs()    
    if len_logs != 0:
        datenow = datetime.date.today().strftime("%d-%m-%Y")
        logslistheader = ["No.", "Logs", "Source"]
        print(tabulate(logsdata, headers=logslistheader, tablefmt="heavy_outline"))
        while True:
            print(">Enter command")
            dnc_input()
            if inpsplit[0] == "end":
                #return
                break #delete this when adding the dnc module
            elif inpsplit[0] == "read":
                try:
                    if int(inpsplit[1]) > 0 and int(inpsplit[1]) < len(logsdata) + 1:
                        #sys_load(2, "Gathering text data...")
                        targetlog0 = logsdata[int(inpsplit[1]) - 1]
                        targetlog = targetlog0[1]
                        if targetlog[0:3] == "log":
                            with open(f'dnc_logs\\{targetlog}') as logf:
                                targetlogdata = logf.read()
                                logf.close()
                            if str(targetlogdata[31:32]) == '1':
                                #sys_load(5, "Auto-decrypting...")
                                #sys_load(1, "Preparing to display message log...")
                                #print(targetlogdata[33::])
                                enc_text = targetlogdata[33::]
                                sprtext = list(enc_text)
                                dnc_text = []
                                j = 0
                                for i in range(len(sprtext)):
                                    try:
                                        if sprtext[(i+j)] != " ":
                                            char_replc = str(sprtext[(i+j)]) + str(sprtext[(i+j+1)])
                                            char_indexref = charcodes.index(char_replc)
                                            alpha_replc = latinalphas[char_indexref]
                                            dnc_text.extend(alpha_replc)
                                            j += 1
                                        else:
                                            dnc_text.extend(" ")
                                    except IndexError:
                                        break
                                logdatetime = targetlogdata[8:30]
                                print(f">[{targetlog0[2]}]{logdatetime}:")
                                print(" "+"".join(dnc_text))
                            elif str(targetlogdata[31:32]) == '2':
                                #sys_load(1, "Preparing to display message log...")
                                logdatetime = targetlogdata[8:30]
                                print(f">[{targetlog0[2]}]{logdatetime}:")
                                print(" "+targetlogdata[69::])
                            elif str(targetlogdata[31:32]) == '3':
                                #sys_load(1, "Preparing to display message log...")
                                logdatetime = targetlogdata[8:30]
                                print(f">[{targetlog0[2]}]{logdatetime}:")
                                print(" "+targetlogdata[33::])
                            elif str(targetlogdata[31:32]) == '4':
                                print(">Display alongside the original encrypted text? (Y/N)")
                                verf_dpenc = input("> ").upper()
                                if verf_dpenc == "Y":
                                    dpenctext = True
                                else:
                                    dpenctext = False
                                #sys_load(5, "Auto-decrypting...")
                                #sys_load(1, "Preparing to display message log...")
                                enc_text = targetlogdata[33::]
                                sprtext = list(enc_text)
                                dnc_text = []
                                j = 0
                                for i in range(len(sprtext)):
                                    try:
                                        char_replc = str(sprtext[(i+j)]) + str(sprtext[(i+j+1)])
                                        char_indexref = n2techarcodes.index(char_replc)
                                        alpha_replc = latinalphas[char_indexref]
                                        dnc_text.extend(alpha_replc)
                                        j += 1
                                    except IndexError:
                                        break
                                    except ValueError:
                                        dnc_text.extend(" ")
                                        j += 1
                                logdatetime = targetlogdata[8:30]
                                print(f">[{targetlog0[2]}]{logdatetime}:")
                                print(" "+"".join(dnc_text))
                                if dpenctext == True:
                                    print(">Original encrypted text:")
                                    print(" "+targetlogdata[33::])
                            elif str(targetlogdata[31:32]) == '5':
                                with open(f'dnc_logs\\{targetlog}') as logf:
                                    targetlogdata = logf.readlines()
                                    logf.close()
                                print(">Display alongside the original encrypted text? (Y/N)")
                                verf_dpenc = input("> ").upper()
                                if verf_dpenc == "Y":
                                    dpenctext = True
                                else:
                                    dpenctext = False
                                #sys_load(5, "Auto-decrypting...")
                                #sys_load(1, "Preparing to display message log...")
                                enc_text0 = "".join(targetlogdata[0].split('\n'))
                                enc_text = enc_text0[69::]
                                sprtext = list(enc_text)
                                dnc_text = []
                                j = 0
                                for i in range(len(sprtext)):
                                    try:
                                        char_replc = str(sprtext[(i+j)]) + str(sprtext[(i+j+1)])
                                        char_indexref = s2techarcodes.index(char_replc)
                                        alpha_replc = latinalphas[char_indexref]
                                        dnc_text.extend(alpha_replc)
                                        j += 1
                                    except IndexError:
                                        break
                                    except ValueError:
                                        dnc_text.extend(" ")
                                        j += 1
                                logdatetime = enc_text0[8:30]
                                print(f">[{targetlog0[2]}]{logdatetime}:")
                                print(" "+"".join(dnc_text))
                                if dpenctext == True:
                                    print(">Original encrypted text:")
                                    print(" "+"".join(targetlogdata)[69::])
                        elif targetlog[0:3] == "dnc":
                            with open(f'dnc_logs\\{targetlog}', 'r') as logf:
                                dnctextdata = logf.read()
                                logf.close()
                            print(dnctextdata)
                    else:
                        print(">Row no. out of range.")
                except IndexError:
                    print(">Invalid command parameter. Specify the row no. of the target log.")
                except ValueError:
                    print(">Invalid command parameter. Input integers only.")
            elif inpsplit[0] == "dnclog":
                try:
                    if int(inpsplit[1]) > 0 and int(inpsplit[1]) < len(logsdata) + 1:
                        #sys_load(2, "Gathering text data...")
                        targetlog0 = logsdata[int(inpsplit[1]) - 1]
                        targetlog = targetlog0[1]
                        if targetlog[0:3] == "log":
                            with open(f'dnc_logs\\{targetlog}') as logf:
                                targetlogdata = logf.read()
                                logf.close()
                            if str(targetlogdata[31:32]) == '2':
                                enc_text = targetlogdata[69::]
                                sprtext = list(enc_text)
                                dnc_text = []
                                j = 0
                                for i in range(len(sprtext)):
                                    try:
                                        if sprtext[(i+j)].isdigit() == True:
                                            char_replc = str(sprtext[(i+j)]) + str(sprtext[(i+j+1)])
                                            char_indexref = charcodes.index(char_replc)
                                            alpha_replc = latinalphas[char_indexref]
                                            dnc_text.extend(alpha_replc)
                                            j += 1
                                        elif sprtext[(i+j)].isdigit() == False and sprtext[(i+j+1)].isdigit() == False:
                                            dnc_text.extend(" ")
                                            j += 1
                                        else:
                                            dnc_text.extend(" ")
                                    except IndexError:
                                        break
                                logdatetime = targetlogdata[8:30]
                                with open('dnc_logs\\dncftemp', 'r') as tokentemp:
                                    counttoken = tokentemp.readlines()
                                    no = len(counttoken) + 1
                                    tokentemp.close()
                                with open(f'dnc_logs\\dnc{no}{datenow}', 'w') as dncf:
                                    dncf.write(f">[{targetlog0[2]}]{logdatetime}:\n")
                                    dncf.write(" "+"".join(dnc_text))
                                    dncf.close()
                                with open('dnc_logs\\dncftemp', 'a') as tokentemp:
                                    tokentemp.write(f'[dnctemptoken{randint(1000000000,9999999999)}]\n')
                                    tokentemp.close()
                                #sys_load(2, "Decrypting VDS-2 text data from log file...")
                                print(f'>Session completed. A new file has created titled \'dnc{no}{datenow}\'')
                                dnclogs()
                                print(tabulate(logsdata, headers=logslistheader, tablefmt="heavy_outline"))
                            elif str(targetlogdata[31:32]) == '3':
                                with open(f'dnc_logs\\{targetlog}', 'r') as logf:
                                    logtextdata = logf.read()
                                    logf.close()
                                textdatasplit = logtextdata[33::].split()
                                dnc_text = []
                                for i in range(len(textdatasplit)):
                                    if textdatasplit[i] in marshallalphas:
                                        marshallindexref = marshallalphas.index(textdatasplit[i])
                                        textdatasplit[i] = latinalphas[marshallindexref]
                                        dnc_text.extend(textdatasplit[i])
                                    else:
                                        dnc_text.extend(textdatasplit[i])
                                logdatetime = targetlogdata[8:30]
                                with open('dnc_logs\\dncftemp', 'r') as tokentemp:
                                    counttoken = tokentemp.readlines()
                                    no = len(counttoken) + 1
                                    tokentemp.close()
                                with open(f'dnc_logs\\dnc{no}{datenow}', 'w') as dncf:
                                    dncf.write(f">[{targetlog0[2]}]{logdatetime}:\n")
                                    dncf.write(" "+" ".join(dnc_text))
                                    dncf.close()
                                with open('dnc_logs\\dncftemp', 'a') as tokentemp:
                                    tokentemp.write(f'[dnctemptoken{randint(1000000000,9999999999)}]\n')
                                    tokentemp.close()
                                #sys_load(2, "Decrypting GDR text data from log file...")
                                print(f'>Session completed. A new file has created titled \'dnc{no}{datenow}\'')
                                dnclogs()
                                print(tabulate(logsdata, headers=logslistheader, tablefmt="heavy_outline"))
                            else:
                                print(">The log text data is not in VDS-2 or GDR EC format.")
                        else:
                            print(">Can only decrypt files where the filename starts with \'log\'.")
                    else:
                        print(">Row no. out of range.")
                except IndexError:
                    print(">Invalid command parameter. Specify the row no. of the target log.")
                except ValueError:
                    print(">Invalid command parameter. Input integers only.")
            else:
                print(">Invalid command.")
    else:
        print(">No dnc logs found.")
        #return

breakall = False
while breakall == False:
    try:
        with open('dosinfo_user', 'r') as dosinfo:
            global dosinfo_user
            dosinfo_user = dosinfo.read()
            dosinfo.close()
    except FileNotFoundError:
        print("FATAL ERROR: Necessary components/files are absent. Initiating system restart...")
        time.sleep(2)
        break
    sys_on = True

    while sys_on == True:
        clear_terminal()
        time.sleep(1)
        try:
            with open('dosinfo_model', 'r') as dosinfo:
                dosinfo_model = dosinfo.read()
                dosinfo.close()
            
            with open('sysver', 'r') as sysver_fileOpen:
                sysver = sysver_fileOpen.read()
                sysver_fileOpen.close()

            with open("userdir_par", "r") as pars:
                parslist = pars.read().splitlines()
                pars.close()

            with open('ota_sv.txt', 'r') as ota:
                ota_ver = ota.readline()
                ota.close()

            with open('cmdaddons', 'r') as addon:
                cmdaddons = addon.read().splitlines()
                addon.close()

            if ota_ver == sysver:
                ota_upd = "No OTA updates available."
            else:
                with open('ota_size.txt', 'r') as ota:
                    ota_size = ota.readline()
                    ota.close()
                ota_upd = f"New OTA update available: COMMSDOS Version {ota_ver} [{ota_size}]"
            
            timenow = datetime.datetime.today().strftime("%I:%M %p")
            datenow = datetime.date.today().strftime("%d-%m-%Y")
            print(f">Welcome {dosinfo_user} - {timenow}, {datenow}")
            print(f">Current COMMSDOS Version: {sysver}")
            print(f" {dosinfo_model}, Manufactured by The Koshvic Brothers Co.")
            print(f" {ota_upd}")
            print("\n\n")
            
            while True:
                cmdmain = str(input("> "))
                cmdsplit = cmdmain.split()

                try:
                    if cmdsplit[0] == "exec":
                        try:
                            try:
                                with open(f"floppy_disks/{cmdsplit[1]}", "r") as f:
                                    sys_load(2, f"Launching {cmdsplit[1]}... ")
                                    code = f.read()
                                    exec(code)
                            except UnicodeDecodeError:
                                with open(f"floppy_disks/{cmdsplit[1]}", "r", encoding='utf-8') as f:
                                    code = f.read()
                                    exec(code)
                            input(">Press enter to continue to system...")
                            clear_terminal()
                            break
                        except IndexError:
                            print(">Error. File not found.")
                        except FileNotFoundError:
                            try:
                                with open(f"dos_storage_dir/{cmdsplit[1]}", "r") as f:
                                    sys_load(2, f"Launching {cmdsplit[1]}... ")
                                    code = f.read()
                                    exec(code)
                                    input(">Press enter to continue to system...")
                                    clear_terminal()
                                    break
                            except UnicodeDecodeError:
                                with open(f"dos_storage_dir/{cmdsplit[1]}", "r", encoding='utf-8') as f:
                                    code = f.read()
                                    exec(code)
                                    input(">Press enter to continue to system...")
                                    clear_terminal()
                                    break
                            except FileNotFoundError:
                                print(">Error. File not found.")
                    elif cmdsplit[0] == "help":
                        sysHelp()
                    elif cmdsplit[0] == "enc":
                        enc_seq()
                    elif cmdsplit[0] == "dnc":
                        dnc_seq()
                    elif cmdsplit[0] == "seq" and cmdsplit[1] == "logo_ascii.tmx":
                        clear_terminal()
                        print(logo_ascii)
                        time.sleep(4)
                        break
                    elif cmdsplit[0] == "seq" and cmdsplit[1] == "disclaimer.tmx":
                        clear_terminal()
                        print("Copyright (C) The Koshvic Brothers Co. Ltd., 200X. All rights reserved")
                        print("This version of COMMSDOS is engineered specifically for ORTHOS Desktop Machines.")
                        print("Under the MCHJ COMMS Act VIII Part 1, states: Do not distribute this system anywhere else as it is a private property to the Marshall military and government.")
                        input("\n>Press 'Enter' to continue...")
                        clear_terminal()
                        break
                    elif cmdsplit[0] == "term:uintfc.tmx" and cmdsplit[1] == "--std":
                        sys_load(4, "Terminating all processes... ")
                        print(">Shutting down COMMSDOS...")
                        time.sleep(2)
                        clear_terminal()
                        sys_shutdown()
                        break
                    elif cmdsplit[0] == "term:uintfc.tmx" and cmdsplit[1] == "--rst":
                        sys_load(4, "Terminating all processes and restarting... ")
                        clear_terminal()
                        time.sleep(0.9)
                        print(logo_ascii)
                        time.sleep(3)
                        break
                    elif cmdsplit[0] == "term:kernelupd.pkg" and cmdsplit[1] == "--ota":
                        updsuccess = False
                        invalidupdpar = False
                        autorst = False
                        try:
                            if cmdsplit[2] == "-auto.rst:1":
                                autorst = True
                            else:
                                invalidupdpar = True
                        except IndexError:
                            autorst = False
                        if invalidupdpar == True:
                            print(">Invalid command or parameters.")
                        elif ota_upd == "No OTA updates available.":
                            print(">No new OTA updates avaialable for the system kernel.")
                        else:
                            sys_load(7, "Fetching OTA update from server host... ")
                            time.sleep(0.9)
                            for remaining in range(0, 101, 1):
                                sys.stdout.write("\r>Downloading OTA update from server host... [{:.2f}%] ".format(remaining))
                                sys.stdout.flush()
                                time.sleep(0.2)
                            sys.stdout.write("\n")
                            sys.stdout.flush()
                            for remaining in range(0, 101, 1):
                                sys.stdout.write("\r>Installing update to system kernel... [{:.2f}%] ".format(remaining))
                                sys.stdout.flush()
                                time.sleep(0.1)
                            sys.stdout.write("\n")
                            sys.stdout.flush()
                            with open('ota_sv.txt', 'r') as otaupd:
                                updver = otaupd.read()
                                otaupd.close()
                            with open('sysver', 'w') as sysverfile:
                                sysverfile.write(updver)
                                sysverfile.close()
                            updsuccess = True
                        if autorst == True and updsuccess == True:
                            sys_load(4, "Terminating all processes and restarting... ")
                            clear_terminal()
                            time.sleep(0.9)
                            print(logo_ascii)
                            time.sleep(3)
                            break
                        elif autorst == False and updsuccess == True:
                            ota_upd = "No OTA updates available."
                            print(">Kernel update installed successfully. Restart the system to complete and apply all changes.")
                    elif cmdsplit[0] == "dir":
                        try:
                            testdir = cmdsplit[1][0:1]
                            testdir = True
                        except IndexError:
                            testdir = False
                        
                        if testdir == True:
                            try:
                                if cmdsplit[1][0:1] == "-":
                                    dirnameindex = parslist.index(cmdsplit[1]) + 1
                                    dirname = parslist[dirnameindex].strip("\n")
                                    path = f'C:/Users/user/Desktop/COMMSDOS/{dirname}'
                                    dirparslc = True
                                else:
                                    dirparslc = False

                                if dirparslc == True:
                                    path = f'C:/Users/user/Desktop/COMMSDOS/{dirname}'
                                elif dirparslc == False:
                                    dirname = cmdsplit[1]
                                    path = f'C:/Users/user/Desktop/COMMSDOS/{dirname}'
                                d = []
                                f = []
                                for (dirpath, dirnames, filenames) in walk(path):
                                    d.extend(dirnames)
                                    f.extend(filenames)
                                    break
                                if len(f) != 0:
                                    print("List of contents from: orthos1000b/"+dirname+"\n\n" + "   <<dir>>\n".join(d), end="   <<dir>>\n" + "\n".join(f) + "\n")
                                else:
                                    print("Path does not exist or no files detected.")
                            except ValueError:
                                print(f">Directory parameter '{cmdsplit[1]}' does not exist.")
                        else:
                            path = 'C:/Users/user//Desktop/COMMSDOS'
                            d = []
                            f = []
                            for (dirpath, dirnames, filenames) in walk(path):
                                d.extend(dirnames)
                                f.extend(filenames)
                                break
                            if len(f) != 0:
                                print("List of contents from: orthos1000b/root\n\n" + "   <<dir>>\n".join(d), end="   <<dir>>\n" + "\n".join(f) + "\n")
                    elif cmdsplit[0] == "localprint":
                        cmdsplit.pop(0)
                        print(">"+" ".join(cmdsplit))
                    elif cmdsplit[0] == "globalprint":
                        sys_load(4, "Printing message to all available CT's... ")
                        cmdsplit.pop(0)
                        print(">[CT-MC0305-DELTA]["+timenow+"]: "+" ".join(cmdsplit))
                    elif cmdsplit[0] == "mkdir":
                        try:
                            dirname = cmdsplit[1]
                            setpar = cmdsplit[2]
                            if setpar in parslist and dirname in parslist:
                                print(f">Directory '{dirname}' already exists with its parameter set to '{setpar}'")
                            elif setpar in parslist:
                                print(f">Parameter '{setpar}' already exists.")
                            elif dirname in parslist:
                                print(f">Directory '{dirname}' already exists.")
                            else:
                                terminalinp(f'mkdir {dirname}')
                                if termsuccess == True:
                                    with open("userdir_par", "a") as f:
                                        f.write(setpar + "\n")
                                        f.write(dirname + "\n")
                                        f.close()
                                    with open("userdir_par", "r") as pars:
                                        parslist = []
                                        parslist = pars.read().splitlines()
                                        pars.close()
                                    print(f">Created directory '{dirname}' with parameter set to '{setpar}'.")
                        except IndexError:
                            print(">Invalid command or parameters.")
                    elif cmdsplit[0] == "rmf":
                        try:
                            dirpar = cmdsplit[1]
                            filename = cmdsplit[2]
                            dirnameindex = parslist.index(dirpar) + 1
                            dirname = parslist[dirnameindex].strip("\n")
                            try:
                                ftest = open(filename, "r")
                                ftest.close()
                                if filename in sysdata:
                                    print(">Cannot delete system files.")
                                else:
                                    terminalinp(f'del /f C:\\Users\\user\\Desktop\\COMMSDOS\\{dirname}\\{filename}')
                                    if termsuccess == True:
                                        print(">File deleted successfully.")
                            except FileNotFoundError:
                                try:
                                    ftest = open(f'{dirname}\\{filename}', "r")
                                    ftest.close()
                                    if filename in sysdata:
                                        print(">Cannot delete system files.")
                                    else:
                                        terminalinp(f'del /f C:\\Users\\user\\Desktop\\COMMSDOS\\{dirname}\\{filename}')
                                        if termsuccess == True:
                                            print(">File deleted successfully.")
                                except FileNotFoundError:
                                    print(f">File '{filename}' not found.")
                        except IndexError:
                            print(">Invalid command or parameters.")
                        except ValueError:
                            print(f">Directory parameter '{dirpar}' does not exist.")
                    elif cmdsplit[0] == "rmdir":
                        try:
                            dirname = cmdsplit[1]
                            try:
                                dirparindex = parslist.index(dirname) - 1
                                dirpar = parslist[dirparindex]
                                if dirname in sysdir:
                                    print(">Cannot delete system directories.")
                                else:
                                    terminalinp(f'rmdir /s /q C:\\Users\\user\\Desktop\\COMMSDOS\\{dirname}')
                                    if termsuccess == True:
                                        with open('userdir_par', 'r') as f1:
                                            lines = f1.readlines()
                                        with open('userdir_par', 'w') as f2:
                                            for line in lines:
                                                if line.strip('\n') != dirname:
                                                    f2.write(line)
                                        with open('userdir_par', 'r') as f3:
                                            lines = f3.readlines()
                                        with open('userdir_par', 'w') as f4:
                                            for line in lines:
                                                if line.strip('\n') != dirpar:
                                                    f4.write(line)
                                        with open("userdir_par", "r") as pars:
                                            parslist = []
                                            parslist = pars.read().splitlines()
                                            pars.close()
                                        f1.close()
                                        f2.close()
                                        f3.close()
                                        f4.close()
                                        print(">Directory deleted successfully.")
                            except ValueError:
                                print(">Directory does not exist.")
                        except IndexError:
                            print(">Invalid command or parameters.")
                    elif cmdsplit[0] == "renf":
                        try:
                            dirpar = cmdsplit[1]
                            oldfname = cmdsplit[2]
                            newfname = cmdsplit[3]
                            try:
                                dirnameindex = parslist.index(dirpar) + 1
                                dirname = parslist[dirnameindex].strip("\n")
                                try:
                                    ftest = open(f'{dirname}\\{oldfname}', "r")
                                    ftest.close()
                                    if oldfname in sysdata:
                                        print(">Cannot rename system files.")
                                    else:
                                        terminalinp(f'cd C:\\Users\\user\\Desktop\\COMMSDOS\\{dirname} & ren {oldfname} {newfname}')
                                        if termsuccess == True:
                                            print(f">File '{oldfname}' has been changed to '{newfname}'.")
                                except FileNotFoundError:
                                    print(f">File '{oldfname}' not found.")
                            except ValueError:
                                print(f">Directory parameter '{dirpar}' does not exist.")
                        except IndexError:
                            print(">Invalid command or parameters.")
                    elif cmdsplit[0] == "dirpars":
                        with open('userdir_par', 'r') as f:
                            dirparslist = f.read()
                            f.close()
                        print(">Directory parameters list (1st line with '-': dir parameter, 2nd line: dir name)")
                        print(dirparslist)
                    elif cmdsplit[0] == "copyf":
                        try:
                            dirsrc = cmdsplit[1]
                            fname = cmdsplit[2]
                            dirdsn = cmdsplit[3]
                            try:
                                dirnameindex = parslist.index(dirsrc) + 1
                                dirsrcname = parslist[dirnameindex].strip("\n")
                                try:
                                    dirnameindex = parslist.index(dirdsn) + 1
                                    dirdsnname = parslist[dirnameindex].strip("\n")
                                    try:
                                        ftest = open(f'{dirsrcname}\\{fname}', "r")
                                        ftest.close()
                                        try:
                                            ftest = open(f'{dirdsnname}\\{fname}', "r")
                                            ftest.close()
                                            print(f">File '{fname}' already exists in directory '{dirdsnname}'.")
                                        except FileNotFoundError:
                                            terminalinp(f'copy C:\\Users\\user\\Desktop\\COMMSDOS\\{dirsrcname}\\{fname} C:\\Users\\user\\Desktop\\COMMSDOS\\{dirdsnname}\\')
                                            if termsuccess == True:
                                                print(f">File '{fname}' has been copied to directory '{dirdsnname}'.")
                                    except FileNotFoundError:
                                        print(f">File '{fname}' not found.")
                                except ValueError:
                                    print(f">Directory parameter '{dirdsn}' does not exist.")
                            except ValueError:
                                print(f">Directory parameter '{dirsrc}' does not exist.")
                        except IndexError:
                            print(">Invalid command or parameters.")
                    elif cmdsplit[0] == "mkf":
                        try:
                            dirpar = cmdsplit[1]
                            fname = cmdsplit[2]
                            try:
                                dirnameindex = parslist.index(dirpar) + 1
                                dirname = parslist[dirnameindex].strip("\n")
                                try:
                                    ftest = open(f'{dirname}\\{fname}', "r")
                                    ftest.close()
                                    print(f">File '{fname}' already exists in directory '{dirname}'.")
                                except FileNotFoundError:
                                    with open(f'{dirname}\\{fname}', 'w') as newf:
                                        newf.write("")
                                        newf.close()
                                    print(f">File '{fname}' has been created in directory '{dirname}'.")
                            except ValueError:
                                print(f">Directory parameter '{dirpar}' does not exist.")
                        except IndexError:
                            print(">Invalid command or parameters.")
                    elif cmdsplit[0] in cmdaddons:
                        #addpoint
                        if cmdsplit[0] == 'koi':
                            try:
                                extras.koi(cmdsplit[1], cmdsplit[2], cmdsplit[3])
                            except IndexError:
                                try:
                                    extras.koi(cmdsplit[1], cmdsplit[2])
                                except IndexError:
                                    try:
                                        extras.koi(cmdsplit[1])
                                    except IndexError:
                                        extras.koi()
                    else:
                        print(">Invalid command or parameters.")
                except IndexError:
                    print(">Invalid command or parameters.")

        except FileNotFoundError:
            print("FATAL ERROR: [F401] Necessary components/files are absent. Please contact system administrators immediately.")
            input("Press ENTER to initiate system restart.")
            break

if sys_on == False and breakall == True:
    os.system('exit')
else:
    print("FATAL ERROR: [F401] Necessary components/files are absent. Please contact system administrators immediately.")
    input("> ")
