num_increasing = 0

with open('data.txt') as file:
  arr = [int(l) for l in file]
  for i in range(len(arr) - 1):
    if (arr[i + 1] > arr[i]):
      num_increasing += 1

print(num_increasing)