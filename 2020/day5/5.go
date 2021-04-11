package main

import (
  "fmt"
  "bufio"
  "os"
)

func calculateSeatID(row, col int)  int {
  return row*8 + col
}

func parseSeatString(s string) (int, int) {
  low, high := 0, 127
  for i := 0; i < 7; i++ {
    if s[i] == 'F' {
      high = low + ((high - low) / 2)
    } else {
      low = low + ((high - low) / 2) + 1
    }
  }
  row := low
  low, high = 0, 7
  for i := 7; i < 10; i++ {
    if s[i] == 'L' {
      high = low + ((high - low) / 2)
    } else {
      low = low + ((high - low) / 2) + 1
    }
  }
  col := low
  return row, col
}


func main() {
  fmt.Println("Start.")
  file, _ := os.Open("./input.txt")
  defer file.Close()

  scanner := bufio.NewScanner(file)
  max := 0

  var seats [128][8]int
  for scanner.Scan() {
    s := scanner.Text()
    row, col := parseSeatString(s)
    seats[row][col] = 1
    id := calculateSeatID(row, col)
    if id > max {
      max = id
    }
  }
  fmt.Println(max)
  missing := make([]int, 0)
  for r := 0; r < 128; r++ {
    for c := 0; c < 8; c++ {
      if seats[r][c] == 0 {
        missing = append(missing, calculateSeatID(r, c))
      }
    }
  }
  for i := 1; i < len(missing); i++ {
    if missing[i-1]+1 != missing[i] && missing[i+1]-1 != missing[i] {
      fmt.Println(missing[i])
    }
  }
}
