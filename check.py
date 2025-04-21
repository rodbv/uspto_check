import argparse
import time
from datetime import datetime, timedelta
from http import HTTPStatus

import requests
from beepy import beep

ONE_KB = 1024
ONE_MEGABYTE = 1024 * 1024
ONE_MINUTE = 60


def check(keyname, quiet: bool = False, minutes: int = 1):
    filename = f"apc{keyname}.zip"
    url = f"https://bulkdata.uspto.gov/data/trademark/dailyxml/applications/{filename}"

    failed_previously = False

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
                if not quiet and failed_previously:
                    beep("success")
                return
            else:
                print(
                    (
                        f"[{timestamp}] 🙅‍♂️ File {filename} found, "
                        f"but size is too small, {round(file_size/ONE_KB, 1)} KB. Check {url}"
                    )
                )
        else:
            print(
                (
                    f"[{timestamp}] 🤬 File {filename} not found. "
                    f"Trying again in {minutes} minute{'' if minutes == 1 else 's'}."
                )
            )

        failed_previously = True
        time.sleep(ONE_MINUTE * minutes)


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
    parser.add_argument(
        "--minutes", type=int, default=1, help="Minutes to wait between checks."
    )

    args = parser.parse_args()
    keyname = args.keyname

    if not keyname:
        yesterday = datetime.now() - timedelta(days=1)
        keyname = yesterday.strftime("%y%m%d")

    check(keyname, args.quiet, args.minutes)
