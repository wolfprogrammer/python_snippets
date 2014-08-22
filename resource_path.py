#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Useful functions to locate files in the script directory.
Unlike __file__, it can be called from another file and
reused.

"""

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

def resource_path(filename):
    """
    :param filename: (str)  Name of file in same directory of script
    Returns absolute path to file in same directory that this function
    is being called.
    """

    import os
    import inspect
    return os.path.join( os.path.dirname(os.path.abspath(inspect.stack()[1][1])), filename)

def get_resource_file(filen):
    """
    :param filen: (str) File name of resource file
    :return:

    Return content of file in same directory of the script calling
    this routine or inside the zip file if the script is imported
    from a zip file ( Python egg file).

    """
    import zipfile
    import os
    import inspect
    this_directory = os.path.dirname(os.path.abspath(inspect.stack()[1][1]))
    #logger.debug("Getting resource file %s" % filen)

    if zipfile.is_zipfile(this_directory):
       #logger.debug("ZIP FILE")
       zf = zipfile.ZipFile(this_directory)
       data = zf.read(filen)

    else:
       #logger.debug("NOT ZIP FILE")
       data = open(os.path.join(this_directory, filen)).read()

    return data
