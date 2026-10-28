"""Comprobacións automáticas. Executa: python probas.py

OK       -> a función funciona
PENDENTE -> a función aínda non está feita
FALLA    -> a función está feita pero dá un resultado incorrecto
ERRO     -> a función produce un erro ao executarse
"""

from pathlib import Path

from src.lectura import ler_notas
from src import estatisticas as est
from src import clasificacion as cla
from src import informe as inf

ALUMNADO = ler_notas(Path(__file__).parent / "datos" / "notas.csv")


def proba_media():
    assert est.media([4, 6, 8]) == 6
    assert est.media([]) == 0


def proba_maxima():
    assert est.nota_maxima([3, 9, 5]) == 9


def proba_minima():
    assert est.nota_minima([3, 9, 5]) == 3


def proba_aprobado():
    assert cla.aprobado(5) is True
    assert cla.aprobado(4.9) is False


def proba_contar_aprobados():
    assert cla.contar_aprobados([4, 5, 7, 2]) == 2


def proba_cualificacion():
    assert cla.cualificacion(4) == "Suspenso"
    assert cla.cualificacion(5) == "Aprobado"
    assert cla.cualificacion(7) == "Notable"
    assert cla.cualificacion(9) == "Sobresaliente"
    assert cla.cualificacion(10) == "Sobresaliente"


def proba_resumo():
    texto = inf.seccion_resumo(ALUMNADO)
    for linea in ["Alumnado: 6", "Media: 5.92", "Nota máxima: 9.0",
                  "Nota mínima: 3.5", "Aprobados: 4"]:
        assert linea in texto, f"Falta a liña '{linea}'"


def proba_listado():
    texto = inf.seccion_listado(ALUMNADO)
    for linea in ["Antía: 7.5 (Notable)", "Brais: 4.0 (Suspenso)",
                  "Uxía: 9.0 (Sobresaliente)", "Xoán: 5.5 (Aprobado)"]:
        assert linea in texto, f"Falta a liña '{linea}'"


def proba_informe_completo():
    texto = inf.informe_completo(ALUMNADO)
    assert "Media: 5.92" in texto, "O informe non inclúe o resumo"
    assert "Antía: 7.5 (Notable)" in texto, "O informe non inclúe o listado"


PROBAS = [
    ("FASE 1 · Usuario 1", [proba_media, proba_maxima, proba_minima]),
    ("FASE 1 · Usuario 2", [proba_aprobado, proba_contar_aprobados, proba_cualificacion]),
    ("FASE 2 · Usuario 1", [proba_resumo]),
    ("FASE 2 · Usuario 2", [proba_listado]),
    ("FASE 2 · Xuntos", [proba_informe_completo]),
]


def executar():
    for titulo, probas in PROBAS:
        print(f"\n{titulo}")
        for proba in probas:
            nome = proba.__name__.replace("proba_", "")
            try:
                proba()
                estado = "OK"
            except NotImplementedError:
                estado = "PENDENTE"
            except AssertionError as e:
                estado = f"FALLA  {e}" if str(e) else "FALLA"
            except Exception as e:
                estado = f"ERRO   {type(e).__name__}: {e}"
            print(f"  {nome:<20} {estado}")


if __name__ == "__main__":
    executar()
