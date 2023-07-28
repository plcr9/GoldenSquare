from lib.colours import ColourChecker

def test_colour_is_in_array():
    colours = ColourChecker()
    colours = ['red', 'green', 'blue']
    assert 'green' in colours

