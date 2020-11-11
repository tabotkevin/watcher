#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from watchdog.events import PatternMatchingEventHandler
from redis import Redis
from rq import Queue

from utils import process_file

class FileEventHandler(PatternMatchingEventHandler):

    def __init__(self, *args, **kwargs):
        super(FileEventHandler, self).__init__(*args, **kwargs)
        self.q = Queue(connection=Redis())

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        filename = event.src_path
        self.q.enqueue(process_file, filename)


