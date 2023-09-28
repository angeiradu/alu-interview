#!/usr/bin/python3
# the amount of rainwater retained between the walls.
def rain(walls):
    if not walls:
        return 0
    
    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    total_rainwater = 0
    
    while left < right:
        if walls[left] <= walls[right]:
            left_max = max(left_max, walls[left])
            total_rainwater += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            total_rainwater += right_max - walls[right]
            right -= 1
    
    return total_rainwater
