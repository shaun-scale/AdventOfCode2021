hor = 0
depth = 0
aim = 0

with open('data.txt') as file:
  for l in file:
    [command, inc] = l.split()
    inc = int(inc)
    if command == "up":
      aim -= inc
    if command == "down":
      aim += inc
    if command == "forward":
      hor += inc
      depth += aim * inc

print(hor * depth)