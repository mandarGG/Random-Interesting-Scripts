#!/bin/bash
# Train number is the train number for which you want to check availabilty and can be checked at erail.in
train_no=57563
#it is Initial Station of Your Journey
it=HYB
#ft is Destination station of your journey
ft=NED
#class is your class of travel, ex: SL for sleeper 
class=SL
# Date is your date of travel
date=6
#Month is your month of travel(1-12)
month=5
#av is the limit,if availability goes below av desktop notification will be shown and mail will be sent
av=20
export av 
curl 'http://198.50.238.219/AVL_Request?Key='$train_no'_'$it'_'$ft'_'$class'_GN_'$date'-'$month'~&Cache=1&callback=jQuery1102014319540465779446_1454481487908&_=1454481487911' -H 'Host: 198.50.238.219' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'DNT: 1' -H 'Referer: http://erail.in/' -H 'Connection: keep-alive'>answer
bash ./filtererail.sh

