
def validate_indian_mobile_number(mobile_number):
    """
    Validates if the given mobile_number is a valid Indian mobile number.
    - Starts with 6, 7, 8, or 9
    - Contains exactly 10 digits
    Returns 'valid mobile number' or 'invalid mobile number'
    """
    if isinstance(mobile_number, str) and mobile_number.isdigit() and len(mobile_number) == 10:
        if mobile_number[0] in {'6', '7', '8', '9'}:
            return 'valid mobile number'
    return 'invalid mobile number'

# Take input from user
user_input = input("Enter mobile number: ")
result = validate_indian_mobile_number(user_input)
print(result)





