def validate_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "@#$%^&+=" for c in password)
    
    return has_upper and has_lower and has_digit and has_special

while True:
   
    password = input("Enter your password: ")
    
    if validate_password(password):
        print("Password is valid.")
        break
    else:
        print("Password is invalid. Check if you have satisfied all conditions.")

