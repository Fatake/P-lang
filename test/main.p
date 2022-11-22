modulo pricipal

importa pantalla
importa lib2

def Main(){

    Imprime("Hola Mundo en P-Lang")
    para (i, c) en (argv) {
        Imprime("[${1}] Palabra -> ${2}",i,c)
    }

    si (1 > 2) {
        Imprime(" 1 no es mayor a 2");
    } si (1 == 2) {
        Imprime("Uno no es igual a 2");
    } sino {
        Imprime("Uno es menor a 2");
    }
}