def password_is_valid(password):
    if (len(password)>8):
        if(password != None):
            if(any(c.islower() for c in password)):
                if(any(c.isupper() for c in password)):
                    if(any(i.isdigit() for i in password)):
                        return True
                    else:
                        raise Exception('Password has to contain a digit')
                else:
                    raise Exception('Password has to contain uppercase')
            else:
                raise Exception('Password has to contain lowercase')
        else:
            raise Exception('Password cannot be empty')

    else:
        raise Exception('Password has to be longer than 8 characters') 
        
def password_is_ok(password):
    count = 0
    if len(password)>8:
        count +=1
        if password != None:
            count +=1
            if any((c.islower() for c in password) or (any(c.isupper() for c in password)) or (i.isdigit() for i in password)):
                count +=1
    
    if count >= 3:
        return True
    else:
        raise Exception('Password  either has to contain a digit  \n  or password has to contain uppercase \n or password has to contain lowercase') 



    
