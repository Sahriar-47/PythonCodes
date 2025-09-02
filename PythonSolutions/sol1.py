pairs = [(293, 57), (302, 59)]

for a, b in pairs:
    mod_value = a % b
    print(f"{a} % {b} = {mod_value}")
    print(mod_value == 0)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(fibonacci(i), end=" ")
