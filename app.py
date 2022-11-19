#/
#    author:   abhijayrajvansh
#    created:  29.01.2022 01:55:46
#/
import colorama
from colorama import Fore
import time

colorama.init(autoreset = True)

def calc ():

    crypto_name = input("Enter The Cryptocurrency Name              : ")

    initial_coin_price = input("Enter The *Current* Value of Coin          : ")
    initial_coin_price = float(initial_coin_price)
    initial_buying_amt = input("Enter The *Initial* Buying Amount          : ")
    initial_buying_amt = float(initial_buying_amt)
    initial_buying_amt = initial_buying_amt + ((initial_buying_amt * 0.5) / 100)
    choice = input("\n - '1' For Percentage Calculation\n - '2' For Biding Calculation\n\nChoice                                     : ")
    choice = int(choice)

    if choice == 1:
        percent_increase = input("Enter The Percent Elevation (ex: 1.5 or 2) : ")
        percent_increase = float(percent_increase)
        BID_coin_price = round(initial_coin_price + ((initial_coin_price * percent_increase) / 100), 4)
    else:
        safe_BID_Value = input("Enter Safe High BID Coin Value             : ")
        safe_BID_Value = float(safe_BID_Value)
        percent_increase = round(((100 * (safe_BID_Value - initial_coin_price)) / initial_coin_price), 4)
        BID_coin_price = float(safe_BID_Value)

    final_amt = round(initial_buying_amt + ((initial_buying_amt * percent_increase) / 100), 4)
    sellingPrice_brokerage = round(final_amt - ((final_amt * 0.5) / 100), 4)
    total_profit = round((sellingPrice_brokerage - initial_buying_amt), 4)

    print("\nPercent Gain In Coin Price : " + f"{Fore.RED}" + str(initial_coin_price) + " -> " + f"{Fore.GREEN}" + str(BID_coin_price) + f"{Fore.GREEN}" + " ⬆ " + str(percent_increase) + "%")
    print("~~~~~~~~~~~~~~~~~~~~~~( " + crypto_name + " )~~~~~~~~~~~~~~~~~~~~~~")
    print("| Final Coin Value                         : " + str(BID_coin_price))
    print("| Final Selling Amount                     : " + str(final_amt))
    if total_profit > 0 :
        print(f"| Profit Gain                              : {Fore.GREEN}+" + str(total_profit))
    else:
        print(f"| Profit Gain                              : {Fore.RED}" + str(total_profit))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

while True:
    calc()
    time.sleep(1)