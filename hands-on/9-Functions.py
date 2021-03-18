def add(a, b):
    return a + b

print(add(2,4)),

# help about function
help(add)

def dummy():
    print("Mj")

val = dummy()
print(type(val))

album_ratings = [10.0, 2, 5.2, 5.7]
sum(album_ratings)
len(album_ratings)

album_ratings.sort()
album_ratings


def print_elements(album_ratings):
    for i in album_ratings:
        print(i)

print_elements(album_ratings)