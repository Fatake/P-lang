package main

import (
	"fmt"
	"os"

	cli "github.com/Fatake/P-lang/cli"
	lex "github.com/Fatake/P-lang/lex"
	util "github.com/Fatake/P-lang/utilities"
)

func main() {
	lex_filePath, err := cli.GetArgs()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	fileLines, err := util.FileReader(lex_filePath)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	_, err = lex.AnalizeLex(fileLines, true)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

}
