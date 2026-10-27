temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is cloudy outside")
else:
  print("It is sunny outside")

#def calculate_sum(a, b):
 #   print(a + b)

#my_sum = calculate_sum(3, 1) # 4
#print(my_sum)

def outer_func():
    msg = "Hello there!"
    print(msg)

    def inner_func():
        res = "How are you?"
        print(res)

    inner_func()

outer_func()