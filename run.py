#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

from watcher import FileWatcher

@click.command()
@click.option('--path', default=".", help='Folder path.')
def main(path):
    print(f'Watching: {path}')
    FileWatcher(path).run()

if __name__ == "__main__":
    main()
