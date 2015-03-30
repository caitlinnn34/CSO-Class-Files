def vendingMachine(money, choice):
    drinks= ['pepsi', 'coke','fuze']
    if money < 1.75:
        print "need more money"
    elif money >= 1.75:
        if choice.lower() in drinks:
            return (choice.lower(), 'your change is ' + str(money -1.75))
        else:
            return (money, "choice unavailable")
            

                
