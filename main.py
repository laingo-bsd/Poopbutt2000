import time
import random
global money
global tradeprice 
global day
day = 0
miners = 1
money = 0
cc = 0
adminmode = 1
tradeprice = 20
rad = ["1CVRq6oCQ2BNVe7YKam9o3ZvX2JMwzX1My", "1Mmbf8NQQ7b6ufFtfaGo1BDmJ15jVdLcKp", "1LboW7wjgUbQrxugQwp8cAw5PJ1a1m7mZo", "19UUMJo9VTQYShWjR3Xocx4ALk29JomZaA", "1KpnPz3ERckprnD6S31mKygdu6aFNifAX4", "1EUKpfQ9Z6pFYiw41NZJ6PL7ambKaJGDNT", "1MkbHGB51uCNchjNuP3d7wXLm1Zpp91MRs", "16qLzA3KAEUEbLy8iBWRKdDK5ZYribAoyB", "13P94yUn4bhL6ewN3EpuKoeyZKMmHEww9C", "1L2Tuj1iHokmocWTNyG7TNpYmK8q7a3UD", "18zZFBu1eVdDEsP46r5oM1ZTZaEGHvdPqp", "1CQT78C45qHj8F7xnf6vg2AcLLyvSj88wb"]

'''
cc=clinkcoin




'''

def tradepricernd():
  global tradeprice
  y = random.randint(-16, 20)
  tradeprice = tradeprice + y
  if tradeprice <= 0:
    tradeprice = 0
    tradeprice = tradeprice + random.randint(1, 10)
  time.sleep(3)
  print(str(tradeprice) + "cc to Usd is the new trade price")
  


def admin():
  global money
  print()
  print("Admin menu")
  print("1 = Set Money")
  print("2 = Set Level")
  print("3 = Stuff")
  cmd = input(": ")
  if cmd == "1":
    money = input("Set money to?: ")


def mining():
  global day
  global cc
  h = 0
  
  md = 0
  # day = 1 to 3 minutes
  print("How many days would you like to mine for?")
  cmd = input(": ")
  day = int(day) + int(cmd)
  day = int(day) - 1
  while int(cmd) > 0:

    cmd = int(cmd) - 1
   
    md = md + 1
    mb = random.randint(5, 10)
    
    print()
    print("DAY " + str(md))
    print()

    while mb > 0:
      
      mined = random.randint(1, 4)
      cc = cc + mined
      h = h + 1
      print("Net | Share #" + str(h) + " accepted")
      time.sleep(random.randint(1, 2))
      print("You got " + str(mined) + " Clink Coin")
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
  #print("2 = Asic Miners")
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
      if str(x) <= str(cc):
        cc = cc - int(x)
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
      if cmd == "yes" and money >= totalprice:
        money = int(money) - int(totalprice)
        cc = int(cc) + int(x)
      else:
        print("You don't have enough money in your accout for that")

  if cmd == "2":
    print("====== Asic Miner Shop ======")
    print()
    print()
    print("miner 1")
    print("price = 5,000")
    print()
    print("=============")
    print()
    print("miner 2")
    print("$4,000")
    print()
    print("=============")
    print()
    print("miner 3")
    print("price = $3,000")


def start():
  globals()
  global day
  day = int(day) + 1
  if day == 30:
    print("Get premium to continue and get updates")
    quit()

  tradepricernd()
  print("====== Main ======")
  print(" You are on day " + str(day))
  print(" You have " + str(cc) + " cc")
  print(" You have $" + str(money))
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
  print(" You are a small computer web dev, nobody knows of you.          Your goal?\n\nGet your name recognized.\n\nTo start out you need money so you are going to use what you \nknow best...\n\nComputers! You have 365 days to get enough money before this\ncryptocurrency crashes good luck.")
  print()
  input("press enter to continue..." ) #we ether have one here or each day
  print()
  print()
  start()
  
  






startup()

