#!/usr/bin/env python
"""Some custom exceptions to be raised when the time is right


"""
class DoesNotExistError(Exception):
    pass

class PathNotFoundError(Exception):
    pass

class BadEdgeCostError(Exception):
	pass

class BadFileContentsError(Exception):
	pass