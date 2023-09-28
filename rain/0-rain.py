#!/usr/bin/python3
# the amount of rainwater retained between the walls.

def rain(walls):
    water_temp = 0
    water = 0
    size = len(walls)
    prev_wall = 0

    if size <= 0:
        return water_temp

    for i in range(size):

        if walls[i] >= walls[prev_wall]:
            prev_wall = i
            water_temp = 0
        else:
            water += walls[prev_wall] - walls[i]
            water_temp += walls[prev_wall] - walls[i]

    if prev_wall < size - 1:

        # Subtract last temp volume from total.
        water -= water_temp
        # Store last peak wall.
        prev_pass_peak = prev_wall
        prev_wall = size - 1

        for i in range(size - 1, prev_pass_peak, -1):

            if walls[i] >= walls[prev_wall]:
                prev_wall = i
            else:
                water += walls[prev_wall] - walls[i]

    return water
