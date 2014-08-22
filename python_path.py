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
pwd     = os.pwd

sleep = time.sleep

exit = sys.exit

def run(cmd, stdin=None):
    from subprocess import Popen, PIPE
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    print "\n".join(p.communicate(stdin)).strip('\n')

def mkdir(path):
    if not isdir(path):
        os.mkdir(path)
