# Resolve the problem!!
import re


def run():
    # Start coding here
    with open('src/encoded.txt', mode='r', encoding='utf-8') as f:
        result = ''.join(re.findall('[a-z]', f.read()))
    print(result)

if __name__ == '__main__':
    run()
