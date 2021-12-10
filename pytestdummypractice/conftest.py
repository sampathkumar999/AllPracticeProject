import pytest

@pytest.fixture(scope='class')
def setup():
    print('I will invoke the browser and open the url')
    yield
    print("i will close all the windows and browser")



@pytest.fixture()
def dataload():
    print('This method contains test data')
    return ['sampath', 'kumar', 'bodhula']


@pytest.fixture(params=['chrome','firefox','IE'])
def paramsdata(request):
    return request.param
