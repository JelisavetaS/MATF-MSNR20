def for_fib(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

def recur_fib(n):
   if n <= 1:
       return n
   else:
       return(recur_fib(n-1) + recur_fib(n-2))
   
def tail_recur_fib(n, a = 0, b = 1): 
    if n == 0: 
        return a 
    if n == 1: 
        return b 
    return tail_recur_fib(n - 1, b, a + b)

functional_fib = (lambda x, a=1, b=0:
         b if x == 0
         else functional_fib(x - 1, a + b, a))

number = 10

print('Input number is: ' + str(number))
print('For loop Fibonacci ' + str(for_fib(number)))
print('Recursion Fibonacci: ' + str(recur_fib(number)))
print('Tail recursion Fibonacci: ' + str(tail_recur_fib(number)))
print('Functional Fibonacci: ' + str(functional_fib(number)))
