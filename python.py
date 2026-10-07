##n = int(input())
##x0 = 0
#x1 = 1
#i = 0
#print(x0)
#print(x1)
#while i<=n:
   # x2 = x1 + x0
   # x0 = x1
   # x1 = x2
   ### i = i +1

    

n = int(input())
stop = 1
flag = True
last_even = 2
if n ==1 :
    print(n)
while stop != n:
    for number in range (last_even + 1 , 200000000):
        flag = True
        if number % 2 != 0:
            for divider in range(3, int(number**0.5)+1):
                if number % divider == 0:
                    flag = False
                    break
            if flag == True:
                print(number)
                last_even = number
                stop+=1
                break
        else:
            flag = False

            

            
             

     