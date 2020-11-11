#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

from watchdog.observers import Observer
from handler import FileEventHandler

class FileWatcher:

    def __init__(self, src_path, patterns):
        self._src_path = src_path
        self._handler = FileEventHandler(patterns=patterns)
        self._observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self._schedule()
        self._observer.start()

    def stop(self):
        self._observer.stop()
        self._observer.join()

    def _schedule(self):
        self._observer.schedule(
            self._handler,
            self._src_path,
            recursive=True
        )

