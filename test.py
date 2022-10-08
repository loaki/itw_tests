from collections import Counter
import numpy as np

def count_occurrences_in_text(word, text):
    """
    Return the number of occurrences of the passed word (case insensitive) in text
    """
    i = 0
    word_count = 0
    len_text = len(text)
    separators = " .,!?()«»:\"\n\u201c\u201d"

    # text markdown 
    while text[i] == text[-1 - i] and (text[i] == "'" or text[i] == '_'):
        i += 1
    # count matching word in text separated by separator
    prev_separator = False
    for t in re.split(word.lower(), text[i:-i].lower() if i > 0 else text.lower()):
        if (not t or t[0] in separators) and prev_separator == True:
            word_count += 1
        if not t or t[-1] in separators:
            prev_separator = True
        else:
            prev_separator = False
    return word_count

from collections import Counter
if __name__ ==  '__main__':
    import re
    text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""

    # index = 0
    # text = "John O(maley is my friend"
    # word = 'maley is'
    # print(len(re.split(word.lower(), text.lower())))
    # print((re.split(fr"{word.lower()}\b", text.lower())))
    print(re.search('i', text))
    # print(text[:-1])
    # print(count_occurrences_in_text('georges', text))
 