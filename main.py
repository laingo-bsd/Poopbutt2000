    import time
    import random
    global money
    global tradeprice
    global day
    global demo
    global miners
    global rad
    day = 1
    demo = day
    miners = 1
    money = 500
    cc = 0
    adminmode = 1
    tradeprice = 10
    rad = [
        "1CVRq6oCQ2BNVe7YKam9o3ZvX2JMwzX1My", "1Mmbf8NQQ7b6ufFtfaGo1BDmJ15jVdLcKp",
        "1LboW7wjgUbQrxugQwp8cAw5PJ1a1m7mZo", "19UUMJo9VTQYShWjR3Xocx4ALk29JomZaA",
        "1KpnPz3ERckprnD6S31mKygdu6aFNifAX4", "1EUKpfQ9Z6pFYiw41NZJ6PL7ambKaJGDNT",
        "1MkbHGB51uCNchjNuP3d7wXLm1Zpp91MRs", "16qLzA3KAEUEbLy8iBWRKdDK5ZYribAoyB",
        "13P94yUn4bhL6ewN3EpuKoeyZKMmHEww9C", "1L2Tuj1iHokmocWTNyG7TNpYmK8q7a3UD",
        "18zZFBu1eVdDEsP46r5oM1ZTZaEGHvdPqp", "1CQT78C45qHj8F7xnf6vg2AcLLyvSj88wb"
    ]
    '''
    cc=clinkcoin


    embed link: https://repl.it/@poopbutt2000/Poopbutt2000?embed=1#main.py

    but thats not for the website

    Each time we doing a mining thing it will run the random money adding program x ammount of times


    '''


    def tradepricernd():
        global tradeprice
        y = random.randint(-6, 10)
        tradeprice = tradeprice + y
        if tradeprice <= 0:
            tradeprice = 0
            tradeprice = tradeprice + random.randint(1, 10)
        time.sleep(3)
        print(str(tradeprice) + " USD to cc is the new trade price")


    def admin():
        global money
        global cc
        print()
        print("Admin menu")
        print("1 = Set Money")
        print("2 = Set Level")
        print("3 = Stuff")
        print("4 = cc")
        cmd = input(": ")
        if cmd == "1":
            money = input("Set money to?: ")
        if cmd == "4":
            cc = input("set cc to?")


    def mining():
        global day
        global cc
        global rad
        global miners
        global mined
        mined = 0
        tempmined = 0
        h = 0

        md = 0
        # day = 1 to 3 minutes
        print("How many days would you like to mine for?")
        cmd = input(": ")
        day = int(day) + int(cmd)
        day = int(day) - 1
        while int(cmd) > 0 and int(cmd) < int(365) - int(day):

            cmd = int(cmd) - 1

            md = md + 1
            mb = random.randint(5, 10)

            print()
            print("DAY " + str(md))
            print()

            while mb > 0:
              
                tmpminers = miners
                while tmpminers > 0 :
                  tempmined > 0
                  tempmined = int(tempmined) 
                  random.randint(1, 4)
                  tmpminers = tmpminers - 1
                cc = cc + mined
                h = h + 1
                print("Net | Share #" + str(h) + " accepted")
                time.sleep(random.randint(1, 2))
                print("You got " + str(mined) + " Clink Coin")
                print("From " + rad[random.randint(0, 9)])
                mb = mb - 1
                #make ten to twenty seconds later.
                time.sleep(random.randint(10, 20))
                print()
                print()
                print()
                #time.sleep(random.randint(40, 90))

    def market():

      global money 

      globals()
      print()
      print("================ Market ================")
      print()
      print("What are you looking for today?")
      print()
      print("1 = Cryto Trading")
      print("2 = Asic Miners")
      #print("3 = Property Market")
      cmd = input(": ")
      if cmd == "1":
          print("1 = Buy")
          print("2 = Sell")
          cmd2 = input(": ")

          #SELLING
          if cmd2 == "2":
              global cc
              print("Today's price for cc is " + str(tradeprice))
              print("cc in account " + str(cc))
              x = input("How much would you like to trade?: ")
              if int(x) <= int(cc):
                  cc = int(cc) - int(x)
                  money = int(x) * tradeprice + money
                  print("you now have " + str(cc) + "cc")
                  print("You now have $" + str(money))

              else:
                  print("You don't have enough cc to do that.")

          #BUYING
          if cmd2 == "1":
              ccwithtax = tradeprice / 100 * 6 + tradeprice
              print("Today's price for cc is " + str(tradeprice))
              x = input("how much would you like to buy?: ")
              totalprice = int(x) * int(ccwithtax)
              print("Your total is " + str(totalprice) + "cc")
              print("Are you sure you would like to continue?")
              print("yes")
              print("no")
              cmd = input(": ")
              if cmd == "yes" and int(money) >= int(totalprice):
                  money = int(money) - int(totalprice)
                  cc = int(cc) + int(x)
              else:
                  print("You don't have enough money in your accout for that")
                  
      if cmd == "2":
          global miners
          print("====== Asic Miner Shop ======")
          print()
          print()
          print("1 = 1 Miner")
          print("Price = $50")
          print()
          print()
          print("2 = 5 Miners")
          print("Price = $225")
          print()
          print()
          print("3 = 10 Miners")
          print("Price = $425")
          print()
          print()
          print("4 = 100 Miners")
          print("Price = $4,500")
          min = input(": ")
          if min == "1":
            print("You're total is $53")
            print("Are you sure you would like to continue?")
            print("yes")
            print("no")
            su = input(": ")
            if su == "yes" and int(money) >= 53:
                print("Your all set!")
                money = int(money) - 53
                miners = int(miners) + 1
            else:
              print("You don't have the money for that!")
          if min == "2":
            print("Your total is $239")
            print("Are you sure you would like to continue?")
            print("yes")
            print("no")
            su = input(": ")
            if su == "yes" and int(money) >= 239:
                print("Your all set!")
                money = int(money) - 239
                miners = int(miners) + 5     
          if min == "3":
            print("Your total is $450")
            print("Are you sure you would like to continue?")
            print("yes")
            print("no")
            su = input(": ")
            if su == "yes" and int(money) >= 450:
                print("Your all set!")
                money = int(money) - 450
                miners = int(miners) + 10
          if min == "4":
            print("Your total is $4,770")
            print("Are you sure you would like to continue?")
            print("yes")
            print("no")
            su = input(": ")
            if su == "yes" and int(money) >= 4770:
                print("Your all set!")
                money = int(money) - 4770
                miners = int(miners) + 100
                print(miners)
    def start():
      
      globals()
      tradepricernd()
      print("====== Main ======")
      print(" You are on day " + str(day))
      print(" You have " + str(cc) + " cc")
      print(" You have $" + str(money))
      print(" You have " + str(miners) + " Miners")
      print()
      #input("Press enter to continue...")
      # if we need we can uncoment this
      print()
      print("1 = Mining")
      print("2 = Market")

      cmd = input(": ")

      if cmd == "1":
          mining()
      if cmd == "2":
          market()
      if cmd == "admin":
          if adminmode == 1:
              admin()

      print()
      print()
      start()


    def startup():
        print(
            " You are a small computer web dev, nobody knows of you.          Your goal?\n\nGet your name recognized.\n\nTo start out you need money so you are going to use what you \nknow best...\n\nComputers! You have 365 days to get enough money before this\ncryptocurrency crashes, good luck."
        )
        print()
        input("press enter to continue...")  #we ether have one here or each day
        print()
        print()
        start()


    startup()
                                                                                                                                                                                                                  