def toplama(x, y):
    return x + y

def cixarma(x, y):
    return x - y

def vurma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölmək olmaz!"
    else:
        return x / y

print("Sadə Kalkulyator")
print("Əməliyyatlar: ")
print("1. Toplama")
print("2. Çixma")
print("3. Vurma")
print("4. Bölmə")

secim = input("Əməliyyat nömrəsini seçin (1/2/3/4): ")

# İstifadəçidən ədədləri daxil etməsi
num1 = int(input("Birinci ədədi daxil edin: "))
num2 = int(input("İkinci ədədi daxil edin: "))

if secim == '1':
    print(f"{num1} + {num2} = {toplama(num1, num2)}")

elif secim == '2':
    print(f"{num1} - {num2} = {cixarma(num1, num2)}")

elif secim == '3':
    print(f"{num1} * {num2} = {vurma(num1, num2)}")

elif secim == '4':
    print(f"{num1} / {num2} = {bolme(num1, num2)}")

else:
    print("Yanlış seçim!")