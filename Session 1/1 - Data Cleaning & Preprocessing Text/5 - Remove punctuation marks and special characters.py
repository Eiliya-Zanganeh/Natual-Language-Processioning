import re


def clean(text):
    return re.sub(r'[^\w\s]', '', text)

if __name__ == '__main__':
    print(clean("I love NLP! 💙"))