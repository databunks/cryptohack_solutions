v = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
output_string = ""

for i in v:
    output_string = output_string + str(chr(i))

print(output_string)