#decorator

#def outer_function():
#    message = 'hi'
#
#    def inner_function():
#        print(message)
#    return inner_function()
#
#outer_function()

def generate_power_func(n):
    print("id(n): %X" %id(n))
    def nth_power(x):
        return x**n
    print("id(nth_power): %X" %id(nth_power))
    return nth_power

p = generate_power_func(4)
del generate_power_func
p(3)
