string = ':3 ' * 99999
string += ':3'
with open('end.txt', 'w') as f:
    f.write(string)
