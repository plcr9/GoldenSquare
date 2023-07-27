from lib.gratitudes import Gratitudes

'''It should append a string to the initial part of the statement'''
def append_string_to_gratitude():
    gratitude = Gratitudes()
    assert gratitude.append() == ""

'''add strings to the original statement'''
def add_strings_to_gratitudes_statement():
    gratitude = Gratitudes()
    gratitude.add("small ")
    gratitude.add("mercies")
    assert gratitude.output() == "small mercies"

'''format string output'''
def format_gratitudes_statement_string():
    gratitude = Gratitudes()
    gratitude.format("small ")
    gratitude.format("mercies")
    assert gratitude.format() == "Be grateful for: small mercies"