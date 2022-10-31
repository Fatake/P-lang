package utilities

import (
	"bufio"
	"fmt"
	"os"
)

func FileReader(fileNamePath string) (fileLines []string, err error) {
	readFile, err := os.Open(fileNamePath)

	if err != nil {
		return nil, fmt.Errorf("[!] Error al leer el archivo: %s", fileNamePath)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}

	readFile.Close()

	return fileLines, nil
}
