package main

import (
    "strings"
    "fmt"
    "io/ioutil"
    // "reflect"
)

func containsVal(m map[string]int, v int)(bool) {
    for _, x := range m{
        if x == v {
            return true
        }
    }
    return false
}

func checksum(x string)(int) {
    two := 0
    three := 0
    ids := strings.Split(x, "\n")
    for i := 0; i < len(ids); i++ {
        counter := make( map[string]int )
        s := strings.Split(ids[i], "")
        for _, l := range s {
            counter[l]++
        }
        if containsVal(counter, 2) {
            two++
        }
        if containsVal(counter, 3) {
            three++
        }
    }
    return two * three
}

func main() {
    f, err := ioutil.ReadFile("input.txt")
    if err != nil {
        panic(err)
    }
    fmt.Println(checksum(string(f)))
}