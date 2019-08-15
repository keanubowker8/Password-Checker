from password import password_is_valid, password_is_ok

def test_password_is_valid():
	try:
		assert password_is_valid('QpA9Aapaaa') == 'Password is valid'
		assert password_is_valid('Q1Aap9aaa') == 'Password is valid'
		assert password_is_valid('QAAaupa8a') == 'Password is valid'
	except AssertionError as e:
		print('''               password should be larger than 8 chars
               password should not be null
               password should have at least one uppercase letter
               password should have at least one lowercase letter
               password should have at least one number''')

	
def test_password_is_okay():
    try:
        assert password_is_ok('QpAAapaa') == 'Password is okay'
        assert password_is_ok('Q1AAapaaa') == 'Password is okay'
        assert password_is_ok('QAAapa8a') == 'Password is okay'
    except AssertionError as e:
        print('''         Password must meet at least 3 of these conditions.       
		    Password should be larger than 8 characters.
            Password should not be null.
            Password should have at least one uppercase letter.
            Password should have at least one lowercase letter.
            Password should have at least one number.''')
        print(e)


