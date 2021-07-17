# CheckShot v1.0 Architecture
### ... Notes about the scripts ... ###

## Architecture :

In the SOURCES directory, there are 
- 2 python scripts :
	* olCheckSeq.py
	* olCheckShot.py
- 2 directories :
	* olCheckLibs/
		* olCheckLib.py
		* olHtmlLib.py
	* olCheckWebRef/

olCheckSeq.py launches olCheckShot.py shot by shot.
Both call functions in olCheckLib.py and olHtmlLib.py


## Operation :

### olCheckSeq.py

- IMPORTS : Necessary modules for the script.

- VARIABLES : All the variables used in the script.
  Also imports the classes from olCheckLib.py and olHtmlLib.py

- TITLE : Will only be displayed in the console.

- INTRO : Prints the variables

- LOGS : Handles the LOGS directory and defines the active checkLog file.
  Generates the checkLog file.

- SEQUENCE HTML FRAME :
  Checks if the .web directory exists in the sequence
  If not, copies it from the installation directory.
  Defines the seqReport page

- MAIN LOOP :
  * if olCheckSeq.py is not followed by an argument, prints an error message.
  (in the console, in the main log and in the seqReport)
  * else lists the shots
  for all the files in the asked shot list :
  - if file is a directory :
    - executes olCheckShot.py
  - if file does not exist :
  	- prints an error message
  - if file is not a directory :
  	- prints an error message
  - if file has wrong permissions :
  	- prints an error message

- Closes the log

- END


### olCheckShot.py

- IMPORTS : Necessary modules for the script.

- VARIABLES : All the variables used in the script.
  Also imports the classes from olCheckLib.py and olHtmlLib.py

- TITLE : Will only be displayed in the console.

- INTRO : Prints the variables

- LOGS : Handles the LOGS directory and defines the active checkLog file.
  Generates the checkLog file.

- Checks passed argument
  If number of arguments is not 0 or 1, prints an error message and exit.

- Functions definitions :
	* makeLog : starts the shot part of the log
	* isReport : makes a backup of report.htm if if already exists in the shot
	* listContent : checks the content of the shot
	  - if file is .bounds, checks if it is empty (with olChecks.isEmpty)
	  - if file is report.htm, prints a message
	  - if other htm file, ignores
	  - else, appends file to the list to be processed
	* nbImagesVsDuration : checks if number of images is correct
	  (with olChecks.myBounds and olChecks.nbImages)
	  - if .bounds does not exist, prints a message
	  - if number of images is OK, prints a message
	  - if number of images is not, prints a message
	  If shot is not OK, sets validShot to 0
	* compareNbPics : launches nbImagesVsDuration
	* numInPic : checks if 2nd field is numerical
	  - if so, prints a message
	  - if not, prints a message and set validShot to 0
	* comparePicsWithBounds : compares the required number of images with the files in list
	  (with olChecks.myBounds)
	  - if bounds is missing or incorrect, prints a message
	  - else, makes a list of possible missing images
	  If there are missing images, sets validShot to 0
	* verifyExts : verifies that the file extensions are correct (ext variable)
	  - checks the number of fields (must be 3)
	  - checks if the extension is correct
	  - prints messages and write to logs
	* verifyPics : checks the size of the files
	  - if empty pics are found, adds them to the empty list
	  - prints messages and writes to logs
	* isShotValid : generates the conclusion
	  - if validShot is still 1, shot is validated
	  - if validShot is 0, shot is wrong	  
	  - prints messages and writes to logs
	* detailPics : prints a full list of the files
	  - uid + gid + size + file
	  - adds this list in report.htm
	* thisIsTheEnd : prints the end of the checkShot

- EXECUTION : 
	* Calls the functions
	  - olTitle, olIntro, olLogs
	* Defines the current directory and the variables used by the fonctions
	  - define validShot to 1
	* Defines the HTML report name and calls the makeLog function
	* Executes the checks functions
	  - olHtml.mkPageStart
	  - checkArgv, listContent, compareNbPics, numInPic, comparePicsWithBounds,
	    verifyExts, verifyPics, isShotValid, detailPics

- END : Finish the report.


### olCheckLib.py

- IMPORTS

- VARIABLES

- class olCol
  * Colors and styles for the console display

- class olPr
  * Lines for the console display

- class olReports
  * Table for the report

- class olChecks
  * isEmpty : checks if .bounds file is empty
  * isEmptyHtml : checks if .bounds file is empty and writes in report
  	- calls reportStart and reportEnd
  * myStart : finds start bound in .bounds file
  	- returns mystart
  * myEnd : finds end bound in .bounds file
   - returns myend
  * myBounds : defines mystart, myend and duration variables
		- if 2 values found, assigns these values to mystart and myend
		- if not, assigns 0 to mystart and myend
		- il values ar not integers, assigns 0
		- returns mystart, myend and duration variables
  * nbImages : counts the images
		- returns nbPics


### olHtmlLib.py

- IMPORTS

- class olCss : HTML tags
	* Styles : Bs, Be, Is, Ie, Us, Ue, BR, HR, LSs, LSe, CEN
	* Colors : cGs, cYs, cRs, cBs, Fe
	* Fonts : F3, F4, F5, Fe
	* Tables : TR*, TD*
	* Listing : LST (takes value "listing", called by olCheckShot.py)

- class olHtml : HTML pages and tables management
	* mkHead : writes HEAD of checkShot page
	* mkSeqHead : writes HEAD of checkSeq page
	* mkTableStart : writes the beginning of checkShot table
	* mkSeqTableStart : writes the beginning of checkSeq table
	* mkTableEnd : writes ending of table
	* mkEnd : writes ending of HTML page
	* mkSeqPageStart : writes the beginning of checkSeq page
		- checks the shot path
		- writes in seqReport.htm
		- calls mkSeqHead and mkSeqTableStart to start seq page and table
	* mkSeqPageEnd : writes the end of checkSeq page
		- writes in seqReport.htm
		- calls mkTableEnd and mkEnd to end table and page
	* mkPageStart : writes the beginning of checkShot page
		- checks the shot path
		- writes in report.htm
		- calls mkHead and mkTableStart to start shot page and table
	* mkPageEnd : 
		- writes in report.htm
		- calls mkTableEnd and mkEnd to end shot table and page

