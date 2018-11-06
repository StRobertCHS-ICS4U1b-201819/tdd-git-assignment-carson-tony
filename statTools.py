def mode(list_data):
    if len(list_data) == 0 : return None
    freq = {}
    mx = 0
    for num in list_data:
        if num not in freq:
            freq[num]=0
        freq[num]+=1
        mx = max(mx,freq[num])
    mode = []
    for num,value in freq.items():
        if value==mx:
            mode.append(num)
    if len(mode) == 1 : return mode[0]
    mode.sort()
    return mode

def lower_quartile(list_data):
    if len(list_data) == 0 : return None
    if len(list_data) < 4 : return 0
    list_data.sort()
    if len(list_data) % 2 == 0 :
        list_lowerhalf = list_data[:len(list_data)//2]
        return (list_lowerhalf[len(list_lowerhalf)//2-1] + list_lowerhalf[len(list_lowerhalf)//2])/2
    else :
        list_lowerhalf = list_data[:len(list_data)//2]
        return list_lowerhalf[len(list_lowerhalf)//2]

def upper_quartile(list_data):
    if len(list_data) == 0 : return None
    if len(list_data) < 4 : return 0


def variance(list_data):
    if len(list_data) == 0 : return None
    mean = sum(list_data) / len(list_data)
    total = 0
    for num in list_data:
        total += abs(mean-num) * abs(mean-num)
    return round(total / len(list_data),3)