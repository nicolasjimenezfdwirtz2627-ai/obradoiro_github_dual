"""Programa principal: le os datos e mostra o informe."""

from pathlib import Path

from src.lectura import ler_notas
from src.informe import informe_completo

RUTA_DATOS = Path(__file__).parent / "datos" / "notas.csv"


def main():
    alumnado = ler_notas(RUTA_DATOS)
    print(informe_completo(alumnado))


if __name__ == "__main__":
    main()
