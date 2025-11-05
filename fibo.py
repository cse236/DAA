#Code with Recursion

def recursive_fibo(n):
 if n in (0,1):
    return n
 return recursive_fibo(n-1) + recursive_fibo(n-2)
n = 10
if n < 0:
 print("Invalid Input")
 exit()
print("Fibonacci Sequence :", end = " ")
for i in range(n):
 print(recursive_fibo(i), end = ' ')