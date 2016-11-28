# -*- coding: utf-8 -*-
version_tuple = (0, 0, 1)
# __version__ = '0.0.1'
def get_version_string():
    if isinstance(version_tuple[-1], basestring):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))
__author__ = 'Oscar Sánchez Jara <osanchez@rcp.pe>'
__since__ = '2016-11-28'
__version__ = get_version_string()
__version_api__ = '1'