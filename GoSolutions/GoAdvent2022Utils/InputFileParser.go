package InputFileParser

import (
	"fmt"
	"os"
)

func makeSliceOfLinesFromFile(filename string) []string {
	fileContents, readInError := os.ReadFile(filename)
	if (readInError != nil) {
		fmt.Println("CRITICAL:"+readInError.Error())
		return []string{}
		} else {
			lines := []string{}
			for _, line := range fileContents {
				lines = append(lines, string(line))
			}
			return lines
		}
	}