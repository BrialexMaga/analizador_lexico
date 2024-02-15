from enum import Enum

class Alfabeto(Enum):
    IDENTIFICADOR = 0
    ENTERO = 1
    REAL = 2
    CADENA = 3
    TIPO = 4 # int, float, void
    OPSUMA = 5 # +, -
    OPMUL = 6 # *, /
    OPRELAC = 7 # <, >, <=, >=, ==, !=
    OPOR = 8 # ||
    OPAND = 9 # &&
    OPNOT = 10 # !
    OPIGUALDAD = 11 # ==, !=
    PUNTOCOMA = 12 # ;
    COMA = 13 # ,
    PARENTESISIZQ = 14 # (
    PARENTESISDER = 15 # )
    LLAVEIZQ = 16 # {
    LLAVEDER = 17 # }
    ASIGNACION = 18 # =
    IF = 19
    WHILE = 20
    RETURN = 21
    ELSE = 22
    SIGNODINERO = 23 # $