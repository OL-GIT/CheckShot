#! /usr/bin/env python3
# -*- coding: utf8 -*-

# ----------------------------------------
### LICENSE
# ----------------------------------------
# MIT License - Copyright (c) 2021 OL-GIT


# ----------------------------------------
### Images extension
# ----------------------------------------
ext = "jpg"


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

pgmDir = "/opt/checkShot/"

# Silent mode for sys.path
from io import StringIO
org_stdout = sys.stdout
silent = StringIO()
sys.stdout = silent

libDir = pgmDir + 'olCheckLibs/'
sys.path.append(libDir)
from olCheckLib import olCol, olPr, olReports, olChecks
from olHtmlLib import olHtml, olCss

sys.stdout = org_stdout


# ----------------------------------------
### VARIABLES
# ----------------------------------------
myMach = socket.gethostname()
myDate = datetime.now().strftime("%y%m%d-%H%M")
curDir = os.getcwd()
seqDir, shotDir = os.path.split(curDir)
prjDir, seqRep = os.path.split(seqDir)
webDir = seqDir + "/.web"
seqReport = webDir + "/seqReport.htm"
logDir = prjDir + "/LOGS"
checkShot = pgmDir + "olCheckShot.py"
report = curDir + "/report.htm"


# ----------------------------------------
### TITLE
# ----------------------------------------
def olTitle():
	olPr.sLine()
	print("# \033[33m------------ OLCHECKSHOT --------- v0.3 --------- 210709 -----------\033[0m #")
	olPr.sLine()
	text=""
	olCol.Yellow(text)
	print('''
   XXXX  XX                      XX       XXXXX  XX
  X    X  X                       X      X     X  X                X
 X        X                       X      X        X                X
 X        X XX    XXXXX   XXXXX   X  XX  X        X XX    XXXXX   XXXX
 X        XX  X  X     X X     X  X  X    XXXXX   XX  X  X     X   X
 X        X   X  XXXXXXX X        X X          X  X   X  X     X   X
 X        X   X  X       X        XXX          X  X   X  X     X   X
  X    X  X   X  X     X X     X  X  X   X     X  X   X  X     X   X  X
   XXXX  XXX XXX  XXXXX   XXXXX  XX   XX  XXXXX  XXX XXX  XXXXX     XX
	''')
	olCol.End()
	olPr.sLine()


# ----------------------------------------
### INTRO
# ----------------------------------------
def olIntro():
	print("myDate :", myDate)
	print("curDir :", curDir)
	print("prjDir :", prjDir)
	print("seqDir :", seqDir)
	print("webDir :", webDir)
	print("logDir :", logDir)
	print("pgmDir :", pgmDir)
	print("libDir :", libDir)
	print("checkShot :",checkShot)
	print("seqReport :", seqReport)
	print("report :", report)
	olPr.sLine()
	text=""
	olCol.Yellow(text)
	print("\033[1mWARNING - REQUIRED IMAGES EXTENSION :", ext, "\033[0m")
	olPr.sLine()
	olCol.End()
	olPr.eLine()


# ----------------------------------------
### LOGS
# ----------------------------------------
def olLogs():
	if not os.path.isdir(logDir):
		print(logDir, "does not exist, creating it.")
		os.makedirs(logDir)
	else:
		print(logDir, "already exists.")

	global logCS
	logCS = logDir + "/" + "olCheckSeqlog." + myDate + ".txt"
	print("logFile :", logCS)

	olCol.End()
	olPr.eLine()


# ----------------------------------------
### Check Arguments
# ----------------------------------------
def checkArgv():
	print("\033[93m--- Function checkArgv \033[0m")

	n = len(sys.argv)
	if n == 1:
		print("Working in current directory")
		olPr.eLine()
	elif n == 2:
		askedShot = sys.argv[1]

		lastChar = (askedShot[-1])
		if lastChar == "/":
			askedShot = askedShot[:-1]
		splitAskedShot = os.path.split(askedShot)
		askedDir = (splitAskedShot[1])
		print(askedShot)

		splitPath = os.path.split(curDir)
		lastDir = (splitPath[1])

		if askedDir == lastDir:
			olPr.eLine()
			text = "You are in asked shot :" + askedShot
			olCol.Green(text)
			olPr.eLine()
			olCol.End()
		else:
			olPr.eLine()
			text = "You are not in asked shot :" + askedShot
			olCol.Red(text)
			olPr.eLine()
			olCol.End()
			exit(0)
	else:
		text = '''
	Number of arguments must be 0 or 1
	- Ex : olCheckShot.py
	or
	- Ex : olCheckShot.py P1
		'''
		olCol.Purple(text)
		exit(0)


# ----------------------------------------
### INTRO2
# ----------------------------------------
def olIntro2():
	print("WE ARE HERE :", curDir)
	print("WE LOG HERE :", logDir)
	olCol.End()
	olPr.eLine()
	olPr.sLine()
	olPr.eLine()


# ----------------------------------------
### WRITE REPORT START
# ----------------------------------------
def reportStart(leftField):
	sys.stdout = olReport						# set output to olReport
	olCss.TRTD()
	print("        ",leftField)
	olCss.TDTD700()

### WRITE REPORT END
def reportEnd():
	olCss.TDTR()
	sys.stdout = org_stdout						# Back to std output


# ----------------------------------------
### Generate the log file if not already created by olCheckSeq.py
# ----------------------------------------
def makeLog():
	print("\033[93m--- Function makeLog \033[0m")
	org_stdout = sys.stdout

	myDate = datetime.now().strftime("%y%m%d-%H%M")

	if os.path.isfile(logCS):
		print("LOG CS :", logCS)
		print(logCS, "already exists")
	else:
		print(logCS, "does not exist")
		open(logCS, 'x')

	with open(logCS, 'a') as sLog:
		olPr.eLine()

		sys.stdout = sLog					# set output to sLog
		olPr.dLine1()
		olPr.dLine2()
		print("# olCheckShot                                             ", myDate, "#")
		olPr.dLine2()
		olPr.dLine1()
		print("# olCheckShot -", myDate)
		print("# Checking content in : ", curDir)
		olPr.sLine()
		print("Shot directory: {0}".format(os.getcwd()))
		olPr.eLine()
		sys.stdout = org_stdout			# Back to std output

	olPr.eLine()


# ----------------------------------------
### Check if report.htm exist in Shot
### If so, backup to report_PATH_date.htm
# ----------------------------------------
def isReport():

	if os.path.isfile('report.htm'):
		text = '  *** A report already exists for this Shot.'
		olCol.Yellow(text)
		olCol.End()

		repMtime = os.path.getmtime('report.htm')
		repCtime = time.ctime(repMtime)
		repIso = time.strptime(repCtime)
		creDate = time.strftime("%y%m%d-%H%M", repIso)

		# Backup to "report_<date>.htm"
		orgReport = r'report.htm'
		savReport = r'report' + "_" + shotReport + "_" + creDate + '.htm'
		shutil.copyfile(orgReport, savReport)

		olPr.eLine()
		print("  . Last shot Report created", repCtime)
		print("  . Copying to", savReport)
		print("  . Writing", repName)

		with open(logCS, 'a') as sLog:
			sys.stdout = sLog					# set output to sLog
			print("  . Shot Report created", repCtime)
			print("  . Copying to", savReport)
			print("  . Writing", repName)
			print("")
			sys.stdout = org_stdout			# Back to std output

	else:
		text = '    *** No report yet for this Shot.'
		olCol.Yellow(text)
		olCol.End()


# ----------------------------------------
### Check content in dir : .bounds + pics
# ----------------------------------------
def listContent():
	print("\033[93m--- Function listContent \033[0m")
	isHtm = "htm"

	os.chdir(curDir)

	listFiles = os.listdir(curDir)
	listFiles.sort()
	for file in listFiles:

		if file == ".bounds":
			print(file, "exists.")
			olChecks.isEmpty(file)				# Checks if .bounds is empty

			sys.stdout = olReport				# set output to olReport
			olChecks.isEmptyHtml(file)			# Checks if .bounds is empty
			sys.stdout = org_stdout				# Back to std output

		elif file == "report.htm":
			text = '  *** A report already exists for this Shot.'
			olCol.Yellow(text)
			olCol.End()
			olPr.eLine()
			olPr.eLine()

		elif isHtm in file:
			# print("htm file found :", file)
			pass

		else:
			listPics.append(file)

	firstPic = listPics[0]
	lastPic = listPics[-1]

	text = "listPics : " + firstPic + " -> " + lastPic
	olCol.Yellow(text)
	olCol.End()
	olPr.eLine()
	olPr.eLine()


# ----------------------------------------
### Compare number of images and required duration
# ----------------------------------------
def nbImagesVsDuration(listPics):
	print("\033[93m  --- Function nbImagesVsDuration \033[0m")
	valid = 1
	duration = int(olChecks.myBounds()[2])
	nbPics = int(olChecks.nbImages(listPics))
	leftField = "Quantity"

	if duration == 0:
		print("*** NO *** No .bounds file ")
		leftField = "Bounds"
		reportStart(leftField)
		print("        <li> WARNING - .bounds file missing")
		reportEnd()

		leftField = "Quantity"
		reportStart(leftField)
		print("        <li> WARNING - Unable to estimate required number of images")
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("WARNING - No .bounds file")
		sys.stdout = org_stdout			# Back to std output


	elif duration == nbPics:
		print("*** OK *** Required pics :", nbPics)

		reportStart(leftField)
		print("        <li> OK - Required pics = Number of pics")
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("OK - Required pics = Number of pics")
		sys.stdout = org_stdout			# Back to std output

	else:
		print("*** NO *** Required pics != Number of pics ")


		reportStart(leftField)
		print("        <li> WARNING - Required pics != Number of pics :")
		olCss.HR()
		olCss.LSs()
		print(" Required :", duration, "/", "Found : ", nbPics)
		olCss.LSe()
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("WARNING - Required pics != Number of pics")
		sys.stdout = org_stdout			# Back to std output

		valid = 0

	if valid == 0:
		validShot = valid
		# print("  VALIDSHOT :", validShot)
		return validShot


# ----------------------------------------
### Compare number and duration
# ----------------------------------------
def compareNbPics():
	print("\033[93m--- Function compareNbPics \033[0m")
	valid = 1
	# print(listPics)
	valid = nbImagesVsDuration(listPics)
	if valid == 0:
		validShot = valid
		# print("VALIDSHOT :", validShot)
	olPr.eLine()


# ----------------------------------------
### Check if second field is numeric
# ----------------------------------------
def numInPic():
	print("\033[93m--- Function numInPic \033[0m")
	global validShot
	nonNumeric = []
	leftField = "Numeric"
	valid = 1

	# print(listPics)
	for pic in listPics:
		picName=pic.split(".")
		picNum = picName[1]
		if picNum.isnumeric() == False:
			nonNumeric.append(pic)

	if not nonNumeric:
		print("*** OK *** Second fields are numerical in all pics")

		reportStart(leftField)
		print("        <li> OK - Second fields are numerical in all pics")
		reportEnd()
	
		sys.stdout = sLog					# set output to sLog
		print("OK - Second fields are numerical in all pic")
		sys.stdout = org_stdout			# Back to std output

	else:
		print("*** Warning *** : Non numerical 2nd field in these pics :\n", nonNumeric)

		reportStart(leftField)
		print("        <li> WARNING - Non numerical 2nd field in these pics :")
		olCss.HR()
		olCss.LSs()
		for nonNum in nonNumeric:
			print("-", nonNum)
		olCss.LSe()
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("WARNING - Non numerical 2nd field in these pics")
		sys.stdout = org_stdout			# Back to std output

		valid = 0

	if valid == 0:
		validShot = valid
		# print("VALIDSHOT :", validShot)
		olPr.eLine()
		return validShot
	else:
		olPr.eLine()


# ----------------------------------------
### Verify bounds and pics
# ----------------------------------------
def comparePicsWithBounds():
	print("\033[93m--- Function comparePicsWithBounds \033[0m")
	global validShot
	
	bounds = olChecks.myBounds()
	mystart = bounds[0]
	myend = bounds[1]
	duration = bounds[2]

	num = mystart
	missPics = str()
	leftField = "Missing"
	valid = []

	if duration == 0:
		valid = 0
		print("*** WARNING *** Missing .bounds file")
	elif duration == 1:
		valid = 0
		print("*** WARNING *** Incorrect .bounds file")
	else:
		print("  -> Duration found :", duration)
		while num <= duration:
			realNum = str(num).zfill(4)
			picMatch = [x for x in listPics if realNum in x]
			if not picMatch:
				print("Image", realNum, "is missing")
				missPics = missPics+" "+realNum
				valid = 0
			num = num + 1
		if valid == 0:
			print("*** WARNING *** Missing pics :", missPics)

			reportStart(leftField)
			print("        <li> WARNING - Missing pics :")
			olCss.HR()
			olCss.LSs()
			print(missPics)
			olCss.LSe()
			reportEnd()

			sys.stdout = sLog					# set output to sLog
			print("NO - Missing pics :")
			print(missPics)
			sys.stdout = org_stdout			# Back to std output


	if valid == 0:
		validShot = valid
	else:
		print("*** OK *** No missing pics")

		reportStart(leftField)
		print("        <li> OK - No missing pics")
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("OK - No missing pics")
		sys.stdout = org_stdout			# Back to std output

	# print("VALIDSHOT :", validShot)
	olPr.eLine()
	return validShot


# ----------------------------------------
### Verify pics extensions
# ----------------------------------------
def verifyExts():
	print("\033[93m--- Function verifyExts \033[0m")
	global validShot
	valid = []
	extMatch = [x for x in listPics if not ext in x]
	badFields = []

	for pic in listPics:
		picName=pic.split(".")

		wordNb = len(pic.split("."))
		# If there are 3 words in the picName
		if wordNb != 3:
			print("Bad number of fields in", pic)
			badFields.append(pic)

		else:
			picExt = picName[2]

			try:
				(picName[2]) = int(picName[2])
			except:
				pass

			if isinstance(picName[2], int) == True:
				extMatch.append(pic)
			else:
				pass

	# print(extMatch)
	leftField = "Fields"
	if badFields:
		print("Wrong number of fields :")
		print(badFields)
		valid = 0
		validShot = valid
		print("VALIDSHOT :", validShot)
		olPr.eLine()

		reportStart(leftField)
		print("        <li> WARNING - Wrong number of fields :")
		olCss.HR()
		olCss.LSs()
		for badFld in badFields:
			print("-", badFld)
		olCss.LSe()
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("NO - Wrong number of fields :")
		print(badFields)
		sys.stdout = org_stdout			# Back to std output

	else:
		reportStart(leftField)
		print("        <li> OK - Number of fields is correct in all pics")
		reportEnd()


	leftField = "Extensions"
	if extMatch:
		print("Bad extension :")
		print(extMatch)
		print("*** WARNING *** Bad Extensions")
		valid = 0
		validShot = valid
		print("VALIDSHOT :", validShot)
		olPr.eLine()

		reportStart(leftField)
		print("        <li> WARNING - Bad Extensions :")
		olCss.HR()
		olCss.LSs()
		for extMat in extMatch:
			print("-", extMat)
		olCss.LSe()
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("NO - Bad Extensions")
		print(extMatch)
		sys.stdout = org_stdout			# Back to std output

		return valid

	else:
		leftField = "Extensions"
		print("*** OK *** No bad Extensions")
		olPr.eLine()

		reportStart(leftField)
		print("        <li> OK - No bad Extensions")
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("OK - No bad Extensions")
		sys.stdout = org_stdout			# Back to std output


# ----------------------------------------
### Verify if a file is empty
# ----------------------------------------
def verifyPics():
	print("\033[93m--- Function verifyPics (emtpy or not ?) \033[0m")
	global validShot
	leftField = "Weight"
	valid = []
	for spic in listPics:
		size = os.stat(spic).st_size
		if size == 0:
			print("ZERO :", repr(size).rjust(10), spic.ljust(10))
			emptyPics.append(spic)
			valid = 0
		else:
			pass

	if valid == 0:
		validShot = valid
		print("*** WARNING *** Empty pics found")
		print("EMPTY PICS :", emptyPics)
		print("VALIDSHOT :", validShot)

		reportStart(leftField)
		print("        <li> WARNING - Empty pics found :")
		olCss.HR()
		olCss.LSs()
		for empPic in emptyPics:
			print("-", empPic)
		olCss.LSe()
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("WARNING - Empty pics found")
		print(emptyPics)
		olPr.eLine()
		sys.stdout = org_stdout			# Back to std output

	else:
		print("*** OK *** No empty pics found")

		reportStart(leftField)
		print("        <li> OK - No empty pics found")
		reportEnd()

		sys.stdout = sLog					# set output to sLog
		print("OK - No empty pics found")
		olPr.eLine()
		sys.stdout = org_stdout			# Back to std output

	olPr.eLine()
	return validShot;


# ----------------------------------------
### Is shot valid ?
# ----------------------------------------
def isShotValid():
	olPr.sLine()
	print("\033[93m--- Function isShotValid \033[0m")

	if validShot == 0:
		print("\033[91m\033[1mWARNING :", shotPath,"\033[0m")
		print("Invalid, empty or missing files ...")
		olPr.sLine()

		# WRITE REPORT
		sys.stdout = olReport					# set output to olReport
		olCss.TRs()
		olCss.TDsC2()
		olCss.CEN()
		olPr.eLine()
		olCss.BR()
		olCss.F4(); olCss.Bs(); olCss.cRs()
		print("        WARNING :", shotPath)
		olPr.eLine()
		olCss.BR()
		olCss.Fe();	olCss.Be(); olCss.Fe()
		olCss.BR()
		print("        *** Invalid, empty or missing files ***")
		olPr.eLine()
		olCss.BR()
		olCss.Fe(); olCss.Be(); olCss.Fe()
		olCss.BR()
		olCss.TDe()
		sys.stdout = org_stdout					# Back to std output

	else:
		print("\033[92m\033[1mOK :", shotPath, "\033[0m")
		olPr.sLine()

		# WRITE REPORT
		sys.stdout = olReport					# set output to olReport
		olCss.TRs()
		olCss.TDsC2()
		olCss.CEN()
		olPr.eLine()
		olCss.BR()
		olCss.F4(); olCss.Bs(); olCss.cGs()
		print("        OK :", shotPath)
		olPr.eLine()
		olCss.BR()
		olCss.Fe(); olCss.Be(); olCss.Fe()
		olCss.BR()
		olCss.TDe()
		sys.stdout = org_stdout					# Back to std output

	olPr.eLine()


# ----------------------------------------
### Write pics details in report
# ----------------------------------------
def detailPics():
	print("\033[93m--- Function detailPics \033[0m")

	sys.stdout = olReport					# set output to olReport
	olCss.TRs()
	olCss.TDsC2g()
	olPr.eLine()

	listing = '''
       UID        GID            SIZE | FILE
--------------------------------------------------------------------------------
'''
	for spic in listPics:
		suid = os.stat(spic).st_uid
		sgid = os.stat(spic).st_gid
		size = os.stat(spic).st_size
		i1 = repr(suid).rjust(10)
		i2 = repr(sgid).rjust(10)
		i3 = repr(size).rjust(17)
		listing = listing + i1 + i2 + i3 + " | " + spic + '<br>'

	olCss.LST(listing)
	olPr.eLine()
	olCss.TDe()
	olCss.TRe()
	sys.stdout = org_stdout					# Back to std output


# ----------------------------------------
### END
# ----------------------------------------
def thisIsTheEnd():
	olPr.eLine()
	text = "END of CheckShot"
	olCol.Blue(text)
	olCol.End()
	text = ""




########################################
### EXECUTION
########################################
olTitle()
olIntro()
olLogs()


# ----------------------------------------
### CURRENT DIR DEFINITIONS
# ----------------------------------------
splitPath = curDir.split("/")
olShot = splitPath[-3:]
shotPath = None
shotReport = None
for i in olShot:
	if shotPath is None:
		shotPath = i
		shotReport = i
	else:
		shotPath = shotPath+"/"+i
		shotReport = shotReport+"-"+i
listFiles = os.listdir(curDir)
listFiles.sort()
listPics = []
emptyPics = []

# Floating variable for shot validation
# Stays at 1 as long as there is no error
validShot = "1"

# keep std output in variable
org_stdout = sys.stdout						


# ----------------------------------------
### LOGS AND REPORTS
# ----------------------------------------
repName = curDir + "/report.htm"
makeLog()
isReport()


# ----------------------------------------
### CHECKS
# ----------------------------------------
with open(logCS, 'a') as sLog:
	with open('report.htm', 'a') as olReport:
		olPr.eLine()
		olHtml.mkPageStart(curDir)
		print("REPORT HERE :", repName)

		olIntro2()
		checkArgv()
		listContent()
		compareNbPics()
		numInPic()
		comparePicsWithBounds()
		verifyExts()
		verifyPics()
		isShotValid()
		detailPics()

# ----------------------------------------
### END
# ----------------------------------------
print("Finished Report")
olHtml.mkPageEnd()
sys.stdout = org_stdout					# Back to std output
thisIsTheEnd()
