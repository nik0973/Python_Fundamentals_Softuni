def pass_valid(text: str):
    log_errors = []
    if len(text) < 6 or len(text) > 10:
        log_errors.append("Password must be between 6 and 10 characters")
    if not text.isalnum():
        log_errors.append("Password must consist only of letters and digits")
    counter = 0
    for character in text:
        if character.isdigit():
            counter += 1
    if counter < 2:
        log_errors.append("Password must have at least 2 digits")
    return log_errors

password = input()
errors = pass_valid(password)
if not errors:
    print("Password is valid")
else:
    print('\n'.join(errors))