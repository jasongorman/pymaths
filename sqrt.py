def sqrt(number):
    if(number == 0):
        return 0;

    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;

    return g;


def factorial(number):
    if not isinstance(number, int) or number < 0:
        raise Exception("The input must be a positive integer")

    if number == 0:
        return 0

    f = 1

    for i in range(1, number+1):
        f = f * i

    return f

    
print('The Square root of 25 =', sqrt(25));
print('The factorial of 5 is ', factorial(5))