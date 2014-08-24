#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This shortcouts are useful to write
shell and bat scripts replacements
and to easy locate the files in
the script directory.

"""

import os
import sys
import time

# this script absolute path
this = os.path.abspath(__file__)
# this script directory
this_dir= os.path.dirname(this)

HOME = os.path.expanduser("~")
USERNAME = os.path.basename(HOME)


listdir  = os.listdir
join     = os.path.join
abspath  = os.path.abspath
dirname  = os.path.dirname
basename = os.path.basename

isfile    = os.path.isfile
isdir     = os.path.isdir
exists    = os.path.exists

chdir      = os.chdir
cwd     = os.getcwd
pwd     = os.getcwd()

sleep = time.sleep

exit = sys.exit

def run(cmd, stdin=None):
    from subprocess import Popen, PIPE
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    print "\n".join(p.communicate(stdin)).strip('\n')

def mkdir(path):
    if not isdir(path):
        os.mkdir(path)

def walkdir(path, pattern):
    """

    :param path:        (str)
    :param pattern:
    :return:
    """
    import fnmatch
    import os

    matches = []
    for root, dirnames, filenames in os.walk(path):
      for filename in fnmatch.filter(filenames, pattern):
          yield os.path.join(root, filename)
          #matches.append(os.path.join(root, filename))




# Remove the annotations if you're not on Python3
def find_files(dir_path, patterns):
    """
    Returns a generator yielding files matching the given patterns
    :type dir_path: str
    :type patterns: [str]
    :rtype : [str]
    :param dir_path: Directory to search for files/directories under. Defaults to current dir.
    :param patterns: Patterns of files to search for. Defaults to ["*"]. Example: ["*.json", "*.xml"]
    """
    import fnmatch
    import functools
    import itertools
    import os
    path = dir_path or "."
    path_patterns = patterns or ["*"]

    for root_dir, dir_names, file_names in os.walk(path):
        filter_partial = functools.partial(fnmatch.filter, file_names)

        for file_name in itertools.chain(*map(filter_partial, path_patterns)):
            yield os.path.join(root_dir, file_name)


print "this = ", this
print "this_dir = ", this_dir
print "HOME = ", HOME
print "USERNAME = ", USERNAME
print "Current Directoru = ", os.getcwd()

#print list(walkdir(this_dir, "*.py"))

print list(find_files(".", ['*.py']))

exit(0)