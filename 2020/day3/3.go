package main

import (
  "fmt"
  "os"
  "strings"
)

func checkSlope(m []string, r int, d int) int {
  row, col := 0, 0
  colmod := len(m[0])
  treecount := 0
  for row < len(m)-1 {
    row += d
    col += r
    col = col % colmod
    if m[row][col] == '#' {
      treecount++
    }
  }
  return treecount
}
func main() {
  fname := "input.txt"
  fbytes, _ := os.ReadFile(fname)
  contents := string(fbytes)
  lines := strings.Split(contents, "\n")
  lines = lines[:len(lines)-1]
  a1 := checkSlope(lines, 1, 1)
  a2 := checkSlope(lines, 3, 1)
  a3 := checkSlope(lines, 5, 1)
  a4 := checkSlope(lines, 7, 1)
  a5 := checkSlope(lines, 1, 2)
  fmt.Println(a1*a2*a3*a4*a5)
}
