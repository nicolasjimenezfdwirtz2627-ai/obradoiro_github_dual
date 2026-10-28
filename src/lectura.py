"""Lectura dos datos. Este ficheiro xa está feito: non hai que tocalo."""

import csv


def ler_notas(ruta):
    """Le o CSV e devolve unha lista de dicionarios, un por alumno/a.

    Exemplo: [{"nome": "Antía", "nota": 7.5}, {"nome": "Brais", "nota": 4.0}, ...]
    """
    alumnado = []
    with open(ruta, encoding="utf-8") as ficheiro:
        for fila in csv.DictReader(ficheiro):
            alumnado.append({"nome": fila["nome"], "nota": float(fila["nota"])})
    return alumnado
