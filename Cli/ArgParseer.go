package cli

import (
	"flag"
	"fmt"
	"os"
)

const NUMBER_SUBCOMMANDS int = 2

func GetArgs() (string, error) {
	// Sub Comandos
	lexCommand := flag.NewFlagSet(SUB_COMMAND_LEX, flag.ExitOnError)

	// Count subcommand flag pointers
	lex_filePath := lexCommand.String("file", "", "Ruta del archivo a analizar. (Required)")

	// Verify that a subcommand has been provided
	// os.Arg[0] is the main command
	// os.Arg[1] will be the subcommand
	if len(os.Args) < 2 {
		errorCommand()
		return "", fmt.Errorf("[!] No se dio un comando")
	}

	// Switch on the subcommand
	// Parse the flags for appropriate FlagSet
	// FlagSet.Parse() requires a set of arguments to parse as input
	// os.Args[2:] will be all arguments starting after the subcommand at os.Args[1]
	switch os.Args[1] {
	case SUB_COMMAND_HELP:
		var commands []*flag.FlagSet
		commands = append(commands, lexCommand)
		printHelp(commands)
		os.Exit(0)

	case SUB_COMMAND_VERSION:
		printVersion()
		os.Exit(0)

	case SUB_COMMAND_LEX:
		lexCommand.Parse(os.Args[2:])

	default:
		errorCommand()
		return "", fmt.Errorf("[!] Comando desconocido")
	}

	if lexCommand.Parsed() {
		// Required Flags
		if *lex_filePath == "" {
			lexCommand.PrintDefaults()
			return "", fmt.Errorf("[!] No se dio nombre del archivo")
		}

		return *lex_filePath, nil
	}
	return "", nil
}

func printVersion() {
	fmt.Println("[i] Version 0.1.0")
}

func printHelp(commands []*flag.FlagSet) {
	fmt.Println("P-Lang Compiler")
	for _, command := range commands {
		fmt.Println("Comando: " + command.Name())
		command.PrintDefaults()
	}
}

func errorCommand() {
	fmt.Println("[!] Utilice el comando <help> para ver las opciones")
	fmt.Println("Ejemplo: ./p-lang help")
}
