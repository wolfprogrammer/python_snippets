#!/usr/bin/env python
# -*- coding: utf-8 -*-


import signal
import time


def sigint_handler(signum, frame):
    print 'Stop pressing the CTRL+C!'


signal.signal(signal.SIGINT, sigint_handler)


def main():
    while True:
        print "Try press ctrl+C"
        print '.'
        time.sleep(1)


if __name__ == "__main__":
    main()
