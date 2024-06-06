#!/usr/bin/env python3

from user import User

class TestUser:
    '''Class "User" in user.py'''

    def test_is_class(self):
        ''' a class.'''
        assert(object in User.__bases__)

    def test_initializes_with_names(self):
        ''' first and last name.'''
        the_user = User("My", "User")
        assert((the_user.first_name, the_user.last_name) == ("My", "User"))