import sys
import time
from datetime import datetime, timedelta

import requests
from beepy import beep


def check(keyname):
    filename = f"apc{keyname}.zip"
    url = f"https://bulkdata.uspto.gov/data/trademark/dailyxml/applications/{filename}"

    while True:
        response = requests.head(url)

        timestamp = datetime.now().time().isoformat()[:8]

        if response.status_code == 200:
            print(f"[{timestamp}]✅ File {filename} found!\nCheck {url}")
            beep("success")
            return

        print(f"[{timestamp}] 🤬 File {filename} not found. Checking again in 1 minute")
        time.sleep(60)


if __name__ == "__main__":
    keyname = len(sys.argv) > 1 and sys.argv[1]

    if not keyname:
        yesterday = datetime.now() - timedelta(days=1)
        keyname = yesterday.strftime("%y%m%d")

    check(keyname)
