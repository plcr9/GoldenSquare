from lib.phonebook import Phonebook

'''Initially, there are no phone numbers'''
def test_initially_has_no_numbers():
    phone_book = Phonebook()
    assert phone_book.list_numbers() == []

'''When diary entry added with no phone number, no phone numbers are reflected in the list'''
def test_adds_entry_with_no_numbers():
    phone_book = Phonebook()
    phone_book.extract_numbers("My friend's number is not relevant here.")
    assert phone_book.list_numbers() == []