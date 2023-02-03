'''
There are a number of cities in a row and there are two bus lines
that go between them. They both visit all cities in order, but one
may take longer than the other to go between any two cities. Starting
on or moving to the Blue line takes a certain amount of extra time.

Determine the min. cost to move from first city to each of the city.
'''

def get_min_cost(red, blue, blueCost):
    '''
    if not is_blue:
        min cost to k = min(min_cost_to_k_minus_1 + red[k], min_cost_to_k_minus_1 + blue[k] + blueCost)
    else:
        min cost to k = min(min_cost_to_k_minus_1 + red[k], min_cost_to_k_minus_1 + blue[k])

    Maintain min_cost and if I am currently on blue or red
    '''

    n = len(red)
    min_cost = [0]
    is_blue = False

    for i in range(0, n):
        if is_blue:
            if red[i] < blue[i]:
                # Switch back to using red
                is_blue = False
                min_cost.append(min_cost[-1] + red[i])
            else:
                min_cost.append(min_cost[-1] + blue[i])

        else:
            if red[i] >= (blue[i] + blueCost):
                # Switch to take blue
                is_blue = True
                min_cost.append(min_cost[-1] + blue[i] + blueCost)
            else:
                min_cost.append(min_cost[-1] + red[i])

    return min_cost


if __name__ == '__main__':

    red = [2, 3, 4]
    blue = [3, 1, 1]
    blueCost = 2
    print(get_min_cost(red, blue, blueCost))

    red = [4, 3, 2]
    blue = [2, 5, 1]
    blueCost = 1
    print(get_min_cost(red, blue, blueCost))
