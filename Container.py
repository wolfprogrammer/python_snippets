#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Examples of how to use container class.

>>> from Container import Container
>>> cont = Container()
>>> cont['a'] = 10.23
>>> cont.a
10.23
>>>
>>> dir(cont)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'set', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
>>>
>>> cont.b = "hello world"
>>>
>>> cont.keys()
['a', 'b']
>>>
>>> cont.get('a')
10.23
>>> cont.get('b')
'hello world'
>>> cont.set('hello', 'world')
>>> cont.hello
'world'
>>>


"""


class Container(dict):

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

    def set(self, key, value):
        self[key] = value
#        self.__keys__.append(key)

    def get(self, key):
        return self[key]


    def __getattr__(self, item):
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value

