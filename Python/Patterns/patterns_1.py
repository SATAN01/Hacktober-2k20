def takinginput():
    try:
        global i
        global n
        n = int(input())
        i = 1
    except Exception:
        print('Try entering a numeric value')
        takinginput()   #function will re run if user doesn't enters numeric values
 

takinginput()

while i <= n:
    j = 1
    while j <= i:
        print("*", end=' ')
        j += 1
    print()
    i += 1
