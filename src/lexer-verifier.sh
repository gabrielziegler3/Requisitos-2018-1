#!/bin/bash

read -p "Enter Lexico.md dir: " dir

file="Léxico.md"

lexer_files=$(grep -E -o "\[(.+?)\]" $dir$file | sed 's/\[\|\]//g' | sed 's/$/.md/g' | sed 's/ /-/g')

echo -e "Checking Lexicos...\n"

sleep .7

for i in "$lexer_files"
do
	echo -e "1- Verifying Pattern\n"
	echo -e "\n\n\n"

	grep --color "Sinônimos" -A 1 $dir$i
	read -p "Press enter to continue"

	echo -e "\n\n\n"
	grep --color "Noção" -A 1 $dir$i
	read -p "Press enter to continue"

	echo -e "\n\n\n"
	grep --color "Impacto" -A 1 $dir$i
	read -p "Press enter to continue"
done

