# Link to kata: https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    tower, star, i, width = [], '*', 1, (n_floors*2)-1

    for x in range(n_floors):
        tower.append((star*i).center(width)) # Append and center the asterisk (*).
        i += 2

    return tower
