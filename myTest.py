list1 = ('name', 'gender', 'age', 'hobby')
list2 = ('huangyang', 'man', '29', 'tabletennis')
table1 = [list1, list2]
print(table1)

print('1.add a new soldier\n2.change info of a soldier\n3.query info of a soldier')
select = int(input('please select :'))
while True:
    if select == 1:
        input('The name of soldier :')
        input('The gender of soldier:')
        input('The age of soldier:')
        input('The hobby of soldier:')
        print('Add a new soldier success!')
        input('Then you want to:')
    elif select == 2:
        select2=int(input('You want to change what of a soldier:\n1、name\n2、gender\n3、age\n4、hobby\nyour choice:'))
        if select2==1:
            pass
        elif select2==2:
            pass
        elif select2==3:
            pass
        elif select2==4:
            pass

    elif select == 3:
        pass
