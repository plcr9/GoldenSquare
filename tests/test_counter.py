from lib.counter import Counter

'''Reports a count of zero'''
def test_counter_reports_zero():
    counter = Counter()
    assert counter.report() == 'Counted to 0 so far'

'''When we add a single number to the counter. It is reflected in the final count'''
def test_counter_adds_a_single_number_to_the_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far"

'''When we add multiple numbers to the counter, show the sum of these numbers in the final count'''
def test_counter_adds_multiple_numbers_to_the_count():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far"

'''Using minus numbers'''
def test_counter_adds_a_single_minus_number_to_the_count():
    counter = Counter()
    counter.add(-2)
    assert counter.report() == "Counted to -2 so far"

'''Adding multiple negative numbers'''
def test_counter_adds_multiple_minus_numbers_to_the_count():
    counter = Counter()
    counter.add(-2)
    counter.add(-7)
    assert counter.report() == "Counted to -9 so far"
