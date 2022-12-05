package InputFileParser

import (
	"fmt"
	"os"
	"strings"
)

func MakeSliceOfLinesFromFile(filename string) []string {
	fileContents, readInError := os.ReadFile(filename)
	if readInError != nil {
		fmt.Println("CRITICAL:" + readInError.Error())
		return []string{}
	} else {
		lines := strings.Split(string(fileContents), "\n")
		for _, line := range fileContents {
			lines = append(lines, string(line))
		}
		return lines
	}
}
