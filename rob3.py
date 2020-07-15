n, t = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]

# reduce problem space to n % 4 == 0
n, d = 4 * n, 4 * d

program_displacement_x = sum(d[1::4]) - sum(d[3::4])
program_displacement_y = sum(d[0::4]) - sum(d[2::4])

program_length = sum(d) + n  # dont forget turn cost
cycle_count = t // program_length
leftover_t = t % program_length


visit_counter = 0

if (program_displacement_x, program_displacement_y) == (0, 0):
    # count visits in full program cycles
    for distance in d:
        if x == 0 and 0 <= y < distance:
            visit_counter += cycle_count

        y -= distance
        x, y = -y, x
else:
    # fallback to previous algorithm
    leftover_t = t

instruction_index = 0
while leftover_t > 0:
    distance = min(leftover_t, d[instruction_index])

    if x == 0 and 0 <= y < distance:
        visit_counter += 1

    y -= distance
    x, y = -y, x

    instruction_index = (instruction_index + 1) % n
    leftover_t -= distance + 1


# edge case at the end
if (x, y) == (0, 0):
    visit_counter += 1


print(visit_counter)
