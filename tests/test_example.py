import pytest
from pyrtt.pyrtt import Test

@pytest.mark.parametrize("read_value,return_value", [
    (1, 1), (2, 2), (3, 3)
])
def test_example(read_value, return_value):
    t = Test()
    assert read_value == return_value
