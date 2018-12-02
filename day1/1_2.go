package main

import (
    "io/ioutil"
    "strconv"
    "container/ring"
    "strings"
)

func dup(x string)(sum int) {
    list := strings.Split(x, "\n")
    r := ring.New(len(list))
    seen := map[int]bool{0: true}
    for i := 0; i < r.Len(); i++ {
        num, err := strconv.Atoi(list[i])
        if err != nil {
            panic(err)
        }
        r.Value = num
        r = r.Next()
    }
    for true {
        sum += r.Value.(int)
        if (seen[sum] == true) {
            return sum
        }
        seen[sum] = true
        r = r.Next()
    }
    return
}

func main() {
    f, err := ioutil.ReadFile("input1.txt")
    if err != nil {
        panic(err)
    }
    dup(string(f))
}