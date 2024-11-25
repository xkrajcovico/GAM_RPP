def my_upper(text):
    out = ''
    for znak in text:
        if ord(znak) >= 97:
            out += chr(ord(znak) - 32)
        else:
            out += znak
    print(out)
my_upper(str(input()))