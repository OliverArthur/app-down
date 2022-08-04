# cli.py

import argparse


def read_users_cli_args():
    """Handle the CLI arguments and options"""
    parser = argparse.ArgumentParser(
        prog='is-app-down',
        description='Check if an app is down',
    )
    parser.add_argument(
        "-u",
        "--target-urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more URLs to check if they are down",
    )
    parser.add_argument(
        '-f',
        '--input-file',
        metavar='FILE',
        type=str,
        default="",
        help='Read URLs from a file',
    )
    parser.add_argument(
        '-a',
        '--asynchronous',
        action='store_true',
        help='Check the URLs asynchronously',
    )
    return parser.parse_args()


def display_results(results, urls, errors=""):
    """Display the results of a connectivity check"""
    print(f"The status of {urls} is:", end=" ")
    if results:
        print('"Online!" 👍')
    else:
        print(f'"Offline!" 👎 \n Error: "{errors}"')