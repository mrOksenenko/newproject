#!/usr/bin/env python3
"""Выводит текущее время в терминале. Остановка: Ctrl+C."""

import sys
import time
from datetime import datetime


def main() -> None:
    try:
        while True:
            now = datetime.now().strftime("%H:%M:%S")
            # \r возвращает курсор в начало строки, поэтому время обновляется на месте
            sys.stdout.write(f"\rТекущее время: {now}")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nВыход.")


if __name__ == "__main__":
    main()
