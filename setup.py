#!/usr/bin/env python
# encoding: utf-8

import sys
from os.path import abspath, dirname, join as pjoin


# If you change this version, change it also in docs/conf.py
version = '1.0.2'


here = abspath(dirname(__file__))

index_filename = pjoin(here, 'docs', 'index.txt')
news_filename  = pjoin(here, 'docs', 'news.txt')


# Remove the toctree from the sphinx index, as it breaks long_description
index = open(index_filename).read()
news  = open(news_filename).read()

index_a, index_toc, index_b = index.split('split here', 2)


description = 'pip installs packages. Python packages. An easy_install replacement'
long_description = '''%(index_a)s

The main website for pip is `www.pip-installer.org
<http://www.pip-installer.org>`_.  You can also install
the `in-development version <https://github.com/pypa/pip/tarball/develop#egg=pip-dev>`_
of pip with ``easy_install pip==dev``.

%(index_b)s

%(news)s
'''


classifiers = (
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.4',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
)


kw = {
    'name'                 : 'pip',
    'version'              : version,

    'description'          : description,
    'long_description'     : long_description % locals(),

    'author'               : 'The pip developers',
    'author_email'         : 'python-virtualenv@groups.google.com',

    'license'              : 'MIT',

    'keywords'             : 'easy_install distutils setuptools egg virtualenv',
    'classifiers'          : classifiers,

    'url'                  : 'http://www.pip-installer.org',

    'packages'             : ('pip', 'pip.commands', 'pip.vcs'),

    'test_requires'        : ('nose', 'virtualenv>=1.6', 'scripttest>=1.1.1', 'mock'),
    'test_suite'           : 'nose.collector',

    'entry_points'         : {
        'console_scripts'  :
        (
            'pip    = pip:main',
            'pip-%s = pip:main' % sys.version[:3],
        )
    },

    'zip_safe'             : False,
}


from setuptools import setup
setup(**kw)
