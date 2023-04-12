word_1 = 'hello'
word_2 = 'hello'

print(f"word_1 {id(word_1)} word_2 {id(word_2)}")
print(word_1 is word_2)

num = 1
print(id(num))
num += 1
print(id(num))