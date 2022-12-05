package Day1

import (
	InputFileParser "GoSolutions/GoAdvent2022Utils"
	"fmt"
	"strconv"
)

func Part1() string {
	// Trying to find the elf with the most calories, aka max in the list
	inputLines := InputFileParser.MakeSliceOfLinesFromFile("/home/fossil/Documents/git-sandbox/Advent-Of-Code-2022/Day1/input.txt")
	currMax := 0
	currElfCalories := 0
	for _, line := range inputLines {
		if line == "" || line == "\n" {
			if currElfCalories > currMax {
				currMax = currElfCalories
			}
			currElfCalories = 0
		} else {
			calories, intParseError := strconv.Atoi(line)
			if intParseError != nil {
				fmt.Println("CRITICAL: " + intParseError.Error())
				break
			} else {
				currElfCalories += calories
			}
		}
	}

	return fmt.Sprintln("Most calories packed: " + fmt.Sprint(currMax))
}

func Part2() string {
	inputLines := InputFileParser.MakeSliceOfLinesFromFile("/home/fossil/Documents/git-sandbox/Advent-Of-Code-2022/Day1/input.txt")
	elves := []int{}
	topThreeElvesTotal := 0
	currElfCalories := 0
	for _, line := range inputLines {
		if line == "" || line == "\n" {
			elves = append(elves, currElfCalories)
			currElfCalories = 0
		} else {
			calories, intParseError := strconv.Atoi(line)
			if intParseError != nil {
				fmt.Println("CRITICAL: " + intParseError.Error())
				break
			} else {
				currElfCalories += calories
			}
		}
	}
	currMaxElf := 0
	currMaxElfIdx := 0
	for j := 0; j < 3; j++ {
		for idx, elf := range elves {
			if elf > currMaxElf {
				currMaxElf = elf
				currMaxElfIdx = idx
			}
		}
		topThreeElvesTotal += currMaxElf
		elves[currMaxElfIdx] = 0
		currMaxElf = 0
		currMaxElfIdx = 0
	}
	return fmt.Sprintln("Most calories packed by top three elves: " + fmt.Sprint(topThreeElvesTotal))
}
