string = "abcdefgh"
string_list = list(string)
string_list[2] = 'X'
string_list[5] = 'Y'
new_string = ''.join(string_list)

print("Original:", string)
print("Modified:", new_string)