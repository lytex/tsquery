import os
#from pathlib import Path

import pytest

from tsquery.xdg import get_xdg_home, get_xdg_dirs

# NOTE: these tests will surely fail on Windows
# TODO: is there a good way to compare a PosixPath/WindowsPath to a generic Path?


def test_get_xdg_home():
    os.environ['XDG_CONFIG_HOME'] = '/foo/config'
    assert str(get_xdg_home('XDG_CONFIG_HOME')) == '/foo/config'

    del os.environ['XDG_CONFIG_HOME']
    os.environ['HOME'] = '/foo'
    assert str(get_xdg_home('XDG_CONFIG_HOME')) == '/foo/.config'

    os.environ['XDG_DATA_HOME'] = '/foo/data'
    assert str(get_xdg_home('XDG_DATA_HOME')) == '/foo/data'

    del os.environ['XDG_DATA_HOME']
    os.environ['HOME'] = '/foo'
    assert str(get_xdg_home('XDG_DATA_HOME')) == '/foo/.local/share'

    with pytest.raises(ValueError, match='Unrecognized XDG directory: foo'):
        get_xdg_home('foo')


def test_get_xdg_dirs():
    os.environ['XDG_CONFIG_DIRS'] = '/foo/config1:/foo/config2'
    assert tuple(map(str, get_xdg_dirs('XDG_CONFIG_DIRS'))) == ('/foo/config1', '/foo/config2')

    del os.environ['XDG_CONFIG_DIRS']
    assert tuple(map(str, get_xdg_dirs('XDG_CONFIG_DIRS'))) == ('/etc/xdg',)

    os.environ['XDG_DATA_DIRS'] = '/foo/data1:/foo/data2'
    assert tuple(map(str, get_xdg_dirs('XDG_DATA_DIRS'))) == ('/foo/data1', '/foo/data2')

    del os.environ['XDG_DATA_DIRS']
    assert tuple(map(str, get_xdg_dirs('XDG_DATA_DIRS'))) == ('/usr/share', '/usr/local/share')

    with pytest.raises(ValueError, match='Unrecognized XDG directory: foo'):
        get_xdg_dirs('foo')

