# CheckShot
### Verifies sub-directories integrity of a post-production project. ###


## Scenario :

  Images are rendered on computers/renderfarms and dropped on a server.
  As the tree structure can be different in each project, SeqCheck
  will only be run at the sequence level. (Sequence/Shots/Images)


## Main purpose :

  Check if the shots directories contain :
- The file (.bounds) identifying the required start/end bounds of the shot.
- The adequacy with the number of images found.
- Files with the correct number of fields (name.number.extension)
- Files with the correct numerical field (4 digits, ie ####)
- Files with the correct extension
- Files with non-zero weight
- All the requested images, searching for missing files


## Usage :

  The tool is usable in a punctual case as well as on daily/hourly checks.
It can be launched by a cron task, or a customized script.

- If launched manually, the script generates a human readable report,
that highlights the possible mistakes found.
It can be launched shot by shot, or more globally in a sequence.

- If automated, the user will be able to check the web version
of the dump, which can be seen on any device that handles http pages.

- In both cases, it will also generate a log report that would rather
be intended for system administrators.

The web-tool is oriented for post-production supervisors, who can quickly
glance at shots in progress, see the possible errors, or simply check
the calculation progress.


## Requirements :

Python3 must be installed on the server if automated, 
or on the client in case of a network-shared usage.

It runs on Linux and Windows (with cygwin).

Needed in the installation directory :
  * olCheckSeq.py
  * olCheckShot.py
  
and the subDirectories :
  * olCheckLibs/
  * olCheckWebRef/



## Installation :

Go to the place where you want to install the program.

- Download the .zip archive of the program [here](https://github.com/OL-GIT/CheckShot/archive/refs/heads/main.zip).

or type :

```
> git clone https://github.com/OL-GIT/CheckShot.git
```


## Method :

*olCheckSeq.py* can be run at the sequence level.
You need to specify the name of the shots you want to check :
```
> python3 olCheckSeq.py P1 P2 P3
> python3 olCheckSeq.py P*
> python3 olCheckSeq.py *
```
*olCheckShot.py* can be run at the shot level.
It does not need any argument :
```
> python3 olCheckShot.py
```


## Results :

- If launched manually, checkSeq and checkShot will display the results in the console.
This method is recommended for punctual needs.

- The HTML minisite will be found in $PROJECT/$SEQUENCE/.web/index.htm
It will display seqreport.htm in the left frame.
The shot reports are written in $PROJECT/$SEQUENCE/$SHOT/report.htm and will we displayed in the right frame of the minisite.

- The global log files will be found in $PROJECT/LOGS/ (olCheckSeqlog.DATE-TIME.txt)


