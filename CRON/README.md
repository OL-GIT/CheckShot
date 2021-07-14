# PROJECT AUTOMATED CHECK

### A little script and a cron command to automate olCheckSeq. ###

## Installation :

Copy olCheckProj.sh where you want, but preferably at the root of the project.
(That way you can have one per project.)

## Requirements :
- bash and python3 must be installed on the computer that will run this script.

## Usage :

Edit olCheckProj.sh :
- Verify the path of python and olCheckSeq.py (default installation)
```
PY="/usr/bin/python3"
PG="/opt/checkShot/olCheckSeq.py"
```
- Goto line 5 and choose your project's path.
```
PROJECT="/path/to/PROJECT"
```

Edit and add the cron line to your crontab file :
- Choose the frequency of your task
- Choose the path to the script
- Choose the logFile name


## Example of job definition :
```
# 00 00 *  *  * /path/to/olCheckProj.sh &>/tmp/olCheckLog.log
```
... so olCheckProj.sh will be launched everyday at midnight.


## Reminder for cron syntax :
```
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)
# |  |  |  |  |
# *  *  *  *  *   command to be executed
```
