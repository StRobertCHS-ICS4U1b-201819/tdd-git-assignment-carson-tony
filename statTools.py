import math
def mean(list_data: list) -> float:
    ''' Returns mean of list

        :param list_data: list of values
        :return: float, mean of the list
        '''
    # Empty list handling
    if len(list_data) == 0 : return -1
    # Add all values of list then divide by the length of list
    return sum(list_data) / len(list_data)

def median(list_data: list) -> float:
    ''' Returns median of list

    :param list_data: list of values
    :return: float, median of the list
    '''
    # Empty list handling
    if len(list_data) == 0 : return -1
    # Sort the list
    list_data.sort()
    # Middle value of the list
    divider = len(list_data) // 2
    if len(list_data) % 2 == 0:
        # If the list len is even return the mean of the 2 middle value
        return (list_data[divider - 1] + list_data[divider]) / 2
    else:
        # Return the middle value of the list
        return list_data[divider]

def mode(list_data: list) -> list:
    ''' Returns mode of list

    :param list_data: list of values
    :return: list, list of most frequent values
    '''
    # list to return
    mode = []
    # map of frequency of each value
    freq = {}
    # max occurrences of a value
    mx = 0
    # empty list handling
    if len(list_data) == 0 : return mode
    for num in list_data:
        # hash num if not put in freq map
        if num not in freq:
            freq[num] = 0
        # increase value frequency
        freq[num] += 1
        # update max occurrences
        mx = max(mx, freq[num])
    # add values to return list if they have same occurrence as max occurrences
    for num, value in freq.items():
        if value == mx:
            mode.append(num)
    mode.sort()
    return mode

def range(list_data: list) -> float:
    ''' Returns range of list

    :param list_data: list of values
    :return: float, range of the list
    '''
    # empty list handling
    if len(list_data) == 0 : return -1
    # sort the list
    list_data.sort()
    # take the last (greatest value) and subtracts the first (smallest value)
    return list_data[len(list_data) - 1] - list_data[0]

def lower_quartile(list_data: list) -> int:
    ''' Returns lower quartile of a list
        Lower quartile : median of lower half of list

    :param list_data: list of values
    :return: int, lower quartile of list
    '''
    # Handling list that is less than 4 values, no lower quartile, returns -1
    if len(list_data) < 4 : return -1
    list_data.sort()
    # Create list consisting of lower half of list_data
    list_lowerhalf = list_data[:len(list_data)//2]
    # Even value count in list_data, even value count in lower half of list
    # Find median for even/odd list
    if len(list_data) % 2 == 0 :
        return (list_lowerhalf[len(list_lowerhalf)//2 - 1] + list_lowerhalf[len(list_lowerhalf)//2]) / 2
    else :
        return list_lowerhalf[len(list_lowerhalf)//2]

def upper_quartile(list_data: list) -> int:
    ''' Return upper quartile of a list
        Upper quartile : median of upper half of list

    :param list_data: list of values
    :return: int, upper quartile of list
    '''
    # Handling list that is less than 4 values, no upper quartile, returns -1
    if len(list_data) < 4 : return -1
    list_data.sort()
    # Create list consisting of upper half of list_data
    list_upperhalf = list_data[len(list_data)//2:]
    # Even value count in list_data, even value count in upper half of list
    # Find median for even/odd list
    if len(list_data) % 2 == 0 :
        return (list_upperhalf[len(list_upperhalf)//2 - 1] + list_upperhalf[len(list_upperhalf)//2]) / 2
    else :
        return list_upperhalf[len(list_upperhalf)//2]

def variance(list_data: list) -> float:
    ''' Return variance of a list
        Variance : Spread of numbers from the average value in the list
    :param list_data: list of values
    :return: float, variance of the list rounded to 3 decimals
    '''
    if len(list_data) == 0 : return 0
    # Find mean of list
    mean = sum(list_data) / len(list_data)
    total = 0
    # Find difference of each number in list to the mean
    for num in list_data:
        # Add difference squared to total
        total += abs(mean-num) * abs(mean-num)
    # Divide total by list length and round to 3 decimals
    return round(total / len(list_data),3)

def standard_Deviation(list_data: list) -> float:
    ''' Returns standard deviation of list
        Standard Deviation: the square root of the spread of numbers from the average value in the list
    :param list_data: list of values
    :return: float, standard deviation of the list rounded to 3 decimals
    '''
    if len(list_data) == 0: return -1
    # Find mean of list
    mean = sum(list_data) / len(list_data)
    total = 0
    # find difference of each number in the list to the mean
    for num in list_data:
        # Add difference squared to total
        total += abs(mean - num) * abs(mean - num)
    # Square root of total that was divided by list length and rounded to 3 decimals
    return round(math.sqrt(total / len(list_data)), 3)