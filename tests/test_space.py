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
