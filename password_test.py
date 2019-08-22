from password import password_is_valid, password_is_ok
import pytest
def test_password_is_valid():
	"""test that exception is raised for invalid passwords"""
	with pytest.raises(Exception):
		password_is_valid('qqqqqqqqq')

	with pytest.raises(Exception):
		password_is_valid('')

	with pytest.raises(Exception):
		password_is_valid('Qqqqqqqqq')

	"""test that valid passwords work"""	
	password_is_valid('Q8qqqqqqqq') == True


def test_password_is_okay():
	"""test that exception is raised for invalid passwords"""
	with pytest.raises(Exception):
		password_is_ok('qqqqqqqq')

	with pytest.raises(Exception):
		password_is_ok('')

	"""test that valid passwords work"""
	password_is_ok('Q8qqqqqqqq') == True
	password_is_ok('q8qqqqqqqq') == True
	password_is_ok('Qqqqqqqqqq') == True
	password_is_ok('qqqqqqqqqq') == True






