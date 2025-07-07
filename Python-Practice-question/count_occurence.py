def count_leters(string):
    """
    Count the occurrence of each letter in a given string.
    
    Args:
    string (str): The input string to count letters from.
    
    Returns:
    dict: A dictionary with letters as keys and their counts as values.
    """
    count = {}
    for char in string:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert to lowercase for case-insensitive counting
            count[char] = count.get(char, 0) + 1
    return count