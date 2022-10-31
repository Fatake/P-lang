package main

import (
	"fmt"
	"os"

	cli "github.com/Fatake/P-lang/Cli"
	lex "github.com/Fatake/P-lang/Lex"
	util "github.com/Fatake/P-lang/Utilities"
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

	lex.AnalizeLex(fileLines)

}
