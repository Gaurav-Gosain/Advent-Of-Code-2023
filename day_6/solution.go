package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Read input from file
	fileContent, err := os.ReadFile("in.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	s := string(fileContent)

	timeStr, distanceStr := parseInput(s)

	timeSlice := parseIntSlice(timeStr)
	distanceSlice := parseIntSlice(distanceStr)

	p1 := 1

	for i := 0; i < len(timeSlice); i++ {
		t := timeSlice[i]
		d := distanceSlice[i]
		p1 *= getValue(t, d)
	}

	fmt.Println("Part 1:", p1)

	t, _ := strconv.Atoi(strings.Join(timeStr, ""))
	d, _ := strconv.Atoi(strings.Join(distanceStr, ""))

	p2 := getValue(t, d)

	fmt.Println("Part 2:", p2)
}

func parseInput(s string) ([]string, []string) {
	lines := strings.Split(s, "\n")
	time := strings.Fields(strings.Split(lines[0], ":")[1])
	distance := strings.Fields(strings.Split(lines[1], ":")[1])
	return time, distance
}

func parseIntSlice(s []string) []int {
	var result []int
	for _, v := range s {
		num, _ := strconv.Atoi(v)
		result = append(result, num)
	}
	return result
}

func getFirst(t, d int) int {
	for i := 0; i < t; i++ {
		x := (t - i) * i
		if x > d {
			return i
		}
	}
	return 0
}

func getLast(t, d int) int {
	for i := t - 1; i > 0; i-- {
		x := (t - i) * i
		if x > d {
			return i
		}
	}
	return 0
}

func getValue(t, d int) int {
	return getLast(t, d) - getFirst(t, d)
}
