def modify_list(l):
    ll = []
    for i in l:
        if i % 2 != 0:
            ll.append(i)
    return ll
l={3,13,15,27,1,4,8,23,19,12,9,2,17}
lm=list(l)
lm.sort(reverse = True)
a = modify_list(l)
print(set(a))