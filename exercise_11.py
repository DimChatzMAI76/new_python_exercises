lista=[]
for i in range(10):
    user_input=int(input('dwse ari8mo meta3i 10 kai 20: '))
    while user_input<10 or user_input>20:
        print("parakalw meta3i 10 k 20: ")
        user_input=int(input('dwse ari8mo meta3i 10 kai 20: '))
    lista.append(user_input)


print(lista)
my_tuple=tuple(lista)
print(my_tuple)        

list2=[x**2 for x in lista]
list2.sort()
tuple2=tuple(list2)
print(tuple2)
