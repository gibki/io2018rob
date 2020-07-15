n, t = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
x, y = [int(x) for x in input().split()]


NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3


robot_x, robot_y = 0, 0
robot_direction = NORTH


visit_counter = 0

instruction_index = 0
while t > 0:
    distance = d[instruction_index]

    # execute the next instruction
    while distance > 0 and t > 0:
        # check if we are visiting the point
        if (robot_x, robot_y) == (x, y):
            visit_counter += 1

        # move the robot
        if robot_direction == NORTH:
            robot_y += 1
        if robot_direction == EAST:
            robot_x += 1
        if robot_direction == SOUTH:
            robot_y -= 1
        if robot_direction == WEST:
            robot_x -= 1

        # mark step as completed
        distance -= 1
        # movement cost
        t -= 1


    # turn the robot
    robot_direction = (robot_direction + 1) % 4
    # pick up the next instruction
    instruction_index = (instruction_index + 1) % n
    # right turn cost
    t -= 1


# edge case at the end
if (robot_x, robot_y) == (x, y):
    visit_counter += 1


print(visit_counter)
