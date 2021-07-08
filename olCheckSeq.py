# -*- coding: utf8 -*-

# ----------------------------------------
### LICENSE
# ----------------------------------------
# MIT License 
# Copyright (c) 2021 OL-GIT


# ----------------------------------------
### IMPORTS
# ----------------------------------------
import os
from os import listdir, stat
import re
import shutil
import socket
import sys
import time
from datetime import datetime

myOS = (sys.platform)
if myOS ==  "cygwin":
	pgmDir = "/cygdrive/e/OCR/P06/PROGRAM/"
else:
	pgmDir = "/home/ol/OCR/P06/PROGRAM/"
libDir = pgmDir + 'olCheckLibs/'
sys.path.append(libDir)

from olCheckLib import olCol, olPr, olChecks, olCompares
from olHtmlLib import olHtml, olCss

# ----------------------------------------
### TITLE
# ----------------------------------------
olPr.bLine()
text = "# ----------- OLCHECKSEQ ---------- v0.2 --------- 210630 ------------ # "
olCol.Yellow(text)
olCol.End()
olPr.eLine()
olPr.bLine()
text=""
print('''
   XXXX  XX                      XX       XXXXX
  X    X  X                       X      X     X
 X        X                       X      X
 X        X XX    XXXXX   XXXXX   X  XX  X        XXXXX   XXXXXX
 X        XX  X  X     X X     X  X  X    XXXXX  X     X X    X
 X        X   X  XXXXXXX X        X X          X XXXXXXX X    X
 X        X   X  X       X        XXX          X X       X    X
  X    X  X   X  X     X X     X  X  X   X     X X     X X    X
   XXXX  XXX XXX  XXXXX   XXXXX  XX   XX  XXXXX   XXXXX   XXXXX
                                                              X
                                                             XXX
''')
olPr.bLine()


# ----------------------------------------
### VARIABLES
# ----------------------------------------
myMach = socket.gethostname()
myDate = datetime.now().strftime("%y%m%d-%H%M")
curDir = os.getcwd()
splitCurDir = os.path.split(curDir)
prjDir = (splitCurDir[0])
seqDir = curDir
webRef = pgmDir + "olCheckWebRef"
webDir = seqDir + "/.web"
report = webDir + "/seqReport.htm"
logDir = prjDir + "/LOGS/"
checkShot = pgmDir + "olCheckShot.py"

text=""
olCol.Yellow(text)
print("myOS   :", myOS)
print("myMach :", myMach)
print("myDate :", myDate)
print("curDir :", curDir)
print("prjDir :", prjDir)
print("seqDir :", seqDir)
print("webRef :", webRef)
print("webDir :", webDir)
print("report :", report)
print("logDir :", logDir)
print("pgmDir :", pgmDir)
print("checkShot :",checkShot)
olCol.End()
olPr.eLine()


# ----------------------------------------
### LOGS
# ----------------------------------------
if not os.path.isdir(logDir):
	print(logDir, "does not exist, creating it.")
	os.makedirs(logDir)
else:
	print(logDir, "already exists.")

global logCS
logCS = logDir + "olCheckSeqlog." + myDate + ".txt"
print("logFile :", logCS)

olCol.End()
olPr.eLine()



# ----------------------------------------
### Create the sequence page
### If the webDir does not exist, create the minisite

if not os.path.isdir(webDir):
	print(webDir, "does not exist, creating it.")
	shutil.copytree(webRef, webDir)
else:
	print(webDir, "already exists.")

seqRepName = webDir + "/seqReport.htm"
olHtml.mkSeqPageStart(curDir)
print("Writing Report", seqRepName)
global olSeqReport
org_stdout = sys.stdout						# keep std output in variable



# ----------------------------------------
### Create the logFile
org_stdout = sys.stdout

if not logCS:
	open(logCS, 'x')
else:
	pass
	# print(logCS, "already exists")

with open(logCS, 'w') as sLog:
	sys.stdout = sLog					# set output to sLog
	olPr.dLine1()
	olPr.dLine2()
	print("# olCheckSeq                                              ", myDate, "#")
	olPr.dLine2()
	olPr.dLine1()
	print(": Checking content in : ", curDir)
	olPr.eLine()
	sys.stdout = org_stdout			# Back to std output



# ----------------------------------------
### Go to the shots

n = len(sys.argv)
# print("Total arguments:", n)
# print("Script :", sys.argv[0])

if n == 1:
	olPr.eLine()
	# print("*** Usage : python3 olCheckSeq.py <argsuments>")
	# print("*** Where <args> can be : P10, P1 P2 P3, P*, *")

	text='''
| Usage : python3 olCheckSeq.py <arguments>  |
| Where <args> can be : P10, P1 P2 P3, P*, * |
	'''
	olCol.Yellow(text)
	olCol.End()
	olPr.eLine()

	with open(report, 'a') as olSeqReport:
		sys.stdout = olSeqReport	
		print('<br><br><br><br>')
		olCss.TDe()
		olCss.TRe()
		sys.stdout = org_stdout					# Back to std output

	with open(logCS, 'a') as sLog:
		sys.stdout = sLog					# set output to sLog
		olPr.eLine()
		print("*** WARNING : No argument given, exiting")
		olPr.eLine()
		sys.stdout = org_stdout			# Back to std output

else:

	for itSeqLoop in range(1, n):
		# print("i :", i, sys.argv[i], end = " ")
		olPr.eLine()
		olPr.bLine()
		print("# CheckSeq Instruction :")
		# print("    - Shot", i, "to check:", end = "")
		print("    - Shot", itSeqLoop, "to check:")
		# print(sys.argv[i])

		shotDir = curDir+"/"+(sys.argv[itSeqLoop])
		print("    - shotDir would be :", shotDir)

		with open(logCS, 'a') as sLog:
			sys.stdout = sLog					# set output to sLog
			olPr.eLine()
			olPr.bLine()
			print("# CheckSeq Instruction :")
			print("    - Shot", itSeqLoop, "to check:", end = " ")
			print(sys.argv[itSeqLoop])
			olPr.eLine()
			print("* Check if {0} exists".format(shotDir))
			sys.stdout = org_stdout			# Back to std output

		if os.path.isdir(shotDir):
			print("***", shotDir, "exists")
			with open(logCS, 'a') as sLog:
				sys.stdout = sLog					# set output to sLog
				print("*** {0} exists".format(shotDir))
				olPr.eLine()
				sys.stdout = org_stdout			# Back to std output
		else:
			print("***", shotDir, "does not exist")

		try:
				### Go to shot 
				os.chdir(shotDir)
				print("Current working directory: {0}".format(os.getcwd()))
				olPr.eLine()

				text = "CMD : python3\n      " + pgmDir + "olCheckShot.py\n      " + shotDir
				olCol.Yellow(text)
				olCol.End()

				olPr.eLine()
				olPr.eLine()

				### Execute olCheckShot.py on each selected Shot :
				checkShotCmd = "python3 " + pgmDir + "olCheckShot.py " + shotDir
				os.system(checkShotCmd)


				### Go back to Seq Level
				os.chdir(curDir)
				# os.chdir("..")
				curDir = os.getcwd()

				splitPath = shotDir.split("/")
				linkShot = splitPath[-1:]

				linkPath = None
				for shot in linkShot:
					if linkPath is None:
						linkPath = shot
					else:
						linkPath = linkPath+"/"+shot

				with open(report, 'a') as olSeqReport:
					sys.stdout = olSeqReport	
					olCss.TRs()
					olCss.TDs()
					print('        SHOT : <a href="../'+linkPath+'/report.htm" target="right">'+linkPath+'</a>')
					olCss.TDe()
					olCss.TRe()
					sys.stdout = org_stdout					# Back to std output


		except FileNotFoundError:
			print("*** {0} does not exist".format(shotDir))

			with open(logCS, 'a') as sLog:
				sys.stdout = sLog					# set output to sLog
				print("*** {0} does not exist".format(shotDir))
				olPr.eLine()
				sys.stdout = org_stdout			# Back to std output


		except NotADirectoryError:
			print("*** {0} is not a directory".format(shotDir))

			with open(logCS, 'a') as sLog:
				sys.stdout = sLog					# set output to sLog
				print("*** {0} is not a directory".format(shotDir))
				olPr.eLine()
				sys.stdout = org_stdout			# Back to std output


		except PermissionError:
			print("*** No permission to go to {0}".format(shotDir))

			with open(logCS, 'a') as sLog:
				sys.stdout = sLog					# set output to sLog
				print("*** No permission to go to {0}".format(shotDir))
				olPr.eLine()
				sys.stdout = org_stdout			# Back to std output


		# zeDir = os.getcwd()
		# print(zeDir)
		olPr.eLine()


with open(logCS, 'a') as sLog:
	sys.stdout = sLog					# set output to sLog
	olPr.eLine()
	olPr.dLine1()
	print("# END OF LOG                                              ", myDate, "#")
	olPr.dLine1()
	olPr.eLine()
	sys.stdout = org_stdout			# Back to std output



print("Finished Sequence")
olHtml.mkSeqPageEnd()

