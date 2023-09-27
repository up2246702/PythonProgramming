#problem 1
def threeOrFive(): 
    sum = 0
    for i in range(1,1000):
        if not i % 5 or not i % 3:
            sum = sum + i
    print(sum)
   
#problem 2
def fibSequence():
    fibonacci = [1, 1]
    while fibonacci[-1] <= 4000000:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    sum = 0
    for x in fibonacci:
        if x % 2 == 0:
            sum += x
    return sum

#problem 3
def primeFactor():
    n = 600851475143
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    print(n)
    
#problem 4
def palindromeProduct():
#6 digits
    list = []
    i = 0 
    for x in range(100, 999):
        for y in range(100, 999):
            stringValue = str(x*y)
    print(stringValue)
    print(len(stringValue))
            splitValue = [int(a) for a in str(stringValue)]
            print(splitValue)
            if splitValue[0] == splitValue[len] and splitValue[1] == splitValue[4] and splitValue[2] == splitValue[3]:
                palMax = splitValue
    print(palMax)