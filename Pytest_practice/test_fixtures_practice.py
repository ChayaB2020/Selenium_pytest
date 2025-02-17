import pytest

def test_demo(example_fixture):
    print("This is demo")

@pytest.mark.usefixtures("example_fixture")
class Test_class_fixture():
    def test_demo1(self):
        print("This is demo1")

    def test_demo2(self):
        print("This is demo2")

    def test_demo3(self):
        print("This is demo3")
    
    def test_demo4(self):
        print("This is demo4")

def test_using_fixture(another_fixture):
    print(another_fixture)