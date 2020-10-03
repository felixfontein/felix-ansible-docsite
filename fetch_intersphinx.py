#!/usr/bin/python3

import os

import conf


for name, (url, (_, cache_name)) in conf.intersphinx_mapping.items():
    source = url + 'objects.inv'
    destination = os.path.normpath(os.path.join('rst', cache_name))
    print('# {name}:'.format(name=name))
    print('curl {src} > {dst}'.format(src=source, dst=destination))
