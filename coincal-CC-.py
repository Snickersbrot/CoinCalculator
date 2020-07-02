Enter = ''

print('CoinCalculator  -by Snickersbrot')
print('note: do not use commas')
print('''
You can calculate:
1 - how much a coin is worth
2 - how much an amout of coins are worth
3 - how much coins would you get for an amount of moneyy''')

print('''
what do you want to calculate? 1, 2, or 3''')
What = input('Enter here: ')
# 1
if What == '1':
    coins = input('''with how much coins do you want to calculate?(example: 0.00435):
''')
    price_of_the_coins = input('''how much are the *coins* worth?:
''')
    One_Bitcoin_end = float(price_of_the_coins) / float(coins)
    print('')
    print(One_Bitcoin)
    print('''
press Enter to exit''')
    if input() == Enter:
        exit()
# 2
if What == '2':
    One_Bitcoin = input('''how much is a coin worth?:
''')
    coins = input('''
with how much coins do you want to calculate?(example: 0.00435):
''')
    # potc = price of the coins 
    potc = float(One_Bitcoin) * float(coins)
    print('')
    print(potc)
    print('''
press Enter to exit''')
    if input() == Enter:
        exit()
# 3
if What == '3':
    price_of_the_coins = input('''how much are the *coins* you want to calculate with worth?:
''')
    One_Bitcoin = input('''how much is a coin worth?:
''')
    coins_end = float(price_of_the_coins) / float(One_Bitcoin)
    print('')
    print(coins_end)
    print('''
press Enter to exit''')
    if input() == Enter:
        exit()
    
    
