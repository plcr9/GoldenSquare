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

'''When diary entry added with phone number, phone number is reflected in list'''
def test_extracts_numbers_from_single_entry():
    phone_book = Phonebook()
    phone_book.extract_numbers("My friend's number is 07000000000.")
    assert phone_book.list_numbers() == ['07000000000']

'''When three diary entries with phone numbers added'''
def test_extracts_numbers_from_multiple_entries():
    phone_book = Phonebook()
    phone_book.extract_numbers("Dale's number is 07000000001")
    phone_book.extract_numbers("Janet's number is 07000000002")
    phone_book.extract_numbers("Daisy's number is 07000000003")
    assert phone_book.list_numbers() == ["07000000001", "07000000002", "07000000003"]

'''When an entry with multiple numbers in it is added, all phone numbers are reflected in the list'''
def test_extracts_multiple_numbers_from_single_entry():
    phone_book = Phonebook()
    phone_book.extract_numbers("Dale's number is 07000000001 and Janet's number is 07000000002")
    assert phone_book.list_numbers() == ["07000000001", "07000000002"]

'''When entry with 11 digit number added that does not start with zero, it is ignored in the numbers list'''
def test_ignores_numbers_that_do_not_start_with_zero():
    phone_book = Phonebook()
    phone_book.extract_numbers("My friend's number is 77000000000")
    assert phone_book.list_numbers() == []