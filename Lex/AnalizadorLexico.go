package lex

import (
	"fmt"
	"strconv"
	"strings"

	words "github.com/Fatake/P-lang/lex/reserv"
)

const (
	ACTION_DO_NOTHING              int = 0
	ACTION_IGNORE_SINGE            int = 1
	ACTION_IGNORE_LINE             int = 2
	ACTION_OPEN_PARENTHESES        int = 3
	ACTION_CLOSE_PARENTHESES       int = 4
	ACTION_OPEN_BRACKETS           int = 5
	ACTION_CLOSE_BRACKETS          int = 6
	ACTION_OPEN_QUOTATION_MARKS_2  int = 7  // "
	ACTION_CLOSE_QUOTATION_MARKS_2 int = 8  // ""
	ACTION_OPEN_QUOTATION_MARKS_1  int = 9  // '
	ACTION_CLOSE_QUOTATION_MARKS_1 int = 10 // ''
)

func AnalizeLex(fileLines []string, verbose bool) (string, error) {
	//len(fileLines)
	tam := strconv.Itoa(len(fileLines))
	fmt.Println("[i] Numero de Lineas: " + tam)
	fmt.Println("<--------------------->")
	openCloseCadena := [2]bool{false, false}

	for i, line := range fileLines {
		if verbose {
			fmt.Println("\n<--------------------->")
			fmt.Printf("[L %d] %s\n", (i + 1), line)

		}
		palabras := strings.Split(line, " ")

		aggrup := true
		typa := ""
	loop:
		for _, palabra := range palabras {
			res, action := analizaPalabra(palabra)
			if aggrup {
				res = typa
			}
			switch action {
			case ACTION_IGNORE_SINGE:
				continue
			case ACTION_IGNORE_LINE:
				break loop
			case ACTION_OPEN_QUOTATION_MARKS_2:
				openCloseCadena[0] = true
				typa = "Continuación cadena"
				aggrup = true
			case ACTION_CLOSE_QUOTATION_MARKS_2:
				openCloseCadena[1] = true
				aggrup = false
			}

			fmt.Printf("\t[P %s] %s\n", palabra, res)
		}
	}
	if openCloseCadena[0] != openCloseCadena[1] {
		return "Error Lexico", fmt.Errorf("[!] No se a cerrado correctamente los paréntesis")
	}
	return "ok", nil
}

func analizaPalabra(palabra string) (string, int) {
	action := ACTION_DO_NOTHING
	if palabra == "\t" || palabra == "\n" || palabra == "" {
		return "", ACTION_IGNORE_SINGE
	}
	// Checa Por palabras reservadas
	result := "To do"
	switch palabra {
	case words.PAL_RESERV_CONDITION:
		result = "Es condición"
	case words.PAL_RESERV_BUCLE_IN:
		result = "Es blucle for"
	case words.PAL_RESERV_BUCLE_TO:
		result = "Es blucle asignmacion"
	case words.PAL_RESERV_FUNCTION:
		result = "Es Palabra funcion"
	case words.PAL_RESERV_RETURN:
		result = "Es Regreso funcion"
	case words.PAL_RESERV_IMPORT:
		result = "Es Importa"
	case words.PAL_RESERV_MODULE:
		result = "Es modulo"
	case words.DATA_TYPE_INT:
		result = "Tipo de dato entero"
	case words.DATA_TYPE_STRING:
		result = "Tipo de dato Cadena"
	case words.DATA_TYPE_CHARACTER:
		result = "Tipo de dato Caracter"
	case words.DATA_TYPE_ERROR:
		result = "Tipo de dato error"
	}

	if palabra == "//" {
		action = ACTION_IGNORE_LINE
		result = "Inicio de Comentario"
	}
	if palabra == "(" {
		action = ACTION_OPEN_PARENTHESES
		result = "Inicio de agrupador"
	}

	if palabra == ")" {
		action = ACTION_CLOSE_PARENTHESES
		result = "Fin de agrupador"
	}

	if palabra == "{" {
		action = ACTION_OPEN_BRACKETS
		result = "Inicio segmento"
	}

	if palabra == "}" {
		action = ACTION_CLOSE_BRACKETS
		result = "Fin de segmento"
	}

	if strings.HasPrefix(palabra, "\"") {
		action = ACTION_OPEN_QUOTATION_MARKS_2
		result = "Inicio de Cadena"
	}

	if strings.HasSuffix(palabra, "\"") {
		action = ACTION_CLOSE_QUOTATION_MARKS_2
		result = "Fin de Cadena"
	}

	if strings.HasPrefix(palabra, "\"") && strings.HasSuffix(palabra, "\"") {
		action = ACTION_DO_NOTHING
		result = "Cadena"
	}
	// si solo empieza con " entonce envia bandera de espera a finalizar "

	if _, err := strconv.Atoi(palabra); err == nil {
		action = ACTION_DO_NOTHING
		result = "Digito"
	}

	return result, action
}
