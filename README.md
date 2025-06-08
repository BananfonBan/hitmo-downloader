# Hitmo Downloader

Простой асинхронный загрузчик MP3 файлов с сайта [rus.hitmotop.com](https://rus.hitmotop.com) (или [ru.hitmotop.org](https://ru.hitmotop.org)). 

## О программе

**Hitmo Downloader** — это утилита, которая позволяет асинхронно загружать MP3 файлы с сайта [rus.hitmotop.com](https://rus.hitmotop.com).  Она использует библиотеку `aiohttp` для асинхронных HTTP-запросов.

## Возможности

- Асинхронная загрузка нескольких файлов одновременно.
- Настройка максимального количества одновременных задач.

## Установка

```
pipx install https://github.com/BananfonBan/hitmo-downloader/archive/main.zip
```

## Примеры использования

### Скачать треки с [главной страницы hitmotop](https://rus.hitmotop.com/) в рабочую директорию

```
hitmo-downloader -u https://rus.hitmotop.com/
```

### Скачать треки [КиШа](https://rus.hitmotop.com/artist/1701) в домашнюю директорию пользователя с лимитом в 20 одновременно загружаемых файлов

```
hitmo-downloader -u https://rus.hitmotop.com/artist/1701 -o ~/ -limit 20
```

## Использование

```
usage: hitmo-downloader [-h] -u URLS [URLS ...] [-o OUTPUT] [-y] [--limit LIMIT]

Асинхронная загрузка треков с rus.hitmotop.com по ссылкам.

options:
  -h, --help            show this help message and exit
  -u URLS [URLS ...], --urls URLS [URLS ...]
                        Список URL-адресов для загрузки файлов.
  -o OUTPUT, --output OUTPUT
                        Путь к папке для сохранения загруженных файлов (По умолчанию текущая директория)
  -y, --yes             Автоматическое подтверждение начала загрузки.
  --limit LIMIT         Лимит скачиваемых одновременно файлов
```

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. файл [LISENCE](https://github.com/BananfonBan/hitmo-downloader/blob/main/LICENSE)

