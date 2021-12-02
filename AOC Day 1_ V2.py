# AOC Day 1 

# open file, read depths
with open('/Users/gracecampbell/Documents/Advent of Code/Day 1/input.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]

# Part 1:
increases = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increases += 1

# Answer 1:
print(increases)

#-----------
# Part 2:

#testdepths = [200,208,210,200,200,207,240,269,260,263]

increases = 0

for i in range(3, len(depths)):
    if depths[i] > depths[i-3]:
        increases +=1

print(increases)