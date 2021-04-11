
package main

import (
  "bufio"
  "fmt"
  "log"
  "os"
  "strconv"
)

func two_sum(numbers []int) int {
  target := 2020
  complements := make(map[int]int)
  for _, num := range numbers {
    complements[target-num] = num
  }

  for _, num := range numbers {
    elem, has_comp := complements[num]
    if has_comp {
      return elem * complements[elem]
    }
  }

  return 0;
}

func three_sum(numbers []int) int {
  result := 0
  for i, n1 := range numbers {
    for j, n2 := range(numbers[i+1:]) {
      for _, n3 := range(numbers[j+1:]) {
        if n1 + n2 + n3 == 2020 {
          return n1 * n2 * n3
        }
      }
    }
  }
  return result
}

func main() {
  test_file := "day1.input"
  file, err := os.Open(test_file)
  if err != nil {
    log.Fatal(err)
  }
  defer file.Close()

  scanner := bufio.NewScanner(file)
  var numbers []int;
  for scanner.Scan() {
    num, err := strconv.Atoi(scanner.Text())
    if err != nil {
      log.Fatal(err)
    }
    numbers = append(numbers, num)
  }

  if err := scanner.Err(); err != nil {
    log.Fatal(err)
  }

  fmt.Println(two_sum(numbers));
  fmt.Println(three_sum(numbers));
}
