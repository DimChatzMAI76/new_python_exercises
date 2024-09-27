N=int(input('dwse ton ari8mo: '))
while N<3 or N>20:
    print('dwse ari8mo meta3i 3 kai 20')
    N=int(input('dwse ton ari8mo: '))
numbers=[]
for cnt in range(0,N):
    numbers.append(int(input('give the: '+str(cnt+1)+' th number: ')))

numbers.sort()
print(numbers)    
