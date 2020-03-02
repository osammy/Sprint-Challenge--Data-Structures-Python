import time

start_time = time.perf_counter()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1 = set(names_1)
names_2 = set(names_2)
duplicates = list(names_1.intersection(names_2))

end_time = time.perf_counter()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish? There are no restrictions on techniques or data

# structures, but you may not import any additional libraries that you did not write yourself.