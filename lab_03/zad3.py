import os
import sys

word = 'na'
first_file = 'a.txt'

def number_of_words(filepath, word):
    print("PID:", os.getpid(), filepath)
    word_count = 0

    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()

    for line in lines:
        if line.startswith('\\input'):
            new_path = line.removeprefix('\\input{').removesuffix('}\n')
            pid = os.fork()
            if pid > 0:
                continue
            else:
                sys.exit(number_of_words(new_path, word))
        else:
            words = line.lower().split()
            word_count += words.count(word.lower())
    while True:
        try:
            _, exit_status = os.wait()
            if os.WIFEXITED(exit_status):
                word_count += os.WEXITSTATUS(exit_status)
        except OSError:
            break

    return word_count


result = number_of_words(first_file, word)

print(result)