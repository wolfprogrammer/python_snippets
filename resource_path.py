#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Useful functions to locate files in the script directory.
Unlike __file__, it can be called from another file and
reused.

"""

def resource_path(filename):
    """
    :param filename: (str)  Name of file in same directory of script
    Returns absolute path to file in same directory that this function
    is being called.
    """

    import os
    import inspect
    return os.path.join( os.path.dirname(os.path.abspath(inspect.stack()[1][1])), filename)

def this():
    """
    Returns the absolute path to the script that calls this function
    """
    import os
    import inspect
    return os.path.abspath(inspect.stack()[1][1])

def this_dir():
    """
    Returns the absolute path to script directory that calls this function
    """
    import os
    import inspect
    return os.path.dirname(os.path.abspath(inspect.stack()[1][1]))


