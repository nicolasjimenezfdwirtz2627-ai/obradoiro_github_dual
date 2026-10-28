"""Xeración do informe.

FASE 2 · Neste ficheiro traballan AS DÚAS PERSOAS.
"alumnado" é a lista que devolve ler_notas():
[{"nome": "Antía", "nota": 7.5}, {"nome": "Brais", "nota": 4.0}, ...]
"""

from src.estatisticas import media, nota_maxima, nota_minima
from src.clasificacion import contar_aprobados, cualificacion


def seccion_resumo(alumnado):
    """USUARIO 1. Devolve un texto (str) con este formato exacto:

    Alumnado: 6
    Media: 5.92
    Nota máxima: 9.0
    Nota mínima: 3.5
    Aprobados: 4

    Pistas: primeiro crea a lista só coas notas.
    A media leva dous decimais: f"Media: {valor:.2f}"
    Une as liñas con "\\n".join(lista_de_linas)
    """
    raise NotImplementedError


def seccion_listado(alumnado):
    """USUARIO 2. Devolve un texto (str) cunha liña por alumno/a:

    Antía: 7.5 (Notable)
    Brais: 4.0 (Suspenso)
    ...

    Pistas: percorre a lista cun for e usa cualificacion().
    Une as liñas con "\\n".join(lista_de_linas)
    """
    raise NotImplementedError


def informe_completo(alumnado):
    """Xunta todas as seccións do informe."""
    partes = ["=== INFORME DE NOTAS ==="]
    # FASE 2: cada persoa engade AQUÍ a chamada á súa sección, por exemplo:
    # partes.append(seccion_xxx(alumnado))
    return "\n\n".join(partes)
