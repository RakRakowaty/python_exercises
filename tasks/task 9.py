def is_member(x, d):
    if x in d:
        print(True)
    else:
        print(False)
        
def is_member2(x,d):
    status =0
    for i in d:
        if x==i:
            print(True)
            status =1
    if status ==0:
        print(False)

is_member('a',['d',1,2,3,'b'])
is_member2('d',['d',1,2,3,'x'])
    