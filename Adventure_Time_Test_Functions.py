""" Test Functions created for Adventure_Time. Testing some of the functions that require input in the program. 
"""

assert isinstance(yes_no, list)
""" Checks to see if options are in a list. """

def test_choice_1_input():
    """ Tests if input is a string. """
    assert isinstance(response, str)
    assert callable(choice_1)

def test_choice_5_input():
    """ Tests input type for choice_5 function. """
    options_of_choice_5 = answer_choices
    assert isinstance(options_of_choice_5, list)
    assert callable(choice_5)
    
def test_restart():
    """ Tests functionality of restart function. """
    assert callable(restart)  