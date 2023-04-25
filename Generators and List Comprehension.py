"""

A list comprehension returns a complete list of elements upfront.
A generator expression returns a list of elements, one at a time, based on request.
A list comprehension returns an iterable. It means that you can iterate over the result of a list comprehension again and again.
However, a generator expression returns an iterator, specifically a lazy iterator. It becomes exhausting when you complete iterating over it.

"""

a = 100
#   this is a generator expression or a generator


def my_yield(arg):
    global a
    yield arg + 1
    a += 1
    yield arg + 2
    a += 1
    yield arg + 3
    a += 1


print("type of my_yield is", type(my_yield(10)).__name__)
for num in my_yield(10):
    print(num, a)
print(f"a after yield {a}")

example_generator_expression = (n ** 2 for n in range(5))

A = [1, 3, 5, 7]
gen = (a for a in A if a > 4)
for g in gen:
    print("g = ", g)

#   generator in if statement with the keyword any

nums = [9, 7, 1, 3, 5]
if any(n < 4 for n in nums):
    #   this will run once
    print("found number less than 4")


#   this is a list comprehension
#   an expression (or a term) followed by a for loop and an if clause
squares_list_comprehension = [n ** 2 for n in range(5)]

#   find movies released before 2000
movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("Gattaca", 1997)]
old_movies = [tup[0] for tup in movies if tup[1] < 2000]
print(f"old_movies {old_movies}")
