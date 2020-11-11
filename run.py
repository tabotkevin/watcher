#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

from watcher import FileWatcher

@click.command()
@click.option("--path", default=".", help="Folder path.")
@click.option("--patterns", default="*", help=r"File patterns to watch e.g '*.jpg, *.pdf' or '*' for everything.")
def main(path, patterns):
    print(f"Watching: {path} for patterns {patterns}")
    patterns = [pattern.strip() for pattern in patterns.split(",")]
    FileWatcher(path, patterns).run()

if __name__ == "__main__":
    main()
