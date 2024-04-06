def convert_to_uppercase(input_str):
    return input_str.upper()



def convert_first_letters_uppercase(input_str):
    """
    Convert the first letter of each word in the input string to uppercase.
    
    Args:
        input_str (str): Input string to process.
    
    Returns:
        str: Input string with the first letter of each word in uppercase.
    """
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
