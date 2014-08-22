#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Placehoder to Create File templates

$ python placeholder.py

Output:
---------------------------------------------
    The Author is Mr. dummy

    it is my myscript.py

    Template engine myscript.py./bin/sh

    ./myscript.py
--------------------------------------------


"""


template = """

The Author is {{ AUTHOR }}

it is my {{ SCRIPT}}

Template engine {{ SCRIPT}}.{{ SHELL}}

./{{SCRIPT}}
"""


def placeholder(template, **kargs):
    import re

    txt = template

    for k in kargs.keys():
        v = kargs[k]
        txt = re.sub("{{\s*%s\s*}}" % k, v, txt)

    return txt


print placeholder(template, SCRIPT="myscript.py", SHELL="/bin/sh", AUTHOR="Mr. dummy")