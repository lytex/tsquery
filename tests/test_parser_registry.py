from pathlib import Path

import pytest

from tsquery.parser_registry import (
    iter_available_parsers,
    list_available_parsers,
    ParserUnavailable,
    ParserRegistry,
)


def test_available_parsers():
    p = Path('tests/xdg-data-home/tree-sitter/parsers')

    ps1 = sorted(iter_available_parsers([p]))
    assert ps1 == sorted(p.iterdir())

    ps2 = sorted(list_available_parsers([p]))
    assert ps2 == sorted(p.iterdir())


def test_parser_registry_find():
    p = Path('tests/xdg-data-home/tree-sitter/parsers')
    registry = ParserRegistry([p])

    assert registry.find_parser_file('python') == p/'python.so'

    with pytest.raises(ParserUnavailable):
        registry.find_parser_file('quibble')


def test_parser_registry_get():
    # TODO
    pass


def test_parser_registry_query():
    # TODO
    pass
