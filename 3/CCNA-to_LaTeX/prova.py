#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

PART = "part3_extraOficial"

try:
	CAPITOL = sys.argv[1]
except IndexError:
	print("Es necessari el numero del capitol")
	exit()

os.chdir("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/")
print(os.getcwd())

fitxerControl = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/Control", "r")
fitxerBASH = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/BASH.sh", "a")
fitxerDesti = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/" + CAPITOL + ".tex","a")

fitxerDesti.write("% Capitol " + CAPITOL +"\n")
fitxerBASH.write("#!/usr/bin/bash\n\ncat $1 | sed '1,23d' | sed 's/        <h1>/<h1>/g'  > $1.bak\ntac $1.bak | sed '1,7d' | tac  > $1.fi\nrm $1.bak")
fitxerBASH.close()

linia = fitxerControl.readline()

while linia:
	if linia[0] == "\\":
		if linia[1] == "c":
			fitxerDesti.write(linia)
			fitxerDesti.close()
		elif linia[2] == "e" and linia[8] == "{":
			fitxerDesti = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/" + CAPITOL + ".tex","a")
			fitxerDesti.write("\t" + linia)
			fitxerDesti.close()
		elif linia[5] == "e" and linia[11] == "{":
			fitxerDesti = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/" + CAPITOL + ".tex","a")
			fitxerDesti.write("\t\t" + linia)
			fitxerDesti.close()
		elif linia[8] == "e" and linia[14] == "{":
			fitxerDesti = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/" + CAPITOL + ".tex","a")
			fitxerDesti.write("\t\t\t" + linia)
			fitxerDesti.close()
		print("Escrivint:\t" + linia)
	else:
		if linia[0] == CAPITOL[0]:
			print("NUMERO:\t"+ linia[0:len(linia)-1] + ".html")
			os.system("sh /home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/BASH.sh " + linia[:len(linia)-1] + ".html")
			os.system("python3 /home/jacquard/Documents/UOC/Latex/a_latex.py " + CAPITOL + " " + linia[:len(linia)-1] +".html.fi" + " " + PART)
		elif linia[0] == "C":
			fitxerDesti = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/" + CAPITOL + ".tex","a")
			fitxerDesti.write("\n\\end{itemize}")
			fitxerDesti.close()
		elif linia[0] == "u":
			fitxerDesti = open("/home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/" + CAPITOL + ".tex","a")
			linia2 = linia.replace("uoc","\\begin{figure}[h!]\n\t\\begin{center}\n\t\t\includegraphics[scale=0.8]{" + PART + "/capitol" + CAPITOL + "/imatges/uoc")
			linia2 = linia2.replace(" -> ",".png}\n\t\\end{center}\t\n\\caption{")
			linia2 = linia2.replace("µ","}\n\\end{figure}\n\n")#			print(linia2 + " " + linia2.replace("µ", "555555555555555555555555555555555555555555555555555"))
			fitxerDesti.write(linia2)
			fitxerDesti.close()
	linia = fitxerControl.readline()

fitxerControl.close()
fitxerDesti.close()
os.system("cp /home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/DadesBrut/" + CAPITOL + ".tex /home/jacquard/Documents/UOC/Latex/" + PART + "/capitol" + CAPITOL + "/cap" + CAPITOL + ".tex")
