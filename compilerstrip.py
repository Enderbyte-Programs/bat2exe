import os
import subprocess
import shutil

def main():
    bannedfiles = ["test.c","a.exe","gcc.exe"]
    rootdir = 'C:\\Users\\Jordan\\Desktop\\Compiler'
    command = r"C:\Users\Jordan\Desktop\compiler\bin\gcc.exe C:\Users\Jordan\Desktop\compiler\bin\test.c"
    filess = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if True in [f in file for f in bannedfiles]:#Make sure file is not banned
                continue
            filess.append(os.path.join(subdir, file))
    for file in filess:
        _name = file.replace("/","\\").split("\\")[-1]
        shutil.move(file,_name)
        retc = subprocess.call(command.split(" "),stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        
        if retc != 0:
            #Failure
            print(f"File {file} FAILED (size: {os.path.getsize(_name)})")
            shutil.move(_name,file)
            
        else:
            print(f"File {file} Succeeded (size: {os.path.getsize(_name)})")
            retc = subprocess.call(command.split(" "),stderr=subprocess.PIPE,stdout=subprocess.PIPE)
            if retc== 0:
                os.remove(_name)#Sucess
            else:
                print("False alarm")
                shutil.move(_name,file)
    retc = subprocess.call(command.split(" "),stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    print(retc)
            

if __name__ == "__main__":
    main()