def words_string(s):
    """
    You will be given a string of words separated by commas or spaces.
    Your task is to split the string into words and return a list of the words.
    """
    # Step 1: Replace commas with spaces so all separators are spaces
    s = s.replace(',', ' ')

    # Step 2: Split the string on spaces
    words = s.split()

    # Step 3: Return the list of words
    return words


print(words_string('one,two,three'))       # ['one', 'two', 'three']
print(words_string('one two three'))       # ['one', 'two', 'three']
print(words_string('one, two,  three'))    # ['one', 'two', 'three']
print(words_string('  alpha,beta , gamma'))# ['alpha', 'beta', 'gamma']
print(words_string('word'))   