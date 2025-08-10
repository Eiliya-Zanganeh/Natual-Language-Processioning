import re


def clean(text):
    return re.sub(r'\d+', '', text)

if __name__ == '__main__':
    print(clean("I love NLP! 123 "))