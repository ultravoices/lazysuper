dudes_list = []

def make_list_of_dudes(n):
    for i in range(1, n+1):
        dudes_list.append(i)
    return dudes_list

def deadly_circle_of_dudes(a_list):
    number_of_dudes = len(a_list)
    while len(a_list) != 1:
        a_list.pop(1)
        a_list += [a_list.pop(0)]
    return number_of_dudes, a_list
