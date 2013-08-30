#!/bin/bash

for input in input/*; do
  echo "==================="
  echo -en "\e[33mTest #${input##*/}: "
  echo -e "\e[35m./main.py $input\e[0m"

  ./main.py $input

  output=output/${input##*/}
  if [[ -s $output ]]; then
    echo -e "\e[33mExpected output:\e[32m"
    cat $output 
    echo -e "\e[0m"
  fi
done
