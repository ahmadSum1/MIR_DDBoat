import pynmea2


import io
with io.open('data.txt','r', encoding='utf8') as file:
    for line in file:
        try:
            msg = pynmea2.parse(line)
            print(repr(msg))
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue