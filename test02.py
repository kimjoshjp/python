#
#

def count_words(filepath):
    with open(filepath, 'r') as file:
        aaa = file.read()
        aaa_list = aaa.split(" ")
        return len(aaa_list)


print(count_words('/Users/kazu/python/words1.txt'))