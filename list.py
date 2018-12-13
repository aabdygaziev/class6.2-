a = []
while True:
    b = input()
    if b =='q':
        break
    elif b =='add':
        s1 = input()
        a.append(s1)
    elif b =='get':
        print(a)
    elif b =='remove':
        s2 = input()
        if s2 in a:
            a.remove(s2)
    print(a)




