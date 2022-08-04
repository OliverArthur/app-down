# checker.py

import asyncio
import aiohttp

from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=10) -> bool:
    """Return True is the target URL is online.
    Raise exception otherwise.

    Args:
        url (_type_): target ulr
        timeout (int, optional): timeout, default is 10
    """

    error = Exception('Unknown error')
    parser = urlparse(url)
    host = parser.netloc or parser.path.split('/')[0]

    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)

        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()

    raise error


async def site_is_online_async(url, timeout=10) -> bool:
    """Return True if the target url is accessible, otherwise
    raise an exception.
    """
    error = Exception('Unknown error')
    parser = urlparse(url)
    host = parser.netloc or parser.path.split('/')[0]

    for schema in ("http", "https"):
        target_url = f"{schema}://{host}"
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(target_url, timeout=timeout)
                return True
            except asyncio.exceptions.TimeoutError:
                error = Exception(f" TIME OUT! This url {target_url} is not accessible")
            except Exception as e:
                error = e
    raise error