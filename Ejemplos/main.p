modulo nombre
importa ( "Lib1", "Lib2" )

// Comentario
def NombreFuncion (Parametro entero, Algo cadena) (salida string, err error) {
    asignacion := valor
    regresa asignacion
}

def Main(argc entero, argv cadena) {

    Imprime("Hola Mundo en P-Lang")
    para i, c en argv {
        Imprime("[${1}] Palabra -> ${2}",i,c)
    }

    si (1 > 2) {
        Imprime(" 1 no es mayor a 2")
    } si (1 == 2) {
        Imprime("Uno no es igual a 2")
    } entonces {
        Imprime("Uno es menor a 2")
    }

    regresa 1
}