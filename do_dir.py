#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def find_file(path,item):
	for x in os.listdir(path):
		if item in x and os.path.isfile(os.path.join(path,x)):
			print(os.path.relpath(os.path.join(path,x)))
		elif os.path.isdir(os.path.join(path,x)):
			find_file(os.path.join(path,x),item)

find_file('.','.py')