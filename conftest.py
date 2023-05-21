import pytest
@pytest.yield_fixture(scope='module')
def setUptearDownClass():
    print('setUpClss activity')
    yield
    print('tearDownClass activity')
@pytest.yield_fixture()
def setUptearDown():
    print('setUp activity')
    yield
    print('tearDown activity')