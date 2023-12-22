import argparse
import time
from datetime import datetime, timedelta
from http import HTTPStatus

import requests
from beepy import beep


def check(keyname, quiet):
    filename = f"apc{keyname}.zip"
    url = f"https://bulkdata.uspto.gov/data/trademark/dailyxml/applications/{filename}"

    while True:
        response = requests.head(url)

        timestamp = datetime.now().time().isoformat()[:8]

        if response.status_code == HTTPStatus.OK:
            print(f"[{timestamp}]✅ File {filename} found!\\nCheck {url}")
            if not quiet:
                beep("success")
            return

        print(f"[{timestamp}] 🤬 File {filename} not found. Trying again in 1 minute")

        time.sleep(60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--keyname", type=str, default=None, help="Specify the keyname as a string"
    )
    parser.add_argument(
        "--quiet", action="store_true", default=False, help="Suppress output messages"
    )

    args = parser.parse_args()
    keyname = args.keyname

    if not keyname:
        yesterday = datetime.now() - timedelta(days=1)
        keyname = yesterday.strftime("%y%m%d")

    check(keyname, args.quiet)
