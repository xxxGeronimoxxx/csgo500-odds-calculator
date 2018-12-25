while True:
    loss = 0
    count = 0
    totalposs = 54
    winposs = 26
    lossposs = 28
    bet = int(input("your bet: "))
    maxi = int(input("Your credit: "))
    while True:
        loss += bet
        bet = bet*2
        count += 1
        if loss >= maxi:
            count -= 1
            odd = lossposs / totalposs
            print("max num of rounds you can loose: ", count)
            print("your odds of busting: ", odd**count * 100)
            break
        
    
    
    
                
