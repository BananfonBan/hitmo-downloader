import os
import sys
from hd.downloader import download_files
from hd.parser import parse_downloading_links, valid_domains

yes_answer = {"y", "Y", "Yes", "yes", "Да"}


# Основная функция для загрузки всех файлов
async def app(urls: list[str], dir, confirmation, max_concurrent_tasks):
    if not valid_domains(urls):
        print(
            "Указанные ссылки не поддерживаются. Поддерживаемые домены: rus.hitmotop.com, ru.hitmotop.org"
        )
        sys.exit()
    if not os.path.exists(dir):
        print("Указанной директории не существует")
        sys.exit()
    downloading_links = []
    for url in urls:
        downloading_links += parse_downloading_links(url)
    print(f"Было найдено {len(downloading_links)} треков")
    if confirmation:
        await download_files(downloading_links, dir, max_concurrent_tasks)
    else:
        answ = input("Продолжить? (Y/N): ")
        if answ in yes_answer:
            await download_files(downloading_links, dir, max_concurrent_tasks)
        else:
            print("Загрузка отменена")
