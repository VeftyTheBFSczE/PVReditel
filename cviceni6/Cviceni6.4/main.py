import random


def to_uppercase(text):
    return text.upper()


def replace_spaces_with_smiley(text):
    return text.replace(' ', '( ͡° ͜ʖ ͡°)')


def replace_v_with_w(text):
    return text.replace('V', 'W').replace('v', 'w')


def add_asterisks(text):
    return f'*{text}*'


def replace_punctuation(text):
    return text.replace('?', '???').replace('!', '!!!!!')


funky_functions = [
    to_uppercase,
    replace_spaces_with_smiley,
    replace_v_with_w,
    add_asterisks,
    replace_punctuation
]


def funky_format(text):
    for _ in range(3):
        func = random.choice(funky_functions)
        text = func(text)
    return text

# Testovací kód
print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))
print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))
print(funky_format("Ahoj Karle! Pudeme dnes do kina?"))