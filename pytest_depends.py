# -*- coding: utf-8 -*-

import pytest
import textwrap

def pytest_configure(config):
    'Add help displayed by `py.test --markers` command'

    config.addinivalue_line('markers',
        'sequential: tests in the marked class are always executed in the order of definition. '
        'Provided by pytest-depends.')
    config.addinivalue_line('markers',
        'depends(test1, test2, ...): marks the test as depending on specified tests. '
        'Provided by pytest-depends.')


def pytest_collection_modifyitems(session, config, items):
    print('????')

def pytest_addoption(parser):
    group = parser.getgroup('depends')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2016',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo
