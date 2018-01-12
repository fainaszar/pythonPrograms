#!/bin/bash
$firstRow = true
while IFS="," read line
do
	if $firstRow
	then
		echo "**********************************************"
		echo $line | tr ',' '\t'
		echo "**********************************************"
		
	else
		echo $line | tr ',' '\t'
	fi
done < $1

