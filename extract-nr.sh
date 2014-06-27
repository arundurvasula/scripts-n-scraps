#!/bin/bash
#This script will extract all parts of the nr database from NCBI
# couldn't generate the array because NCBI uses double digits!
nums=(00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23)

for i in ${nums[*]}
do
	echo "untaring nr."$i".tar.gz"	
	tar -xzvf nr.$i.tar.gz &> nr.$i.tar.log
done
