#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Screen(object):

	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width = value
		
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

a = Screen()
a.width = 2
a.height = 3
print(a.resolution)
assert a.resolution == 786432, '1024 * 768 = %d ?' % a.resolution