import re

def assess_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 12
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Calculate strength score
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on the strength score
    if strength_score == 5:
        feedback = "Very Strong"
    elif strength_score == 4:
        feedback = "Strong"
    elif strength_score == 3:
        feedback = "Moderate"
    elif strength_score == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    return feedback

# Example usage
password = input("Enter a password to assess its strength: ")
strength = assess_password_strength(password)
print(f"Password strength: {strength}")
