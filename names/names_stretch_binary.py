import time

def binary_search(arr, target):
  if len(arr) == 0:
    return -1
  if arr[0] > target:
    return -1
  if arr[len(arr) - 1] < target:
    return -1
  low = 0
  high = len(arr)-1
  middle = int((high-low)/2 + low)
  while high > low:
    middle = int((high + low)/2)
    if target == arr[middle]:
        return middle
    elif target < arr[middle]:
      high = middle
    else:
      low = middle + 1
  return -1  # not found
  
start_time = time.perf_counter()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
names_1.sort()
for name_2 in names_2:
  if binary_search(names_1, name_2):
    duplicates.append(name_2)

end_time = time.perf_counter()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish? There are no restrictions on techniques or data

# structures, but you may not import any additional libraries that you did not write yourself.