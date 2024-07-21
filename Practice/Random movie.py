import random

n = input("How many choices for random movies? ")
n = int(n)
movies = []

for x in range(0, n):
    x = input("Write movie: ")
    movies.append(x)

rd = random.randrange(len(movies))
print(movies[rd])
