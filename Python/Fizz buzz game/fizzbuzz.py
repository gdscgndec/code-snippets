def fizzbuzz(r):
    for i in range(1,r):
        if (i%3==0 and i%5==0): 
            print(str(i)+' = Fizz buzz')
        elif i%3==0:
            print(str(i)+' = Fizz')
        elif i%5==0:
            print(str(i)+' = Buzz')
        else:
            print(str(i))
fizzbuzz(65)