#!/usr/bin/python3
""" Function that addsnew attribute to an object if it is possible """


def add_attribute(obj, name, value):
    """ Function for add attribute"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
