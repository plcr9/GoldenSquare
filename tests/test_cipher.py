from lib.cipher import *

def test_cipher():
    result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_cipher_decode():
    result = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert result == "theswiftfoxjumpedoverthelazydog"