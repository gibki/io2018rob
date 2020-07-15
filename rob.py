n, t = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]

# reduce problem space to cases where n % 4 = 0
program_displacement_x, program_displacement_y = 0, 0
if n % 4 == 1 or n % 4 == 3:
    n, d = 4 * n, 4 * d
elif n % 4 == 2:
    n, d = 2 * n, 2 * d
else:
    program_displacement_x = sum(d[1::4]) - sum(d[3::4])
    program_displacement_y = sum(d[0::4]) - sum(d[2::4])


program_length = sum(d) + n  # don't forget about turn cost

cycle_count = t // program_length
leftover_t = t % program_length
leftover_x, leftover_y = x - cycle_count * program_displacement_x, y - cycle_count * program_displacement_y


def count_visits_in_line(distance, point, program_displacement, cycle_count):
    if program_displacement < 0:
        program_displacement *= -1
        point = -point + distance -  1

    if point < 0:
        return 0

    count_left_boundary = min(cycle_count, point // program_displacement + 1)
    count_right_boundary = min(cycle_count, max(0, (point - distance) // program_displacement + 1))

    return count_left_boundary - count_right_boundary


visit_counter = 0

for distance in d:
    if program_displacement_x == 0:
        if x == 0:
            if program_displacement_y == 0:
                if 0 <= y < distance:
                    visit_counter += cycle_count
            else:
                visit_counter += count_visits_in_line(distance, y, program_displacement_y, cycle_count)

    else:
        if x % program_displacement_x == 0:
            visit_cycle = x // program_displacement_x
            visit_y = y - visit_cycle * program_displacement_y
            if 0 <= visit_cycle < cycle_count and \
               0 <= visit_y < distance:
                visit_counter += 1

    # move robot
    y -= distance
    # turn robot right
    x, y = -y, x
    # dont forget to turn the displacement vector for the next instruction
    program_displacement_x, program_displacement_y = -program_displacement_y, program_displacement_x


instruction_index = 0
while leftover_t > 0:
    distance = min(leftover_t, d[instruction_index])

    if leftover_x == 0 and 0 <= leftover_y < distance:
        visit_counter += 1

    leftover_y -= distance
    leftover_x, leftover_y = -leftover_y, leftover_x

    instruction_index += 1
    leftover_t -= distance + 1


if (leftover_x, leftover_y) == (0, 0):
    visit_counter += 1


print(visit_counter)
