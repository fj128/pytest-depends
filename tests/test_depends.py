# -*- coding: utf-8 -*-
from __future__ import print_function, division
import pytest

def test_fixture_reordering(testdir):
    '''See that pytest reorders tests based on fixtures in the way we expect'''

    True and testdir.makepyfile('''
    import pytest

    @pytest.fixture(scope='session')
    def sf():
        pass
    
    class TestCls(object):
        def test1():
            pass
        def test2(sf):
            pass
        def test3():
            pass
    
    def test_fn1(sf):
        pass
        
    def test_fn2():
        pass
    ''')

    False and testdir.makepyfile('''
    def test_fn1():
        pass
    ''')

    items = testdir.genitems([testdir.getpathnode('.')])
    print('!!!!', items)
    assert False




@pytest.mark.skip
def test_bar_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_sth(bar):
            assert bar == "europython2015"
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--foo=europython2015',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_sth PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


@pytest.mark.skip
def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'depends:',
        '*--foo=DEST_FOO*Set the value for the fixture "bar".',
    ])


@pytest.mark.skip
def test_hello_ini_setting(testdir):
    testdir.makeini("""
        [pytest]
        HELLO = world
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.fixture
        def hello(request):
            return request.config.getini('HELLO')

        def test_hello_world(hello):
            assert hello == 'world'
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_hello_world PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
