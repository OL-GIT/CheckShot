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

# olCheckSeq.py

- IMPORTS : Necessary modules for the script.
- VARIABLES : All the variables used in the script.
  Also imports the classes from olCheckLib.py and olHtmlLib.py
- TITLE : Will only be displayed in the console.
- INTRO : Prints the variables
- LOGS : Handles the LOGS directory and defines the active checkLog file.
  Generates the checkLog file.
- SEQUENCE HTML FRAME :
  Checks if the .web directory exists in the sequence
  If not, copy it from the installation directory.
  Defines the seqReport page
- MAIN LOOP :
  * if olCheckSeq.py is not followed by an argument, prints an error message.
  (in the console, in the main log and in the seqReport)
  * else lists the shots
  for all the files in the asked shot list :
  . if file is a directory :
    -> executes olCheckShot.py
  . if file does not exist :
  . if file is not a directory :
  . if file has wrong permissions :
  	-> prints an error message
- Close the log
- END


# olCheckShot.py

- IMPORTS : Necessary modules for the script.
- VARIABLES : All the variables used in the script.
  Also imports the classes from olCheckLib.py and olHtmlLib.py
- TITLE : Will only be displayed in the console.
- INTRO : Prints the variables
- LOGS : Handles the LOGS directory and defines the active checkLog file.
  Generates the checkLog file.
- Check passed argument
  If number of arguments is not 0 or 1, print an error message and exit.
- Functions definitions :
	* makeLog : start the shot part of the log
	* isReport : make a backup of report.htm if if already exists in the shot
	* listContent : check the content of the shot
	  . if file is .bounds, checks if it is empty (with olChecks.isEmpty)
	  . if file is report.htm, print a message
	  . if other htm file, ignore
	  . else, append file to the list to be processed
	* nbImagesVsDuration : check if number of images is correct
	  (with olChecks.myBounds and olChecks.nbImages)
	  . if .bounds does not exist, print a message
	  . if number of images is OK, print a message
	  . if number of images is not, print a message
	  If shot is not OK, set validShot to 0
	* compareNbPics : launches nbImagesVsDuration
	* numInPic : check if 2nd field is numerical
	  . if so, print a message
	  . if not, print a message and set validShot to 0
	* comparePicsWithBounds : compare the required number of images with the files in list
	  (with olChecks.myBounds)
	  . if bounds is missing or incorrect, print a message
	  . else, make a list of possible missing images
	  If there are missing images, set validShot to 0
	* verifyExts : verify that the file extensions are correct (ext variable)
	  . check the number of fields (must be 3)
	  . check if the extension is correct
	  . print messages and write to logs
	* verifyPics : check the size of the files
	  . if empty pics are found, add them to the empty list
	  . print messages and write to logs
	* isShotValid : generate the conclusion
	  . if validShot is still 1, shot is validated
	  . if validShot is 0, shot is wrong	  
	  . print messages and write to logs
	* detailPics : print a full list of the files
	  . uid + gid + size + file
	  . add this list in report.htm
	* thisIsTheEnd : print the end of the checkShot
- EXECUTION : 
	* Calls the functions
	  . olTitle, olIntro, olLogs
	* Define the current directory and the variables used by the fonctions
	  . define validShot to 1
	* Define the HTML report name and calls the makeLog function
	* Execute the checks functions
	  . olHtml.mkPageStart
	  . checkArgv, listContent, compareNbPics, numInPic, comparePicsWithBounds,
	    verifyExts, verifyPics, isShotValid, detailPics
- END : Finish the report.

