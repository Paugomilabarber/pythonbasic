# Número de línies del patró
n = 3

# Primera part del patró (creixent)
for i in range(1, n + 1):
    print('*' * i)

# Segona part del patró (decreixent)
for i in range(n - 1, 0, -1):
    print('*' * i)
