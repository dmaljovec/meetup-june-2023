"""The main entry point for the CLI."""
import base64
import sys


import click

from demo._version import __version__
from demo.constants import BANNER

PACKAGE_NAME = "demo"


def print_banner() -> None:
    """Print a cool logo."""
    if BANNER:
        banner = (
            "4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK44qOn4qCA4qCA4qCA4qC"
            "A4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4q"
            "CA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4"
            "qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA"
            "4qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKiuOKjv+Kjp+K"
            "ggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggO"
            "KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgg"
            "OKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKg"
            "gOKggOKggOKggOKggArioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiorj"
            "io7/ior/ioYbioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioI"
            "DioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio"
            "IDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDi"
            "oIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC"
            "A4qCA4qCA4qO/4qO44qO/4qGA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4q"
            "CA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4"
            "qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA"
            "4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOK"
            "ggOKggOKggOKggOKggOKiv+Khj+KjuOKjt+KggOKggOKggOKggOKggOKggOKggO"
            "KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgg"
            "OKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKg"
            "gOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggArioIDioIDioIDioID"
            "ioIDioIDioIDioIDioIDioIDioIDiorjiob/ioIvio7vio4bioIDioIDioIDioI"
            "DioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio"
            "IDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDi"
            "oIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qC"
            "A4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK44qOn4qO84qCL4qK/4qGG4q"
            "CA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4"
            "qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA"
            "4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC"
            "ACuKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKjv+KggeKigO"
            "KhvuKjv+KjpOKjpOKjpOKjpOKjhOKjgOKjgOKjgOKggOKggOKggOKggOKggOKgg"
            "OKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKg"
            "gOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOK"
            "ggOKggOKggArioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio6Dio77io7"
            "/io7TioJ/ioIHio7jio6fioYDioIDioInioInioInioInioJvioJvioLvioLfio"
            "7bio6Tio4DioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDi"
            "oIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioID"
            "ioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qOw4qG/4q"
            "Cb4qCB4qK/4qGF4qKA4qO84qCP4qK54qOn4qCA4qCA4qCA4qCA4qCA4qCA4qCA4"
            "qCA4qCA4qCI4qCZ4qC74qK34qOm4qOE4qGA4qCA4qCA4qCA4qCA4qCA4qCA4qCA"
            "4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC"
            "A4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKjoOKjvu"
            "Kgi+KggOKggOKggOKiuOKjn+Kgi+KggeKigOKjtOKgn+KggOKggOKggOKggOKgg"
            "OKggOKggOKggOKggOKggOKggOKggOKggOKgiOKgmeKgu+Kjt+KjhOKggOKggOKg"
            "gOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOK"
            "ggOKggOKggOKggOKggOKggOKggOKggOKggOKggArioIDioIDioIDioIDiooDio7"
            "zioZ/ioIHioIDioIDioIDioIDioIjioJvioJvioJvioJvioInioIDioIDioIDio"
            "IDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIjioLvi"
            "o7fio4TioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioID"
            "ioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4q"
            "Kg4qO/4qCL4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4"
            "qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA"
            "4qCA4qCA4qCI4qK74qOn4qGA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC"
            "A4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggO"
            "KggOKioOKjv+Kgg+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKgg"
            "OKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKg"
            "gOKggOKggOKggOKggOKggOKggOKgueKjt+KhgOKggOKggOKggOKggOKggOKggOK"
            "ggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggO"
            "KggArioIDioIDio77io6fio7bio7bio7bio6TioYDioIDioIDioIDioIDioIDio"
            "IDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDi"
            "oIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioLnio7fioYDioIDioIDioID"
            "ioIDioIDioIDioIDiooDio4TioIDioIDioIDioIDioIDioIDioIDioIDioIDioI"
            "DioIDioIDioIAK4qCA4qO44qO/4qO/4qO/4qCL4qCJ4qK74qO/4qGE4qCA4qCA4"
            "qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qOg4qO04qO+4qO24qO24qOm4qGA"
            "4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK54qOn4qC"
            "A4qCA4qCA4qCA4qCA4qCA4qKg4qO+4qK/4qOn4qCA4qCA4qCA4qCA4qCA4qCA4q"
            "CA4qCA4qCA4qCA4qCA4qCACuKggOKjv+Kjv+Kgm+Kiu+KjpuKjpOKjvuKjv+Khh"
            "+KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKisOKjv+Kjv+Kjv+Kgi+Kg"
            "iOKiueKjv+KhgOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOK"
            "ggOKjv+KhhuKggOKggOKggOKggOKioOKjv+Kgi+KggOKiu+Kjp+KggOKggOKggO"
            "KggOKggOKggOKggOKggOKggOKggOKggArioIDio7/ioZ/ioqbio77io7/io7zio"
            "b/ioJ/ioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiorjio7/ioIni"
            "oLnio7fiorbio77io7/ioIPioIDioIDioIDioIDioIDioIDioIDioIDioIDioID"
            "ioIDioIDioIDioJjior/io4bioIDioIDioIDio7/ioYfioIDioIDioIDiorvio6"
            "fioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qK74qGH4qCA4qCI4"
            "qCJ4qCJ4qCA4qCA4qCA4qCA4qOk4qCA4qCA4qCA4qKA4qGE4qCA4qCA4qCA4qCA"
            "4qC74qK34qO+4qO/4qO+4qC/4qCD4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC"
            "A4qCA4qCA4qCA4qCA4qCA4qCA4qCI4qK/4qOm4qGA4qCA4qK54qO34qCA4qCA4q"
            "CA4qCA4qC74qC34qC24qC24qC24qC24qC24qC24qC24qK24qO2CuKggOKguOKjt"
            "+KggOKggOKggOKggOKggOKggOKggOKgmOKjv+KhhOKggOKioOKjv+Kgh+KggOKg"
            "gOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOK"
            "ggOKituKjhOKggOKggOKggOKggOKggOKggOKggOKggOKgmeKgu+Kgt+Kgv+Kgm+"
            "KggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKioOKjv+KggQrio"
            "IDio7Dio7/io4fioIDioIDioIDioIDioIDioIDioIDioIjioJvioJvioJvioIHi"
            "oIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioqDioYDioID"
            "ioIDioIDioIDioIDioJnio7fio4TioIDioIDioIDioIDioIDioIDioIDioIDioI"
            "DioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDio7Diob/io"
            "IPioIAK4qKw4qO/4qCL4qK/4qOG4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA"
            "4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC"
            "Y4qO/4qOE4qCA4qCA4qCA4qCA4qCA4qK44qO/4qCA4qCA4qCA4qCA4qCA4qCA4q"
            "CA4qCA4qCA4qCA4qKA4qOg4qOk4qO24qOm4qOk4qOA4qCA4qCA4qCA4qOg4qO+4"
            "qCf4qCB4qCA4qCACuKjv+Kjh+KggOKgiOKjv+KjhuKggOKggOKggOKggOKggOKg"
            "gOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOK"
            "ggOKggOKggOKgmOKiv+KjpuKhgOKggOKggOKggOKiuOKjv+KggOKggOKggOKggO"
            "KggOKggOKggOKigOKjoOKjtuKgn+Kgi+KggeKggOKggOKgieKgm+Kgu+Kgv+Kgv"
            "+Kgm+KggeKggOKggOKggOKggArioInioJvioL/ioL/ioL/ioL/io7fio4TioIDi"
            "oIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioID"
            "ioIDioIDioIDioIDioIDioIDioIDioJnioL/iorfio6bio6Tio7jiob/ioIDioI"
            "DioIDioIDioIDio6Dio77ioJ/ioIvioIDioIDioIDioIDioIDioIDioIDioIDio"
            "IDioIDioIDioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCI"
            "4qCZ4qC74qO24qOk4qGA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qC"
            "A4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCI4qCJ4qCJ4q"
            "CB4qCA4qCA4qKA4qOg4qG+4qCf4qCB4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4"
            "qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKg"
            "gOKggOKggOKggOKggOKggOKgieKgm+Kgv+KituKjpuKjpOKjgOKhgOKggOKggOK"
            "ggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggO"
            "KigOKjgOKjpOKjtOKhtuKgn+Kgi+KggOKggOKggOKggOKggOKggOKggOKggOKgg"
            "OKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggOKggArioIDioIDi"
            "oIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDiooDioonio5nioJv"
            "ioL/ioLfioLbiorbio7bio7bio6bio6Tio6Tio6Tio6Tio6Tio6Tio7biobbioL"
            "bioL7ioJ/ioJvioIvioIniooDio4DioIDioIDioIDioIDioIDioIDioIDioIDio"
            "IDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIDioIAK"
        )
        print(base64.b64decode(banner).decode("utf-8"))


@click.group()
def cli() -> None:
    """Do something."""
    print_banner()
    print(f"Version: {__version__}")


@click.command()
def check() -> None:
    """Check something."""
    pass


cli.add_command(check)

if __name__ == "__main__":
    cli()
