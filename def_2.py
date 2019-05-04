#
#
#
#

sample_list = [4, 100, 30, 43, 57, 32, 90, 77]

total = sum(sample_list) / len(sample_list)

print(total)


def main():
    python = ('Python', 1991)
    ruby = ('Ruby', 1995)
    go = ('Go', 2009)

    programming_lang = (python,ruby,go)

    for lang in programming_lang:
        name, year = lang
        print(name, year, '年生まれ')


if __name__ == "__main__":
    main()
