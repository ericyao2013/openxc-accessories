#!/usr/bin/python

# $Rev:: 363           $
# $Author:: mlgantra   $
# $Date:: 2015-06-16 1#$
#
# openXC-Modem version


VERSION = (0, 1, 4)

__version__ = '.'.join(map(str, VERSION))

def get_version():
    return __version__


if __name__ == '__main__':
    print get_version() 
