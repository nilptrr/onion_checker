# Onion checker
Checks the availability of onion services and returns the result of the check in urls.json.
## Requirements
- Python 3.10

## Install
1. Install Tor
2. Create a virtual environment and install dependencies
```shell
$ python3 -m venv venv
$ pip install -r requirements.txt 
```

## Usage
```python
from onion_checker import check_onion


urls = [
    'https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/',
]

check_onion(urls)
```

## License
The Unlicense. See the LICENSE file for details.
