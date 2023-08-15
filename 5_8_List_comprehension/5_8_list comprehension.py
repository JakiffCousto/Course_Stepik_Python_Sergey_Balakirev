A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
A = [[x**2 for x in row] for row in A]
a = [x**2
     for row in A
     for x in row]
print(A)
print(a)