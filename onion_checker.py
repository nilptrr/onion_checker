from datetime import datetime
import time
import validators

from availability_checker import is_available
from saver import save_check_result


def check_onion(urls: list) -> None:
    check_result = dict()

    for index, url in enumerate(urls):
        url_is_valid: True | validators.ValidationFailure = validators.url(url)

        if url_is_valid:
            url_is_available = is_available(url)
        else:
            url_is_valid = False        # Cast validators.ValidationFailure to bool
            url_is_available = False

        t = time.time()
        timestamp = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

        check_result[index] = {
            "url": url,
            "is_valid": url_is_valid,
            "is_available": url_is_available,
            "timestamp": timestamp
        }

    save_check_result(check_result)
