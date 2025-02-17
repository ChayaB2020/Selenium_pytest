import pytest

def test_first():
    print('hello')
    #assert 'true'

def test_second():
    my_str='Hi'
    assert my_str == 'Hi', 'both strings are not matching'

@pytest.mark.new
def test_family(family_name):
    print(family_name)