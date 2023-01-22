from datetime import datetime
import time

from url_validator import is_valid
from availability_checker import is_available
from saver import save_check_result


def check_onion(urls: list) -> None:
    check_result = dict()

    for index, url in enumerate(urls):
        if url_is_valid := is_valid(url):
            url_is_available = is_available(url)

        else:
            url_is_valid = False
            url_is_available = False

        t = time.time()
        ts = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

        print(type(ts))

        check_result[index] = {
            "url": url,
            "is_valid": url_is_valid,
            "is_available": url_is_available,
            "timestamp": ts
        }

    save_check_result(check_result)
