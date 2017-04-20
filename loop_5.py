#
#
#
#
#

original = input("Please input some sentence?: ").strip().lower()

#split sentence into words
words = original.split()

#loop thorough words and convert to pig latin
new_words = []

for lol in words:
    if lol[0] in "aeiou":
        new_word = lol + "yay"
        new_words.append(new_word)

print(new_words)