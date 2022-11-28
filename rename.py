#!/usr/bin/env python

from os import rename, walk
from os.path import *
from sys import argv

ignoreFiles = ["rename.py", "turtle.jpg", "__pycache__"]


def change_content(change_to, dirname, names):
    # ignore some dirs
    if basename(dirname) in ignoreFiles:
        return

    for name in names:
        # ignore some files
        if name in ignoreFiles:
            continue
        full_path = join(dirname, name)
        if isfile(full_path):
            print("Adjusting content in %s" % full_path)
            content = open(full_path, "r").read()
            content = content.replace(change_from.capitalize(), change_to.capitalize())
            content = content.replace(change_from.upper(), change_to.upper())
            content = content.replace(change_from, change_to)
            open(full_path, "w").write(content)
        elif isdir(full_path):
            for baseDir, dirName, fileNames in walk(full_path):
                change_content(change_to, baseDir, fileNames)


def rename_files(change_to, dirname, names):
    # ignore some dirs
    if basename(dirname) in ignoreFiles:
        return

    for name in names:
        # ignore some files
        if name in ignoreFiles:
            continue
        full_path = join(dirname, name)
        if isdir(full_path):
            for baseDir, dirName, fileNames in walk(full_path):
                rename_files(baseDir, fileNames, change_to)
        if name.find(change_from) != -1:
            new_name = name.replace(change_from, change_to)
            print("Renaming %s to %s" % (full_path, join(dirname, new_name)))
            rename(full_path, join(dirname, new_name))


change_from = 'skeleton'
change_to = argv[-1].lower()
print("Changing name of toolkit project to '%s'." % change_to)
for directory, dirnames, filenames in walk("."):
    change_content(change_to, directory, filenames)
for directory, dirnames, filenames in walk("."):
    rename_files(change_to, directory, filenames)
