#!/bin/bash

set -e

usage () {
    echo "latex-docker usage (make sure you have defined the alias):"
    echo "latex-docker <file.tex>: compile the file"
    echo "latex-docker clean: clean the working environment"
    echo "latex-docker help: print this message"
    echo "latex-docker version: get the code version"
}

# Parse command line argument
if [[ "$#" -ne 1 ]]; then
    usage
    exit 1
elif [[ $1 == "clean" ]]; then
    latexmk -C
    exit $?
elif [[ $1 == "version" ]]; then
    echo "latex-docker version 0.1.4"
    exit 0
elif [[ $1 == *.tex ]]; then
    latexmk -pdf $1
    exit $?
else
    usage
    exit 1
fi
