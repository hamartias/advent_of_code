package main

import (
  "testing"
)

func TestSeatID(t *testing.T) {
  got := calculateSeatID(1, 2)
  if got != 10 {
    t.Errorf("Not 10")
  }
}

func TestSeatString(t *testing.T) {
  inputs := []string{"FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"}
  expRows := []int{44, 70, 14, 102}
  expCols := []int{5, 7, 7, 4}
  for i, s := range inputs {
    gr, gc := parseSeatString(s)
    if gr != expRows[i] {
      t.Errorf("Wrong row %d != %d, test %d", gr, expRows[i], i)
    }
    if gc != expCols[i] {
      t.Errorf("Wrong col %d != %d, test %d", gc, expCols[i], i)
    }
  }
}
