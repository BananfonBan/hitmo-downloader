from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup


def _parse_main_page(link: str) -> str:
    result_link = (
        urlparse(link)._replace(path="", params="", query="", fragment="").geturl()
    )
    return result_link


def valid_domain(link: str) -> bool:
    domains = {"rus.hitmotop.com", "ru.hitmotop.org"}
    hostname = urlparse(link).hostname
    if hostname in domains:
        return True
    else:
        return False


def valid_domains(urls: list[str]) -> bool:
    for url in urls:
        if not valid_domain(url):
            return False
    return True


def parse_song_name(url: str) -> str:
    song_name = url.split("/")[-1]
    return song_name


def parse_downloading_links(link: str) -> list[str]:
    html = requests.get(link).text
    bs = BeautifulSoup(html, "html.parser")
    track_tags = bs.find_all("a", class_="track__download-btn")
    links_list = [link["href"] for link in track_tags]
    return links_list


def parse_pagination_links(link: str) -> list[str | None]:
    html = requests.get(link).text
    bs = BeautifulSoup(html, "html.parser")
    pagination_tags = bs.find_all("a", class_="pagination__link")
    links_list = [link["href"] for link in pagination_tags]
    main_page = _parse_main_page(link)
    result_list = []
    for link_ in links_list:
        result_list.append(main_page + link_)
    return result_list
