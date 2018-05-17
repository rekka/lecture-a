#!/bin/bash

# function that computes the length of the input string
function len {
    echo -n -e "$1" | wc -c | tr -d '[:space:]'
}

# call it as a command

l=$(len Hello)

# careful with spaces
input="my \nstring"
l=$(len "$input")
echo "I got: $l = ${#input}"
