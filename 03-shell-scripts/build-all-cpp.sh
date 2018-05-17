#!/bin/bash

set -x

for f in *.cpp
do
    g++ $f -o ${f%.cpp}
done
