from lib.greet import greet

def test_greet_returns_name():
    result = greet("Dale")
    assert result == "Hello, Dale!"
