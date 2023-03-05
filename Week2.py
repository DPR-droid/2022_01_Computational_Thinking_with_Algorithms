n = int(input('Please enter a number: ')) 
a = int(input('1 for product or 2 for sum: '))

product = 1
sum = 0 
if a == 1 : 
    for number in range(1,n+1): 
        product *= number 
    print('Product till n is: ',product) 
elif a == 2: 
    for number in range(1,n+1): 
        sum += number 
    print('Sum till n is: ',sum)        
else:  
    print('Please enter either 1 or 2') 