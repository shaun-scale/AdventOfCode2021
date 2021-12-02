num_increasing = 0

with open('data.txt') as file:
  arr = [int(l) for l in file]
  for i in range(len(arr) - 2):
    if (sum(arr[i+1:i+4]) > sum(arr[i:i+3])):
      num_increasing += 1

print(num_increasing)