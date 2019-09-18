#!/bin/bash
clear
ans=`awk -F '^' '{print $3}' answer`
echo $ans > myfile
grep -q "AVAILABLE" myfile
state=`echo $?`

if [[ $state -eq 0 ]]
then
	myans=`cat myfile | awk -F 'E' '{print $2}'`
	if [[ $myans -le $av ]]
	then
		echo "Worry! Availability is '$myans'"
		notify-send "Worry,availabilty is low,'$myans'"
		mail -s "Low availabilty number" mandar.gondhalekar@students.iiit.ac.in < ./myfile 
	else
		echo "Availability is '$myans'"
	fi
fi
grep -q "RAC" myfile
state1=`echo $?`
if [[ $state1 -eq 0 ]]
then
	 #myans= `cat myfile` | `awk -F '' '{print $2}'`
	 echo "Sorry,no seats available.The current state is:'$ans'"
	 notify-send "Sorry, seats not available,status :'$ans'"
fi
grep -q "WL" myfile
state2=`echo $?`
if [[ $state2 -eq 0 ]]
then
	 #myans= `cat myfile` | `awk -F '' '{print $2}'`
	 echo "Sorry,ticket is in waiting list :'$ans'"
	 notify-send "Sorry, seats not available,status :'$ans'"
fi


