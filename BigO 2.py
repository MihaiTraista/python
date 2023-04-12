#   what is the runtime of this function?
#   O(b)

def product(a, b):
    result = 0
    for i in range(b):
        result += a
    return result


print(f"product(3, 4) {product(3, 4)}")
