l1 = [10, 20, 30, 40, 50]
result = iter(l1)

while True:
    try:
        element = next(result)
        print(element)
    except StopIteration:
        break
