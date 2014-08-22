#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.pasteur.fr/formation/infobio/python/ch19s06.html

class Singleton:

    _nb = 0

    def __init__(self):
        if Singleton._nb > 0:
            raise Exception, "not more than one instance of " + str(self.__class__)
        Singleton._nb = 1

print "creating a 1st instance"
s1 = Singleton()

print "creating a 2nd instance"
s2 = Singleton()

