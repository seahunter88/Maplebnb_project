from lib.space import Space

'''
space initialises with id, title, price and description.
'''

def test_init():
    space = Space(1, 'test space', 100, 'This is a test space.', 1)
    assert space.id == 1
    assert space.title == 'test space'
    assert space.price == 100
    assert space.description == 'This is a test space.'
    assert space.user_id == 1

'''
Testing that two instances of spaces are identical.
'''

def test_spaces_are_equal():
    space = Space(1, 'test space', 100, 'This is a test space.', 1)
    space_2 = Space(1, 'test space', 100, 'This is a test space.', 1)
    assert space == space_2


'''
Testing that space is formatting in a readable way.
''' 

def test_make_it_a_string():
    space = Space(1, 'test space', 100, 'This is a test space.', 1)
    assert str(space)== "Space(1, test space, 100, This is a test space., 1)"

"""
Testing space title must be between 4 and 20 characters in length
"""
def test_title_length_is_appropriate():
    space = Space(1, 'test house', 1, 'desc', 1)
    assert space.check_title() == True

def test_title_length_too_short():
    space = Space(1, 't', 1, 'desc', 1)
    assert space.check_title() == False

def test_title_length_too_long():
    space = Space(1, 'abcdabcdabcdabcdabcda', 1, 'desc', 1)
    assert space.check_title() == False

"""
Testing space price is a number
"""
def test_price_is_number():
    space = Space(1, 'test house', 100, 'desc', 1)
    assert space.check_price() == True

"""
test space price is at least 20
"""
def test_price_is_above_at_least_20():
    space = Space(1, 'test house', 20, 'desc', 1)
    assert space.check_price() == True

"""
test space description is over 3 words
"""
def test_desc_more_than_3_words():
    space = Space(1, 'test house', 20, 'this is my description which passses', 1)
    assert space.check_description() == True

def test_desc_less_than_3_words():
    space = Space(1, 'test house', 20, 'Description', 1)
    assert space.check_description() == False