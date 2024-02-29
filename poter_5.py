def is_consonant(char):
    """Check if a character is a consonant."""
    return char.lower() not in 'aeiou'

def get_measure(word):
    """Calculate the measure of a word, which is the number of VC sequences."""
    word = word.lower()
    count = 0
    index = 0
    while index < len(word):
        # Skip initial vowels
        while index < len(word) and not is_consonant(word[index]):
            index += 1
        # Check for consonant sequence
        if index < len(word):
            # Found a consonant, move to next vowel
            while index < len(word) and is_consonant(word[index]):
                index += 1
            # Completed a VC sequence
            count += 1
        # Skip the vowels to find the next consonant
        while index < len(word) and not is_consonant(word[index]):
            index += 1
    return count

def ends_double_consonant(word):
    """Check if a word ends with a double consonant."""
    if len(word) >= 2 and word[-1] == word[-2] and is_consonant(word[-1]):
        return True
    return False

def ends_cvc(word):
    """Check if a word ends with a consonant-vowel-consonant sequence where the final consonant is not w, x, or y."""
    if len(word) >= 3 and is_consonant(word[-3]) and not is_consonant(word[-2]) and is_consonant(word[-1]) and word[-1] not in 'wxy':
        return True
    return False

def replace_suffix(word, suffix, replacement):
    """Replace the suffix of a word with a new suffix if it ends with the specified suffix."""
    if word.endswith(suffix):
        return word[:-len(suffix)] + replacement
    return word

def porter_stemmer(word):
    """Apply the Porter Stemmer algorithm to stem a word."""
    # Step 1a
    if word.endswith('sses'):
        word = word[:-2]  # Replace by 'ss'
    elif word.endswith('ies'):
        word = word[:-2]  # Replace by 'i'
    elif word.endswith('ss'):
        pass  # Do nothing
    elif word.endswith('s'):
        word = word[:-1]  # Remove 's'

    # Step 1b
    if word.endswith('eed'):
        if get_measure(word[:-3]) > 0:
            word = word[:-1]  # Replace by 'ee'
    else:
        if ((word.endswith('ed') or word.endswith('ing')) and
                any(is_consonant(c) for c in word[:-2])):
            word = word[:-2] if word.endswith('ed') else word[:-3]
            if word.endswith(('at', 'bl', 'iz')):
                word += 'e'
            elif ends_double_consonant(word) and not word[-1] in 'lsz':
                word = word[:-1]
            elif get_measure(word) == 1 and ends_cvc(word):
                word += 'e'


    return word

def main():
    """Test the Porter Stemmer with a list of words."""
    words = ["dogs", "cats","runs", "running", "farting", "flies", "trouble", "troubling","probation","proudly", "singing", "troubled", "dies", "horses", "university", "universal", "universally","compound",  "complex", "complexity"]

    print("{:15} {:15}".format("Word", "Stemmed"))
    print("-" * 30)
    for word in words:
        stemmed_word = porter_stemmer(word)
        print("{:15} {:15}".format(word, stemmed_word))

if __name__ == "__main__":
    main()