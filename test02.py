#
#

def count_words('/Users/kazu/python/words1.txt'):
    with open('/Users/kazu/python/words1.txt', 'r') as file:
        strng = file.read()
        strng_list = strng.split("")
        return len(strng_list)


print(count_words('/Users/kazu/python/words1.txt'))