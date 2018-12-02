#!/bin/bash

echo "\`python3 1_1.py\` 100 times"
time for i in {1..100}; do python3 1_1.py; done
echo "\`go run 1_1.go\` 100 times"
time for i in {1..100}; do go run 1_1.go; done
echo "go build"
go build 1_1.go
echo "\`./1_1\` 100 times"
time for i in {1..100}; do ./1_1; done

echo "\`python3 1_2.py\` 100 times"
time for i in {1..100}; do python3 1_2.py; done
echo "\`go run 1_2.go\` 100 times"
time for i in {1..100}; do go run 1_2.go; done
echo "go build"
go build 1_2.go
echo "\`./1_2\` 100 times"
time for i in {1..100}; do ./1_2; done