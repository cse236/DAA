#Code without Recursion

first = 0
second = 1
n = 10
print("Fibonacci Sequence :", end = " ")
print(first, second, end = ' ')
for i in range(n-2):
 third = first + second
 print(third, end = ' ')
 first = second
 second = third