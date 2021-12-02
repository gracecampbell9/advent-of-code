# AOC Day 2

# Part 1
testcourse = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

#--------------------------
# read txt file:
with open('Day 2/input.txt', 'r') as txt_input:
    course = [line.strip().split(' ') for line in txt_input.readlines()]
    course = [(x, int(y)) for [x, y] in course]

horizontal = 0
depth = 0

for direction, courseval in course:
    if direction == "forward":
        horizontal += courseval
    elif direction == "down":
        depth += courseval
    else: 
        depth = depth - courseval

print("horizontal:",horizontal)
print("depth:",depth)

# answer 1 = horizontal * depth:
print("Part 1 answer:",depth*horizontal)

#--------------------------
horizontal = 0
depth = 0
aim = 0

for direction, courseval in course:
    if direction == "forward":
        horizontal += courseval
        depth += (aim*courseval)
    elif direction == "down":
        aim += courseval
    else: 
        aim = aim - courseval

print("horizontal:",horizontal)
print("depth:",depth)

# answer 2 = horizontal * depth:
print("Part 2 answer:",depth*horizontal)
