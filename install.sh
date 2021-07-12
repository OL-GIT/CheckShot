#! /bin/sh -f

echo -e "# -------------------------------------------------------- #"
echo -e "# \033[1mCHECKSHOT INSTALLATION                            210712\033[0m #"
echo -e "# -------------------------------------------------------- #"

pgmDir="/opt/checkShot"
pgmBin="olCheckSeq.py olCheckShot.py"
pgmLib="olCheckLibs olCheckWebRef"
valid="1"
copyOK="1"

# --------------------------------------
MISSING()
{
echo -e "# -------------------------------------------------------- #"
echo -e "#                     \033[7m*** WARNING ***\033[0m                      #"
echo -e "# -------------------------------------------------------- #"
echo -e "Some files seem to be missing in current directory"
echo -e "When downloading and unzipping the installation archive,"
echo -e "the following files and directories should be present :"
echo -e "\033[1molCheckSeq.py olCheckShot.py and olCheckLibs/ olCheckWebRef/ \033[0m"
echo -e "# -------------------------------------------------------- #"
echo -e "You could try again to import the complete archive :"
echo -e "\033[1mgit clone https://github.com/OL-GIT/CheckShot.git\033[0m"
echo -e "or download the compressed archive :"
echo -e "\033[1mhttps://github.com/OL-GIT/CheckShot/archive/refs/heads/main.zip\033[0m"
}

# --------------------------------------
USAGE()
{
echo -e "\033[1mYou should consider adding" $pgmDir "to your PATH\033[0m"
echo -e "The program can now be launched from your project directory."
echo -e ""
echo -e "- At sequence level :"
echo -e "$ cd <PROJECT>/<SEQUENCE>"
echo -e "  $ "$pgmDir"/olCheckSeq.py <shotName>"
echo -e "  $ "$pgmDir"/olCheckSeq.py <shotName> <shotName> <shotName>"
echo -e "  $ "$pgmDir"/olCheckSeq.py *"
echo -e ""
echo -e "- At shot level :"
echo -e "$ cd <PROJECT>/<SEQUENCE>/<SHOT>"
echo -e "  $ "$pgmDir"/olCheckShot.py"
echo -e ""
}

# --------------------------------------
INSTOK()
{
echo -e ""
echo -e "                 \033[7m*** INSTALLATION DONE ***\033[0m"
echo -e ""
echo -e "# -------------------------------------------------------- #"
}

# --------------------------------------
INSTNO()
{
echo -e ""
echo -e "                \033[7m*** INSTALLATION FAILED ***\033[0m"
echo -e ""
echo -e "# -------------------------------------------------------- #"
echo -e "Maybe you should have a look at your /opt directory ..."
echo -e "You can also try to copy the files manually."
echo -e "Files to copy :"
echo -e "olCheckSeq.py olCheckShot.py olCheckLibs/ olCheckWebRef/"
}


# --------------------------------------
### CHECK IF FILES AND DIRS EXIST
if test -d $pgmDir
then
	echo  "Install directory" $pgmDir "already exists."
else
	echo  "Install directory" $pgmDir "does not exist, created it."
	mkdir $pgmDir
fi

for bin in $pgmBin
do
	if [ ! -f $bin ]
	then
		valid="0"
	fi		
done

for lib in $pgmLib
do
	if [ ! -d $lib ]
	then
		valid="0"
	fi		
done


# --------------------------------------
### INSTALLATION
if test $valid = "1"
then
	cp olCheckSeq.py $pgmDir
	cp olCheckShot.py $pgmDir
	cp -r olCheckLibs $pgmDir
	cp -r olCheckWebRef $pgmDir
	chmod 754 olCheckSeq.py olCheckShot.py olCheckLibs olCheckWebRef
else
	MISSING
	exit 0
fi


# --------------------------------------
### CHECK IF INSTALLATION SUCCEEDED
for bin in $pgmBin
do
	if [ ! -f "$pgmDir/$bin" ]
	then
		echo $pgmDir/$bin "is missing"
		copyOK=0
	fi		
done

for lib in $pgmLib
do
	if [ ! -d "$pgmDir/$lib" ]
	then
		echo $pgmDir/$lib "is missing"
		copyOK=0
	fi		
done


# --------------------------------------
### END MESSAGE - USAGE OR REINSTALL SUGGESTION
if test $copyOK = "1"
then
	INSTOK
	USAGE
else
	INSTNO
fi

