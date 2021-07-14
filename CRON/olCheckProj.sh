#! /bin/bash -f

PY="/usr/bin/python3"
PG="/opt/checkShot/olCheckSeq.py"
PROJECT="/path/to/PROJECT"

cd $PROJECT
list=`ls`
listSeq=""

for i in $list
do
	if [[ ${i::1} == "S" ]]
	then
		listSeq="$listSeq $i"
	fi
done
echo $listSeq

for Seq in $listSeq
do
	cd $PROJECT/$Seq
	listPlans=`ls | grep P`
	# echo $listPlans
	$PY $PG $listPlans
done


exit 0



