import pytest

@pytest.fixture(scope="class")
def example_fixture():
    print("this will run first as its in fixture")
    yield
    print("this will run last as its after yield")

@pytest.fixture()
def another_fixture():
    print("this is another fiture returning data")
    return ['chaya','Bhagavat','chayabhagavath@gmail.com']

@pytest.fixture(params=[('chaya','Bhagavat'),('Mahesh','rayar'),('Kridha','Rayar')])
def family_name(request):
    return request.param