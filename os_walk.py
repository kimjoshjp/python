#
#
#
#
import os

target = '/Users/kazunorif/bbpy'
def directory_list(target_path):
    for root, dirs, files in os.walk(target_path):
        print(root)
        for dirc in dirs:
            print('\t', dirc)
        
        for file in files:
            print('\t', file)




if __name__ == "__main__":
    directory_list(target)

import os


def search(target_path, search_text):
    for root, dirna, files in os.walk(target_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, encoding='utf-8') as f:
                if search_text in f.read():
                    print(filename)


if __name__ == '__main__':
    search('input', '出席')