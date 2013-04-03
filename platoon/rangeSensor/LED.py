#!/usr/bin/python

from __future__ import division

def analogToDigital(analogColors):
	'''
	Accepts a 2D list of analog RGB values (analogColors) and converts them 	to digital.
	Returns - 2D list of digital RGB values (digitalColors)
	'''
        digitalColors = [[x/255 for x in y] for y in analogColors]
        return digitalColors

