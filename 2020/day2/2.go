
package main

import (
  "bufio"
  "log"
  "os"
  "strings"
  "fmt"
  "strconv"
)

func countCharacters(input *string) map[rune]int {
  ret := make(map[rune]int)
  for _, b := range(*input) {
    ret[b]++
  }
  return ret
}

type pwEntry struct {
  lower int
  upper int
  char rune
  password string
}

func parseEntry(input string) *pwEntry {
  split := strings.Split(input, ":")
  bounds := strings.Split(split[0], "-")
  upper_split := strings.Split(bounds[1], " ")
  char := upper_split[1][0]
  lower, err := strconv.Atoi(bounds[0])
  if err != nil {
    log.Fatal(err)
  }
  upper, err := strconv.Atoi(upper_split[0])
  if err != nil {
    log.Fatal(err)
  }

  for {
    if (len(split[1]) == 0 || split[1][0] != ' ') {
      break
    }
    split[1] = split[1][1:]
  }

  ret := new(pwEntry)
  ret.lower = lower
  ret.upper = upper
  ret.char = rune(char)
  ret.password = split[1]
  return ret
}

func pwIsValidCount(entry *pwEntry) bool {
  charCount := countCharacters(&entry.password)
  pwcharCount, has_char := charCount[entry.char]
  if has_char {
    return (entry.lower <= pwcharCount && entry.upper >= pwcharCount)
  } else {
    return entry.lower == 0
  }
}

func pwIsValidPlacement(entry *pwEntry) bool {
  inplace := 0
  pwlength := len(entry.password)
  if entry.lower <= pwlength {
    if rune(entry.password[entry.lower-1]) == entry.char {
      inplace++
    }
  }
  if entry.upper <= pwlength {
    if rune(entry.password[entry.upper-1]) == entry.char {
      inplace++
    }
  }
  fmt.Println(pwlength, entry.password, entry.lower, entry.upper, entry.char)
  fmt.Println(entry, inplace)
  return inplace == 1
}

func main() {
  test_file := "day2.input"
  file, err := os.Open(test_file)
  if err != nil {
    log.Fatal(err)
  }
  defer file.Close()

  scanner := bufio.NewScanner(file)
  countIsCorrect := 0
  placementIsCorrect := 0
  for scanner.Scan() {
    line := scanner.Text()
    parsed := parseEntry(line)
    if pwIsValidCount(parsed) {
      countIsCorrect++
    }
    if pwIsValidPlacement(parsed) {
      fmt.Println("correct, ", parsed)
      placementIsCorrect++
    }
  }

  if err := scanner.Err(); err != nil {
    log.Fatal(err)
  }
  fmt.Println(countIsCorrect)
  fmt.Println(placementIsCorrect)
}
