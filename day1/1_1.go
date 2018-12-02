package main

import (
    "bufio"
    // "fmt"
    "os"
    "strconv"
)

func freq(f *os.File)(sum int) {
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        i, err := strconv.Atoi(scanner.Text())
        if err != nil {
            panic(err)
        }
        sum += i
    }
    return
}

func main() {
    f, err := os.Open("input1.txt")
    if err != nil {
        panic(err)
    }
    freq(f)
    // fmt.Println(freq(f))
}