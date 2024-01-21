def max_of_three(p,m,d):
    if p>m and p>d:
        print(p)
    elif m>d:
        print(m)
    else:
        print(d)

print (max_of_three(20,5,0))