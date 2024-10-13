string = 'label'
new_string = ''

for i in string:
    new_string = new_string + chr(ord(i) ^ 13)

print(new_string)