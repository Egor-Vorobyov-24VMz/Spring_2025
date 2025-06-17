#Ввод двоичной последовательности
InNum = input("Enter the binary sequence: ")

#Основной алгоритм
OutNum = 0
power = len(InNum) - 1

for Number in InNum:
    OutNum = OutNum + int(Number) * (2 ** power) 
    power = power - 1

print("Decimal value:", OutNum)