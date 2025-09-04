def is_pangram(sentence):
    # Input string
    s = sentence
    # s = "The quick brown fox jumps over the lazy dog"
    
    # Initialize bitmask for tracking found letters
    f = 0
    
    # Loop through each character in lowercase string
    for char in s.lower():
        if char.isalpha():  # Check if the character is alphabetic
            f |= 1 << (ord(char) - ord('a'))  # Set corresponding bit for letter
        
        if f == (1 << 26) - 1:  # All letters found
            return True  # It's a pangram
            break
    else:
        return False  # Not a pangram    