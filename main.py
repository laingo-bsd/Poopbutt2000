import time
import random
global money
global tradeprice 
global dayleft
miners = 1
money = 500
cc = 0
dayleft = 365
adminmode = 1
tradeprice = 20

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
  global dayleft
  print("How many days would you like to mine for?")
  cmd = input(": ")
  dayleft = int(dayleft) - int(cmd)



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
  print("3 = Property Market")
  cmd = input(": ")
  if cmd == "1":
    print("1 = Buy")
    print("2 = Sell") 
    cmd = input(": ")
    #gay
    #SELLING
    if cmd == "2":
      global cc
      print("Today's price for cc is " + str(tradeprice))
      print("cc in account " + str(cc))
      x = input("How much would you like to trade?: ") 
      if str(x) <= str(cc):
        cc = cc - int(x)
        money = int(x) * tradeprice + money
        print("you now have " + str(cc) + "cc")
        print("You now have $" + str(money))

    #BUYING
    if cmd == "1":
      ccwithtax = tradeprice / 100 * 6 + tradeprice
      print("Today's price for cc is " + str(tradeprice))
      x = input("how much would you like to buy?: ")
      totalprice = int(x) * int(ccwithtax)
      print("Your total is " + str(totalprice) + "cc")
      print("Are you sure you would like to continue?")
      print("yes")
      print("no")
      cmd = input(": ")
      if cmd == "yes":
        money = int(money) - int(totalprice)
        cc = int(cc) + int(x)
      
  if cmd == "2":
    print("====== Asic Miner Shop ======")
    print()
    print("1 = 100 - 1000")
    print()
        

def start():
  globals()
  global dayleft
  dayleft = dayleft - 1
  dayon = 365-dayleft
  print(dayon)
  tradepricernd()
  
  print("====== Main ======")
  print(" You are on day " + str(dayon))
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
  print(" You are a low class hacker, nobody knows of you. Your goal?\n\nGet your name recognized.\n\nTo start out you need money so you are going to use what you \nknow best...\n\nComputers! You have 365 days to get enough money before this\ncryptocurrency crashes good luck.")
  print()
  input("press enter to continue..." ) #we ether have one here or each day
  print()
  print()
  start()
  
  






startup()
