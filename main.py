import func

pwr:int


while True:
    try:
        pwr = int(input("Enter the power of the polynom: "))
    except:
        print("-- Invalid entry.")  
    else:
        if pwr > 0:
            break
        else:
            print("-- Enter a positive number.")

func.Clr()
coef:list[int]
plus:list[int]
res:list[int]
coef = list(0 for i in range(pwr+1))
plus = list(0 for i in range(pwr+1))
res = list(0 for i in range(pwr+1))


for i in range(pwr+1):
    for j in range(pwr):
        print(f"{coef[pwr - j]}x^{pwr - j} + ", end="")
    print(f"{coef[0]}x^0")
    while True:
        try:
            coef[pwr - i] = int(input(f"Coeficient for x^{pwr - i}: "))
        except:
            print("-- Invalid entry.")
        else:
            break
    func.Clr()

for j in range(pwr):
        print(f"{coef[pwr - j]}x^{pwr - j} + ", end="")
print(f"{coef[0]}x^0")