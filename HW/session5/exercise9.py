def get_even_list(l):
    for i in list(l):
        if i%2 == 0:
            l.remove(i)
    return(l)
print(get_even_list([1, 4, 5, -1, 10]))