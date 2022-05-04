import os
import time


stdfile = ['[CN]', 'adjust=0']

cheatfile = ['[CN]', 'i1=9', 'i2=9', 'i3=9', 'i4=9', 'adjust=0', 'hs=10600', 'ep=0', 'ch0=1', 'ch1=1', 'ch2=1', 'ch3=1', 'ch4=1', 'ch5=1', 'ch6=1', 'ch7=1', 'ch8=1', 'ch9=1', 'ch10=1', 'ch11=1', 'ch12=1', 'ch13=1', 'ch14=1', 'ch15=1', 'ch16=1', 'bestminutes=4', 'besttens=3', 'bestseconds=0', 'besttenths=0']


def reset_file():
    file = open(os.getenv("AppData") + "/MMFApplications/CN", "w")
    for item in stdfile:
        file.write(item + "\n")
    file.close()

def cheat_file():
    file = open(os.getenv("AppData") + "/MMFApplications/CN", "w")
    for item in cheatfile:
        file.write(item + "\n")
    file.close()

def create_backup(backup_name: str):
    origfile = open(os.getenv("AppData") + "/MMFApplications/CN", "r")
    backupfile = open("Backups/" + backup_name, "w")
    origcontent = origfile.read().splitlines()
    for item in origcontent:
        backupfile.write(item + "\n")
    origfile.close()
    backupfile.close()

def load_backup(backup_name: str):
    origfile = open(os.getenv("AppData") + "/MMFApplications/CN", "w")
    backupfile = open("Backups/" + backup_name, "r")
    backupcontent = backupfile.read().splitlines()
    for item in backupcontent:
        origfile.write(item + "\n")
    origfile.close()
    backupfile.close()

def exit():
    print("Exiting..")
    time.sleep(1)
    quit()

def command():
    cmd = input("Enter Command (Type 'help' to show help): ")
    if cmd == "help":
        print('\n"delete" to reset Savefile to default;\n"unlockall" to cheat ingame Items and beat 50/20(Please dont claim its legit);\n"cbackup" to create a backup of the current savefile;\n"lbackup" to load a backup by filename;\n"exit" to Exit\n')
        time.sleep(2)
        command()
    elif cmd == "exit":
        exit()
    elif cmd == "delete":
        reset_file()
        print("resetting file")
        time.sleep(1)
    elif cmd == "unlockall":
        cheat_file()
        print("unlocking all..")
        time.sleep(1)
    elif cmd == "cbackup":
        if not os.path.isdir("./Backups"):
            os.system("md .\Backups")
        bak = input("Enter filename for Backup: ")
        create_backup(bak)
        print("creating backup..")
        time.sleep(1)
    elif cmd == "lbackup":
        if not os.path.isdir("./Backups"):
            os.system("md .\Backups")
        bak = input("Enter filename of Backup: ")
        if os.path.isfile("Backups/" + bak):
            print("loading backup..")
            load_backup(bak)
            time.sleep(1)
        else:
            print("Error: Backup not Found")
            time.sleep(1)
            command()
    else:
        print("error: command '" + cmd + "' doesnt exist. please try again")
        time.sleep(2)
        command()
    print("done")
    time.sleep(1)
    command()

    
command()