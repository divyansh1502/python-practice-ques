import re

def count_vowels(s):
    return len(re.findall(r'[aeiouAEIOU]', s))
# Example usage:
input_string = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(input_string)}")