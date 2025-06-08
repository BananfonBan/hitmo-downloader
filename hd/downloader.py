import os
import asyncio
import aiohttp
from hd.parser import parse_song_name
from hd.exceptions import DirectoryNotExist


async def download_file(semaphore, session: aiohttp.ClientSession, url, filename, save_path):
    if not os.path.exists(save_path):
        raise DirectoryNotExist
    full_save_path = os.path.join(save_path, filename)

    try:
        async with semaphore, session.get(url) as response:
            if response.status == 200:
                
                # Записываем файл в указанное место
                with open(full_save_path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
                print(f"Файл успешно сохранён: {full_save_path}")
            else:
                print(f"Ошибка при загрузке {url}: статус {response.status}")
    except Exception as e:
        print(f"Произошла ошибка при загрузке {url}: {e}")
        if os.path.exists(full_save_path):
            os.remove(full_save_path)

async def download_files(urls: list[str], dir, max_concurrent_tasks=5):
    semaphore = asyncio.Semaphore(max_concurrent_tasks)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(
                download_file(
                    semaphore, session, url=url, filename=parse_song_name(url), save_path=dir
                )
            )
            tasks.append(task)

        # Ждём завершения всех задач
        await asyncio.gather(*tasks)
