h = int(input("Enter the value for N: "))
pie = float(input("Enter value for pie: "))
r = 3
for h in range(10, h+1, 2):
    volume = pie * r * r * h
    print('The Volume is', volume)
