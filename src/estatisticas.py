"""Funcións estatísticas básicas.

FASE 1 · Desenvolve: USUARIO 1
Todas reciben unha lista de números, por exemplo [7.5, 4.0, 9.0].
"""


def media(notas):
    return sum(notas) / len(notas) if notas else 0

def nota_maxima(notas):
    return max(notas)


def nota_minima(notas):
    return min(notas)
