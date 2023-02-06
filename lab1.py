import timeit
import matplotlib.pyplot as plt


#RECURSIVE METHOD
inputs1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
results1 = [0, 0, 0, 0, 0.0002, 0.0005, 0.0019, 0.005, 0.021, 0.054, 0.242, 0.611,
            2.56, 6.63, 28.77, 74.76, 412.22]


code_to_test = '''
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
fib(1)'''
#elapsed_time = timeit.timeit(code_to_test, number=1)
#print(format(elapsed_time, '.5f'))

'''xpoints = inputs1
ypoints = results1

plt.title("Recursive method")
plt.xlabel('n-th Fibonacci number')
plt.ylabel('Time(s)')
plt.plot(xpoints, ypoints, 'bo-')
plt.show()'''

#DYNAMIC PROGRAMMING
inputs2 = [479, 721, 866, 1000, 1313, 1555, 1999, 2611, 3333, 3888, 5000, 7543, 8700, 10000, 12801, 15999]
results2 = [0.00008, 0.00010, 0.00014, 0.00018, 0.00021, 0.00026, 0.00033, 0.00046, 0.00065, 0.0008, 0.00118,
            0.00275, 0.00448, 0.00539, 0.00891, 0.01245]

code_to_test = '''
def fib(n):
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]
fib(1)'''
#elapsed_time = timeit.timeit(code_to_test, number=1)
#print(format(elapsed_time, '.5f'))

xpoints2 = inputs2
ypoints2 = results2
plt.title("Dynamic programming method")
plt.xlabel('n-th Fibonacci number')
plt.ylabel('Time(s)')
#plt.plot(xpoints2, ypoints2, 'bo-')
plt.show()

#Binet Formula Method
inputs3 = [479, 721, 866, 1000, 1313, 1555, 1999, 2611, 3333, 3888, 5000, 7543, 8700, 10000, 12801, 15999]
results3 = [0.000004, 0.000004, 0.000004, 0.000005, 0.000005, 0.000005, 0.000005, 0.000006, 0.000006,
            0.000006, 0.000007, 0.000007, 0.000007, 0.00069, 0.000007, 0.001]

code_to_test = '''
def fib(n):
	phi1 = (1 - 5 ** 0.5) / 2
	phi2 = (1 + 5 ** 0.5) / 2
	return (phi2**(n-1) - phi1**(n-1)) // (5**0.5)
fib(1313)'''
#elapsed_time = timeit.timeit(code_to_test, number=1)
#print(format(elapsed_time, '9f'))

xpoints3 = inputs3
ypoints3 = results3
plt.title("Binet formula method")
plt.xlabel('n-th Fibonacci number')
plt.ylabel('Time(s)')
#plt.plot(xpoints3, ypoints3, 'bo-')
plt.show()

#MATRIX POWER METHOD
inputs4 = [479, 721, 866, 1000, 1313, 1555, 1999, 2611, 3333, 3888, 5000, 7543, 8700, 10000, 12801, 15999]
results4 = [0.000469, 0.000703, 0.000839, 0.001, 0.001335, 0.001577, 0.002077, 0.002939, 0.004100, 0.004921,
            0.006843, 0.013791, 0.017616, 0.021414, 0.031691, 0.044863]
def fib(n):
    F = [[1,1], [1, 0]]
    if (n==0):
        return 0
    power(F, n-1)
    return F[0][0]

def power(F, n):
    M = [[1, 1], [1, 0]]

    for i in range(2, n+1):
        mult(F, M)

def mult(F, M):
    x = (F[0][0]*M[0][0] + F[0][1]*M[1][0])
    y = (F[0][0]*M[0][1] + F[0][1]*M[1][1])
    z = (F[1][0]*M[0][0] + F[1][1]*M[1][0])
    n = (F[1][0]*M[0][1] + F[1][1]*M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = n


code_to_test = '''
def fib(n):
    F = [[1,1], [1, 0]]
    if (n==0):
        return 0
    power(F, n-1)
    return F[0][0]

def power(F, n):
    M = [[1, 1], [1, 0]]

    for i in range(2, n+1):
        mult(F, M)

def mult(F, M):
    x = (F[0][0]*M[0][0] + F[0][1]*M[1][0])
    y = (F[0][0]*M[0][1] + F[0][1]*M[1][1])
    z = (F[1][0]*M[0][0] + F[1][1]*M[1][0])
    n = (F[1][0]*M[0][1] + F[1][1]*M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = n
fib(1995)'''
#elapsed_time = timeit.timeit(code_to_test, number=1)
#print(format(elapsed_time, '4f'))

xpoints4 = inputs4
ypoints4 = results4
plt.title("All three methods")
plt.xlabel('n-th Fibonacci number')
plt.ylabel('Time(s)')
plt.plot(xpoints2, ypoints2, 'bo-', xpoints3, ypoints3, 'r*:', xpoints4, ypoints4, 'y+:')
plt.show()