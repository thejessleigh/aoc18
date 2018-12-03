#!/bin/bash

echo "\`python3 2_1.py\` 100 times"
time for i in {1..100}; do python3 2_1.py; done
echo "\`go run 2_1.go\` 100 times"
time for i in {1..100}; do go run 2_1.go; done
echo "go build"
go build 2_1.go
echo "\`./2_1\` 100 times"
time for i in {1..100}; do ./2_1; done


echo "\`python3 2_2.py\` 100 times"
time for i in {1..100}; do python3 2_2.py; done