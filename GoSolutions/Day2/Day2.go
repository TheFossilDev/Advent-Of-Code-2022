package Day2

import (
	InputFileParser "GoSolutions/GoAdvent2022Utils"
)

func Part1() string {
	lines := InputFileParser.MakeSliceOfLinesFromFile("/Users/colewestbrook/Projects/Advent-Of-Code-2022/Day2/input.txt")
	throwPoints := map[string]int{
		"X": 1, // Rock
		"Y": 2, // Paper
		"Z": 3, // Scissors
	}
	winningMatches := []string{
		"A Y",
		"B Z",
		"C X",
	}
	losingMatches := []string{
		"A Z",
		"B X",
		"C Y",
	}
	drawMatches := []string{
		"A X",
		"B Y",
		"C Z",
	}

}
