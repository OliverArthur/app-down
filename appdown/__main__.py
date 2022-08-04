# __main__.py

import asyncio
import pathlib
import sys
from unittest import result

from appdown.checker import site_is_online, site_is_online_async
from appdown.cli import display_results, read_users_cli_args


def main():
    """Run the CLI"""
    users_args = read_users_cli_args()
    urls = _get_website_urls(users_args)

    if not urls:
        print("No URLs provided", file=sys.stderr)
        sys.exit(1)
    if users_args.asynchronous:
        asyncio.run(_asynchronous_check(urls))
    else:
        _synchronous_check(urls)


def _get_website_urls(users_args):
    """Get the URLs to check"""
    urls = users_args.target_urls
    if users_args.input_file:
        urls += _get_urls_from_file(users_args.input_file)
    return urls


def _get_urls_from_file(file):
    """Get the URLs from a file"""
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            if urls := [url.strip() for url in urls_file]:
                return urls
            print(f"No URLs found in {file_path}", file=sys.stderr)
    else:
        print(f"{file_path} is not a file", file=sys.stderr)
    return []


async def _asynchronous_check(urls):
    """Check if the URLs are down"""
    async def _check(urls):
        error = ""
        try:
            result = await site_is_online_async(urls)
        except Exception as e:
            result = False
            error = str(e)
        display_results(results=result, urls=urls, errors=error)

    await asyncio.gather(*(_check(url) for url in urls))


def _synchronous_check(urls):
    """Check if the URLs are down"""
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_results(results=result, urls=url, errors=error)

if __name__ == "__main__":
    main()