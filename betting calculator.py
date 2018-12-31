import math
#x = Startbetrag
#n = Anzahl mögliche Fehlschläge bis zum Bankrott
#a = Gesamtanzahl Geld

while True:
    a = int(input("Enter your Balance here: "))
    x = a/10
    x += 1
    n = math.log2(x)
    n =  math.modf(n)
    n = n[1]
    n = int(n)
   
    while True:
        X = a / (2**n)
        X =  math.modf(X)
        X = X[1]
        X = int(X)
        chance = 28 / 54
        chance = chance**n
        chance *= 100
        print("For max efficency bet", X)
        print("You can loose up to", n, "rounds.")
        print("The chance of this happening is", chance,"%")
        break
        
