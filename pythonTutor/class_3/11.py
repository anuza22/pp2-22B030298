#«Сумма цифр»
a = int(input())
sum = a%10 + a//10%10 + a//100
print(sum)
