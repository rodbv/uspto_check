import argparse
import time
from datetime import datetime, timedelta
from http import HTTPStatus

import requests
from beepy import beep

ONE_MEGABYTE = 1024 * 1024  # 1 MB
ONE_MINUTE = 60


def check(keyname, quiet):
    filename = f"apc{keyname}.zip"
    url = f"https://bulkdata.uspto.gov/data/trademark/dailyxml/applications/{filename}"

    while True:
        response = requests.head(url)

        timestamp = datetime.now().time().isoformat()[:8]

        if response.status_code == HTTPStatus.OK:
            file_size = int(response.headers.get("Content-Length", 0))

            if file_size > ONE_MEGABYTE:
                print(
                    (
                        f"[{timestamp}] ✅ File {filename} found! (Size: {round(file_size/ONE_MEGABYTE, 1)} MB). "
                        f"Check {url}"
                    )
                )
                if not quiet:
                    beep("success")
                return
            else:
                print(
                    (
                        f"[{timestamp}] 🙅‍♂️ File {filename} found, "
                        f"but size is too small. Check {url}"
                    )
                )
        else:
            print(
                (
                    f"[{timestamp}] 🤬 File {filename} not found. "
                    "Trying again in 1 minute."
                )
            )

        time.sleep(ONE_MINUTE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--keyname",
        type=str,
        default=None,
        help="Specify the keyname, e.g. 231210 (YYMMDD).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        default=False,
        help="Suppress sound when file is found.",
    )

    args = parser.parse_args()
    keyname = args.keyname

    if not keyname:
        yesterday = datetime.now() - timedelta(days=1)
        keyname = yesterday.strftime("%y%m%d")

    check(keyname, args.quiet)
