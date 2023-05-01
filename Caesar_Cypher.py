text = "abcABC"
secret = 10
uppercase_offset = 65
lowercase_offset = 97

list_of_characters = list(text)
encrypted = ""

for c in list_of_characters:
    num = ord(c)
    new_num = num + secret
    if c.isupper():
        new_num = (new_num - uppercase_offset) % 26 + uppercase_offset
    else:
        new_num = (new_num - lowercase_offset) % 26 + lowercase_offset
    new_c = chr(new_num)
    encrypted += new_c
    # print(f"c = {c}, num = {num}, new_num = {new_num}, new_c = {new_c}")

print(f"encrypted {encrypted}")
