

PASSWORD_POLICY = (
    "Password Policy:\n"
    "1. Minimum length: 8 characters\n"
    "2. At least one lowercase letter\n"
    "3. At least one uppercase letter\n"
    "4. At least one digit\n"
    "5. No whitespace allowed"
)


# Check Valid
# will return:
# valid_status as bool
# Rule broken as list
# strength as string
def check_valid(pw):
    valid_status = True
    rule_broken = []
    strength_value = 0

    # 1. Minimum length: 8 characters
    if len(pw) >= 8:
        strength_value += 1
    else:
        rule_broken.append("Minimum 8 Characters")

    # 2. At least one lowercase letter
    if any(char.islower() for char in pw):   # checks if at least one item in the iterable is True 
        strength_value += 1
    else:
        rule_broken.append("1 Lowercase Letter")

    # 3. At least one uppercase letter
    if any(char.isupper() for char in pw):
        strength_value += 1
    else:
        rule_broken.append("1 Uppercase Letter")
    
    # 4. At least one digit
    if any(char.isdigit() for char in pw):
        strength_value += 1
    else:
        rule_broken.append("Have a number")

    # 5. Whitespace
    if any(char.isspace() for char in pw):
        strength_value += 1
    else:
        rule_broken.append("Has WhiteSpace")

    # Password Strength
    if strength_value < 2:
        strength = "Weak"
    elif strength_value > 2 and strength_value < 4:
        strength = "Moderate"
    else:
        strength = "Strong"
        valid_status = False

    return valid_status, rule_broken, strength





# User Password Enter
def user_enter():
    print(PASSWORD_POLICY)
    password = input("Enter your password:")
    valid_status = False

    while True: 
        valid_status, rule_broken, strength = check_valid(password)
        
        if valid_status == True:
            print(f"Try again!, you didn't satisfy these rules {rule_broken}")
            
    
    
    print(f"Valid\nstrength_value{strength} Password")


user_enter()




