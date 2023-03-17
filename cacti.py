def cacti_number(plot):
    amount_left = 0
    x_max = len(plot[0])-1
    x_bounds = (0, x_max)
    y_max = len(plot)-1
    y_bounds = (0, y_max)

    for j in range(y_max+1):
        previous_j = j-1
        next_j = j+1
        for i in range(x_max+1):
            next_i = i+1
            previous_i = i-1

            if plot[j][i] == 0:
                increment = True
                if not out_of_bounds(x_bounds, next_i):
                    if plot[j][next_i] == 1:
                        increment = False
                if not out_of_bounds(x_bounds, previous_i):
                    if plot[j][previous_i] == 1:
                        increment = False
                if not out_of_bounds(y_bounds, next_j):
                    if plot[next_j][i] == 1:
                        increment = False
                if not out_of_bounds(y_bounds, previous_j):
                    if plot[previous_j][i] == 1:
                        increment = False
                if increment:
                    amount_left += 1
                    plot[j][i] = 1
    return amount_left
                

def out_of_bounds(bounds, value):
    # lower bound = index 0    |    upper bound = index 1
    return (bounds[0] > value or bounds[1] < value)
