def count_even_numbers(num1, num2):
    count = 0
    if num1 == num2:
        return count
    else:
        for i in range(num1, (num2 + 1)):
            if i % 2 == 0:
                count += 1
                return count

def build_person_to_free_timeslots(avail_list):
    lst = {}
    unique_lst = list(set(avail_list))
    for name in unique_lst:
        if name[0] in lst:
            lst[name[0]].append(name[1])
        else:
            lst[name[0]] = [name[1]]
    return lst

def invert_dictionary(x):
    lst = {}
    unique_lst = list(set(x))
    for time in unique_lst:
        if time[1] in lst:
            lst[time[1]].append(time[0])
        else:
            lst[time[1]] = [time[0]]
    return lst
            
def func(a,b,c):
    print(a,b,c)
    
def many_def(a,b=6,c='toronto'):
    print(a,b,c)
    
def app(item, L = []):
    L.append(item)
    return L

def add(i,j):
    return i + j