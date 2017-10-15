
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path,path))

    def __call__(self, attr):
        return Chain('%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path

    __repr__ = __str__

url1 = Chain().status.user.timeline.list
url2 = Chain().users('Kzc').repos

print(url1)
print(url2)