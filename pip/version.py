#!/usr/bin/env python
# encoding: utf-8


VERSION = (1, 0, 2)


from os.path import abspath, dirname
from subprocess import Popen, PIPE


__here__ = abspath(dirname(__file__))


def _check_output(*cmd):
    p = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=__here__)
    return p.communicate()[0].rstrip('\n')


# PEP8 hates me
_gitsha = lambda : _check_output('git', 'rev-parse',    'HEAD')
_gitbrc = lambda : _check_output('git', 'symbolic-ref', 'HEAD').replace('refs/heads/', '')


def version():
    return '.'.join((str(i) for i in VERSION))


def version_verbose():
    res = 'pip version %s' % version()
    try:
        sha = _gitsha() ; brc = _gitbrc()
        if sha:
            res = '%s  (%s:%s)' % (res, brc, sha[:8])
    except:
        pass

    return res


__all__ = (VERSION, version, version_verbose)


if __name__ == '__main__':
    print version_verbose()
