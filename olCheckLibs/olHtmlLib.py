# -*- coding: utf8 -*-

# Html

import os
import sys


# --------------------------------------------------------------------------------
### olCss
class olCss():
	def Bs():
		print('<b>')
	def Be():
		print('</b>')
	def Is():
		print('<i>')
	def Ie():
		print('</i>')
	def Us():
		print('<u>')
	def Ue():
		print('</u>')
	def cGs():
		print('<font color="#00ff00">')
	def cYs():
		print('<font color="#ffff00">')
	def cRs():
		print('<font color="#ff0000">')
	def cBs():
		print('<font color="#0000ff">')
	def BR():
		print('<br>')
	def HR():
		print('<hr noshade>')
	def F3():
		print('<font size="3">')
	def F4():
		print('<font size="4">')
	def F5():
		print('<font size="5">')
	def Fe():
		print('</font>')
	def TRs():
		print('<tr>')
	def TRe():
		print('</tr>')
	def TRTD():
		print('<tr>')
		print('    <td align="left" valign="top">')
	def TRTD100():
		print('<tr>')
		print('    <td align="left" valign="top" width="100">')
	def TDTR():
		print('    </td>')
		print('</tr>')
	def TDTD():
		print('    </td>')
		print('    <td align="left" valign="top">')
	def TDTD700():
		print('    </td>')
		print('    <td align="left" valign="top" width="700">')
	def TDs():
		print('    <td align="left" valign="top">')
	def TDs100():
		print('    <td align="left" valign="top" width="100">')
	def TDs200():
		print('    <td align="left" valign="top" width="200">')
	def TDsC2():
		print('    <td align="left" valign="top" colspan="2">')
	def TDsC2b():
		print('    <td align="left" valign="top" colspan="2" bgcolor=#0088ff>')
	def TDsC2g():
		print('    <td align="left" valign="top" colspan="2" bgcolor=#888888>')
	def TDe():
		print('    </td>')
	def LSs():
		print('<listing>')
	def LSe():
		print('</listing>')
	def LST(listing):
		print('<listing>')
		print(listing)
		print('</listing>')
	def CEN():
		print('<center>')

# --------------------------------------------------------------------------------
### HTML
class olHtml():
### Aller voir la bibliotheque HTML

# ----------------------------------------
### Make Head
	def mkHead(shotPath):
		print('<!DOCTYPE html>\n<html>\n<head>\n<title>')
		print("    shotCheck", shotPath) 
		print('</title>\n</head>\n<body bgcolor="#000000" text="#ffffff" link="#0088ff" vlink="#0088ff" alink="#0088ff">')
		print('<font face="Arial">\n<center>\n<h1>')
		print("    SHOTCHECK") 
		print('</h1>')

# ----------------------------------------
### Make seqHead
	def mkSeqHead(seqPath):
		print('<!DOCTYPE html>\n<html>\n<head>\n<title>')
		print("    seqCheck", seqPath) 
		print('</title>\n</head>\n<body bgcolor="#000000" text="#ffffff" link="#0088ff" vlink="#0088ff" alink="#0088ff">')
		print('<font face="Arial">\n<center>\n<h1>')
		print('    <a href="intro.htm" target="right">SEQCHECK</a>')
		print('</h1>')

# ----------------------------------------
### Make Table Start
	def mkTableStart(shotPath):
		from datetime import datetime
		myDate = datetime.now().strftime("%y%m%d-%H%M")
		print('<table border="1" width="824" cellpadding="1" cellspacing="1">')
		#print('<tr>\n    <td align="center" valign="top" colspan="2" bgcolor="#0088ff">')
		olCss.TRs()
		olCss.TDsC2b()
		print("       ", shotPath, " - ", myDate) 
		olCss.TDTR()

# ----------------------------------------
### Make Seq Table Start
	def mkSeqTableStart(seqPath):
		from datetime import datetime
		myDate = datetime.now().strftime("%y%m%d-%H%M")
		print('<table border="1" width="200" cellpadding="1" cellspacing="1">')
		print('<tr>\n    <td align="center" valign="top" colspan="2" bgcolor="#0088ff">')
		print("       ", seqPath, " <br> ", myDate) 
		olCss.TDTR()

# ----------------------------------------
	### Make Table End
	def mkTableEnd():
		print('</table>')

# ----------------------------------------
	### Make End
	def mkEnd():
		print("\n</html>")



# --------------------------------------------------------------------------------
### Report page creation


# ----------------------------------------
### Check path and create seq page
	def mkSeqPageStart(curDir):
		splitPath = curDir.split("/")
		olSeq = splitPath[-2:]
		seqPath = None
		for i in olSeq:
			if seqPath is None:
				seqPath = i
			else:
				seqPath = seqPath+"/"+i

		### Write seqReport start
		org_stdout = sys.stdout						# keep std output in variable
		with open('.web/seqReport.htm', 'w') as olSeqReport:
			sys.stdout = olSeqReport					# set output to olReport
			olHtml.mkSeqHead(seqPath)
			olHtml.mkSeqTableStart(seqPath)
			olCss.TRs
			sys.stdout = org_stdout					# Back to std output

# ----------------------------------------
### Finish seq page
	def mkSeqPageEnd():
		org_stdout = sys.stdout						# keep std output in variable
		with open('.web/seqReport.htm', 'a') as olSeqReport:
			sys.stdout = olSeqReport	
			print(olCss.TRe)
			olHtml.mkTableEnd()
			olHtml.mkEnd()
			sys.stdout = org_stdout					# Back to std output
	

# ----------------------------------------
### Check path and create shot page
	def mkPageStart(curDir):
		splitPath = curDir.split("/")
		olShot = splitPath[-3:]
		shotPath = None
		for i in olShot:
			if shotPath is None:
				shotPath = i
			else:
				shotPath = shotPath+"/"+i
		# print("shotPath :",shotPath)
		
		### Write report start
		org_stdout = sys.stdout						# keep std output in variable
		with open('report.htm', 'w') as olReport:
			sys.stdout = olReport					# set output to olReport
			olHtml.mkHead(shotPath)
			olHtml.mkTableStart(shotPath)
			sys.stdout = org_stdout					# Back to std output
			
# ----------------------------------------
### Finish shot page
	def mkPageEnd():
		org_stdout = sys.stdout						# keep std output in variable
		with open('report.htm', 'a') as olReport:
			sys.stdout = olReport	
			olCss.TRe
			olHtml.mkTableEnd()
			olHtml.mkEnd()
			sys.stdout = org_stdout					# Back to std output
		

