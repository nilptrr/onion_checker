import json


def save_check_result(check_result: dict[int, dict[str, bool, bool, str]]) -> None:
    with open('urls.json', 'w') as f:
        json.dump(check_result, f, ensure_ascii=False, indent=4)
