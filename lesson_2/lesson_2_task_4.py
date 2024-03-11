def fizz_buzz (n):
    for m in range (1, n):
        if m % 3 == 0 and m % 5 == 0:
            print("FizzBuzz")
        else: 
            if m % 3 == 0 and m % 5 != 0:
                print("Fizz")
            else:
                if m % 5 == 0 and m % 3 != 0:
                    print("Buzz")
                else:
                    print(m)
        

x = fizz_buzz (100)
print (x)