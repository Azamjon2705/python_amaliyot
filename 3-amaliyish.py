### 3-amaliy ish   To‘rt xonali son berilgan.
# Uni chapdan o‘ngga va o‘ngdan chapga o‘qiganda bir xil o‘qilishi aniqlansin

son=int(input("son=")) # son 4 xonali bo'lsin
zapas=son
yigindi=0
while son>0:
    yigindi=yigindi*10+son%10
    son=son//10
print(zapas==yigindi)
