import sys
import os
try:
    filen=sys.argv[1]
except:
    print("Please provide file name")

defaultdata="""int main(){
    system(\"$$DATA\");
}
"""
with open("tmp.c","w+") as f:
    with open(filen) as g:
        dat = g.readlines()
        dat = [d for d in dat if d.replace(" ","") != ""]
    msg = " && ".join(dat).replace("\n","")
    f.write(defaultdata.replace("$$DATA",msg))
compi = "\\".join(sys.argv[0].replace("/","\\").split("\\")[0:-1])+"\\compiler\\bin\\gcc.exe"
if compi[1] != ':':
    compi = "."+compi
os.system(f'{compi} tmp.c --no-warn -o {filen.replace(".bat",".exe")}')
os.remove("tmp.c")