def password_is_valid(password):
	if (len(password)>8 and password != None and 
		any(c.islower() for c in password) and
		any(c.isupper() for c in password) and
		any(i.isdigit() for i in password)):
		print('Password is valid')    
		return 'Password is valid'							
	else:
		raise AssertionError 
		
def password_is_ok(password):
    count = 0
    if len(password)>8:
        count +=1
    if password != None:
        count +=1
    if any(c.islower() for c in password):
        count +=1
    if any(c.isupper() for c in password):
        count +=1
    if any(i.isdigit() for i in password):
        count +=1
    if count >= 3:
        print('Password is okay')
        return 'Password is okay'
    else:
        raise AssertionError
    