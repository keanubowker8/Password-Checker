from password import password_is_valid, password_is_ok
import pytest
def test_password_is_valid():
	"""test that exception is raised for invalid passwords"""
	with pytest.raises(Exception):
		assert password_is_valid('qqqqqqqq') == Exception('Password has to be longer than 8 characters')
		assert password_is_valid('') == Exception('Password cannot be empty')
		assert password_is_valid('QQQQQQQQQ') == Exception('Password has to contain lowercase')
		assert password_is_valid('qqqqqqqqq') == Exception('Password has to contain uppercase')
		assert password_is_valid('Qqqqqqqqq') == Exception('Password has to contain a digit')

	"""test that valid passwords work"""	
	assert password_is_valid('Q8qqqqqqqq') == True


def test_password_is_okay():
	"""test that exception is raised for invalid passwords"""
	with pytest.raises(Exception):
		assert password_is_ok('qqqqqqqq') == Exception('Password  either has to contain a digit  \n  or password has to contain uppercase \n or password has to contain lowercase') 

	with pytest.raises(Exception):
		assert password_is_ok('') == Exception('Password  either has to contain a digit  \n  or password has to contain uppercase \n or password has to contain lowercase') 

	"""test that valid passwords work"""
	assert password_is_ok('Q8qqqqqqqq') == True
	assert password_is_ok('q8qqqqqqqq') == True
	assert password_is_ok('Qqqqqqqqqq') == True
	assert password_is_ok('qqqqqqqqqq') == True






