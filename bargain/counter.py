a = 30000
b = 0
for i in range(1, 241 * 2):
    b = a + (a*0.03)
    a = b

print(b)