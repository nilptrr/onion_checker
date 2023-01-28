import requests

from config import proxies


def is_available(url: str) -> bool:
    try:
        requests.get(url, proxies=proxies, timeout=5)

    except requests.exceptions.RequestException:
        return False

    else:
        return True
