# APP-DOWN

> Verify a web is down or not

This a simple python CLI app to check if a website is down by passing the url as an argument.

## Setup

```sh
git clone git+ssh://oliverarthur/app-down.git
```

Go to the directory folder

```sh
cd app-down
```

Install all dependencies via poetry, if you don't have poetry, you can install it with `pip install poetry` or visit the url [python-poetry.org/docs](https://python-poetry.org/docs/) and follow the instructions.

```sh
poetry install
```

## Usage

```sh
python -m appdown -h
```

The command from above will show the help message.

```sh
python -m appdown -u https://www.google.com

// or passing multiple urls

python -m appdown -u https://www.google.com https://www.bing.com
```

The command from above will check if the website is down or not. by using the flag `-u` to pass the url or multiple urls

```sh
python -m appdown -f file.txt
```

The command from above will check if the websites in the file are down or not. by using the flag `-f` to pass the file path.

All the previews command will execute synchronously and if you want to execute them asynchronously, you can use the `-a` argument, eg:

```sh
python -m appdown -u https://www.google.com -a
```

### Technologies Used

- [Python](https://www.python.org/) version 3.10
- [Python Poetry](https://python-poetry.org/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [aiohttp](https://aiohttp.readthedocs.io/en/stable/)

### TODO

- [ ] Add unit-tests
- [ ] Make the app available for webapp interface via API.
