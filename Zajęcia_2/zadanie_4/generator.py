def count():
    n1 = 0
    n2 = 1
    while True:
        temp = n2
        n2 = n1 + n2
        n1 = temp
        yield n2


counter = count()

print(next(counter)) #1
print(next(counter)) #2
print(next(counter)) #3
print(next(counter)) #5
print(next(counter)) #8
print(next(counter)) #13
print(next(counter)) #21
