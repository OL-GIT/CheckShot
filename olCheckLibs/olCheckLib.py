# -*- coding: utf8 -*-

# Various Checks
import os
import sys

myOS = (sys.platform)
if myOS ==  "cygwin":
	pgmDir = "/cygdrive/e/OCR/P06/PROGRAM/"
else:
	pgmDir = "/home/ol/OCR/P06/PROGRAM/"
libDir = pgmDir + 'olCheckLibs/'
print(libDir)
#sys.path.insert(0, libDir)
sys.path.append(libDir)
print("sys.path :", sys.path)

# from olCheckLibs import olHtmlLib
from olHtmlLib import olHtml, olCss


curDir = os.getcwd()  


# --------------------------------------------------------------------------------
### olCol - Console colors
class olCol():
	def Purple(text):
		print('\033[95m'+text)
	def Cyan(text):
		print('\033[96m'+text)
	def DarkCyan(text):
		print('\033[36m'+text)
	def Blue(text):
		print('\033[94m'+text)
	def Green(text):
		print('\033[92m'+text)
	def Yellow(text):
		print('\033[93m'+text,end='')
	def Red(text):
		print('\033[91m'+text)
	def Bold(text):
		print('\033[1m'+text)
	def UnderLine(text):
		print('\033[4m'+text)
	def End():
		print('\033[0m',end='')


# --------------------------------------------------------------------------------
### Lines - Console lines
class olPr():
	def eLine():
		print("")
	def sLine():
		print("------------------------------------------------------------------------")
	def bLine():
		print("# ==================================================================== #")
	def dLine1():
		print("########################################################################")
	def dLine2():
		print("#                                                                      #")
	def newLine():
		print("\n")


# --------------------------------------------------------------------------------
### HTML Reports
class olReports():

	# ----------------------------------------
	### WRITE REPORT START
	def reportStart(leftField):
		org_stdout = sys.stdout
		with open('report.htm', 'a') as olReport:
			sys.stdout = olReport						# set output to olReport
			olCss.TRTD()
			print("        ",leftField)
			olCss.TDTD700()
			sys.stdout = org_stdout						# Back to std output

	### WRITE REPORT END
	def reportEnd():
		org_stdout = sys.stdout
		with open('report.htm', 'a') as olReport:
			sys.stdout = olReport						# set output to olReport
			olCss.TDTR()
			sys.stdout = org_stdout						# Back to std output


# --------------------------------------------------------------------------------
### Verifications
class olChecks():

	# ----------------------------------------
	### Is file empty or missing ?
	def isEmpty(file):
		print("\033[93m  --- Function isEmpty \033[0m")
		size = os.stat(file).st_size
		if size > 0:
			with open('.bounds','r') as boundfile:
				line = boundfile.readline().rstrip()
				bounds = line.split()
				if not bounds:
					print("  .bounds is not empty but contains nothing")
				else:
					print("  .bounds is not empty")
		else:
			print("  .bounds is empty")
			print("  Please inquire the .bounds file in", curDir)


	# ----------------------------------------
	### Is file empty or missing ?
	def isEmptyHtml(file):
		org_stdout = sys.stdout

		size = os.stat(file).st_size
		leftField = "Bounds"
		# print(leftField)

		olReports.reportStart(leftField)

		with open('report.htm', 'a') as olReport:
			sys.stdout = olReport						# set output to olReport

			if size > 0:
				with open('.bounds','r') as boundfile:
					line = boundfile.readline().rstrip()
					bounds = line.split()
					if not bounds:
						print("<li> WARNING - .bounds is not empty but contains nothing")
					else:
						print("        <li> OK - .bounds is not empty : ", line)
			else:
				print("        <li> WARNING - .bounds is empty")
				print("  Please inquire the .bounds file in", shotdir)
			sys.stdout = org_stdout						# Back to std output

		# print("        <li> WARNING - .bounds is missing")
		# print("  Please inquire the .bounds file in", curDir)

		olReports.reportEnd()



	# ----------------------------------------
	### Extract start bound
	def myStart():
		print("  \033[93m--- Function myStart \033[0m")
		with open('.bounds','r') as boundfile:
			for line in boundfile:
				bounds = line.split()
				if bounds:
					mystart = int(bounds[0])
				else:
					print("  .bounds is not empty but contains nothing")
					mystart = 0
		# print("mystart:", mystart)
		return mystart


	# ----------------------------------------
	### Extract end bound
	def myEnd():
		print("  \033[93m--- Function myEnd \033[0m")
		with open('.bounds','r') as boundfile:
			for line in boundfile:
				bounds = line.split()
				if bounds:
					myend = int(bounds[1])
				else:
					print("  .bounds is not empty but contains nothing")
					myend = 0
		# print("myend:", myend)
		return myend


	# ----------------------------------------
	### Extract duration
	def myBounds():
		print("  \033[93m--- Function myBounds \033[0m")

		if os.path.isfile('.bounds'):

			with open('.bounds','r') as boundfile:
				line = boundfile.readline().rstrip()
				bounds = line.split()
				if bounds:
					boundsNb = len(bounds)
					if boundsNb == 2:
						try:
							(bounds[0]) = int(bounds[0])
						except:
							pass
						try:
							(bounds[1]) = int(bounds[1])
						except:
							pass

						# print(isinstance(bounds[0], int))
						if isinstance(bounds[0], int) == False:
							# print("  1st value is not an integer")
							mystart = 0
							myend = 0
							duration = 1
						else:
							# print("  1st value is an integer")
							if isinstance(bounds[1], int) == False:
								# print("  2nd value is not an integer")
								mystart = 0
								myend = 0
								duration = 1
							else:
								# print("  2nd value is an integer")
								mystart = int(bounds[0])
								myend = int(bounds[1])
								duration = myend - mystart + 1
								print("  Start:", mystart, "| End:", myend)
								print("  Expected duration :", duration)

					### If there is only 1 bound
					elif boundsNb == 1:
						mystart = 0
						myend = 0
						duration = 1
						print("  End bound missing")
						print("  Unknown duration")

				### If bounds contains null
				else:
					mystart = 0
					myend = 0
					duration = 1
					print("  .bounds is not empty but contains nothing")
					print("  Unknown duration")
			return mystart, myend, duration

		else:
			mystart = 0
			myend = 0
			duration = 0
			print("  .bounds missing")
			print("  Unknown duration")
			return mystart, myend, duration


	# ----------------------------------------
	### Check number of images
	def nbImages(listPics):
		print("  \033[93m--- Function nbImages \033[0m")
		nbPics = 0
		for pic in listPics:
			# print("PIC:", pic)
			nbPics += 1
		print("  Number of pics in", curDir,":", nbPics)
		return nbPics



# --------------------------------------------------------------------------------
### Comparisons
class olCompares():


	# ----------------------------------------
	### Compare number of images and required duration
	def nbImagesVsDuration(listPics):
		print("\033[93m  --- Function nbImagesVsDuration \033[0m")
		valid = 1
		duration = int(olChecks.myBounds()[2])
		nbPics = int(olChecks.nbImages(listPics))
		if duration == nbPics:
			print("*** OK *** Required pics = Number of pics ")
		else:
			print("*** NO *** Required pics != Number of pics ")
			valid = 0

		if valid == 0:
			validShot = valid
			# print("  VALIDSHOT :", validShot)
			return validShot





		