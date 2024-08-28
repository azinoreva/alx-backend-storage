#!/usr/bin/env python3
'''
Function that return all doc
'''


def list_all(mongo_collection):
    '''
    Returns a cursor object
    '''
    return list(mongo_collection.find())
