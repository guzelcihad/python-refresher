# Tuples are ordered sequence
# Immutable

tuple = (1, "Michael", 2.0)
tuple
print(type(tuple))

print(tuple[0])

print(tuple[-1])

tuple2 = tuple + ("hard rock", 10)
tuple2


tuple[1:2]

len(tuple2)

ratings = (5,2,1)
sortedTuple = sorted(ratings)
sortedTuple

tupleOfTuples = (1,4, ('John', 'Smith'))
tupleOfTuples

tupleOfTuples[2][1]