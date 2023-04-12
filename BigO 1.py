#   a time complexity problem from Cracking the Coding Interview
#   what is the time complexity of an algorithm that counts the total possible permutations of a string?
#   answer: O(pow(n, 2) * n!)

count = 1


def permutation(word, prefix):
    # print(f"word {word}, prefix {prefix}")
    global count
    if len(word) == 0:
        count += 1
        # print(prefix)
    else:
        for i in range(len(word)):
            rem = word[0:i] + word[i + 1:]
            permutation(rem, prefix + word[i])


permutation("abcdefghij", "")
print(f"count {count}")