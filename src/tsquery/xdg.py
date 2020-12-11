import logging
import os
from typing import Literal


logger = logging.getLogger(__name__)


_XDG_HOME_T = Literal['XDG_CONFIG_HOME', 'XDG_DATA_HOME']
_XDG_DIRS_T = Literal['XDG_CONFIG_DIRS', 'XDG_DATA_DIRS']


def get_xdg_home(key: _XDG_HOME_T) -> Path:
    """ Implement XDG Base Directory Specification
    See: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
    """
    if key == 'XDG_CONFIG_HOME':
        default = Path.home() / '.config'
    elif key == 'XDG_DATA_HOME':
        default = default = Path.home() / '.local/share'
    else:
        raise ValueError(f'Unrecognized XDG directory: {key}')

    xdg_path = Path(os.getenv(key, default))
    logger.debug('%s -> %s', key, xdg_path)
    return xdg_path


def get_xdg_dirs(key: _XDG_DIRS_T) -> List[Path]:
    """ Implement XDG Base Directory Specification
    See: https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
    """
    if key == 'XDG_CONFIG_DIRS':
        default = [
            Path('/etc/xdg')
        ]
    elif key == 'XDG_DATA_DIRS':
        default = [
            Path('/usr/share'),
            Path('/usr/local/share')
        ]
    else:
        raise ValueError(f'Unrecognized XDG directory: {key}')

    env_val = os.getenv(key)
    if env_val is None:
        paths = default
    else:
        paths = list(map(Path, env_val.split(':')))
    logger.debug('%s -> %s', key, ' : '.join(map(str, paths)))
    return paths

