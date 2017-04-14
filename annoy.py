import time

from datetime import datetime


def main():
    while True:
        time.sleep(2)
        print '{} hello'.format(datetime.now())


if __name__ == '__main__':
    main()

