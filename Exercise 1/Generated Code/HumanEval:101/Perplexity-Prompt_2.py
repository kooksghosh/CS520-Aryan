def words_string(s):
    """
    You will be given a string of words separated by commas or spaces.
    Your task is to split the string into words and return an array of the words.
    """
    # Step 1: If the string is empty, return an empty list
    if not s:
        return []

    # Step 2: Replace all commas with spaces for consistency
    s = s.replace(',', ' ')

    # Step 3: Split the string by spaces
    words = s.split(' ')

    # Step 4: Remove any empty strings from the list
    words = [word for word in words if word]

    # Step 5: Return the final list of words
    return words

# Manual tests
print(words_string('one,two,three'))       # ['one', 'two', 'three']
print(words_string('one two three'))       # ['one', 'two', 'three']
print(words_string('one, two,  three'))    # ['one', 'two', 'three']
print(words_string('  alpha,beta , gamma'))# ['alpha', 'beta', 'gamma']
print(words_string('word'))                # ['word']
print(words_string(''))                    # []