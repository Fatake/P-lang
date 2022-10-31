package Lex

import (
	"fmt"
	"strconv"
)

func AnalizeLex(fileLines []string) (string, error) {
	//len(fileLines)
	tam := strconv.Itoa(len(fileLines))
	fmt.Println("[i] Numero de Lineas: " + tam)
	return "ok", nil
}
