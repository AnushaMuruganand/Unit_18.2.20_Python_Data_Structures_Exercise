def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    # ord() function takes string argument of a single Unicode character and return its integer Unicode code point value.

    # Inorder to change the ASCII code we get from ord() to char position as ("a"=1, "b"=2, etc). Lets take ord('a') which is 97 and subtract it by 1 and store in a variable.
    # Then use that to subtract it from other ord() 

    DIFF = ord("a") - 1

    total = sum((ord(c) - DIFF) for c in word.lower())

    return total % 2 != 0