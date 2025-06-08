import os
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Асинхронная загрузка треков с rus.hitmotop.com по ссылкам.")
    
    # Аргументы командной строки
    parser.add_argument(
        "-u", "--urls",
        type=str,
        required=True,
        nargs="+",  # Позволяет передать несколько URL
        help="Список URL-адресов для загрузки файлов."
    )
    parser.add_argument(
        "-o", "--output",
        default=os.getcwd(),  # По умолчанию файлы сохраняются в текущую папку
        help="Путь к папке для сохранения загруженных файлов (По умолчанию текущая директория)"
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Автоматическое подтверждение начала загрузки."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Лимит скачиваемых одновременно файлов"
    )
    
    return parser.parse_args()