import requests

from config import proxies


def is_available(url: str) -> bool:
    try:
        requests.get(url, proxies=proxies)

    except requests.exceptions.RequestException:
        return False

    else:
        return True
