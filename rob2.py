n, t = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]


visit_counter = 0

instruction_index = 0
while t > 0:
    distance = min(t, d[instruction_index])

    if x == 0 and 0 <= y < distance:
        visit_counter += 1

    y -= distance
    x, y = -y, x

    instruction_index = (instruction_index + 1) % n
    t -= distance + 1


# edge case at the end
if (x, y) == (0, 0):
    visit_counter += 1


print(visit_counter)
