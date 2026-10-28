"""Funcións para clasificar notas.

FASE 1 · Desenvolve: USUARIO 2
"""


def aprobado(nota):
    """Devolve True se a nota é 5 ou máis, e False noutro caso.

    aprobado(5) -> True
    aprobado(4.9) -> False
    """
    raise NotImplementedError


def contar_aprobados(notas):
    """Recibe unha lista de notas e devolve cantas están aprobadas.
    Pista: usa a función aprobado().

    contar_aprobados([4, 5, 7, 2]) -> 2
    """
    raise NotImplementedError


def cualificacion(nota):
    """Devolve o texto da cualificación:
    menos de 5 -> "Suspenso"
    de 5 a menos de 7 -> "Aprobado"
    de 7 a menos de 9 -> "Notable"
    9 ou máis -> "Sobresaliente"
    """
    raise NotImplementedError
