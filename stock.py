import time,datetime

x = 0
y = 0
z = 0
sharessold = 0
sharesbought = 0
shares = 1000000
cash = 0
bp = 0.04
sp = bp/(6/5)
for i in range(100):
    print('total shares left are '+str(shares))

    print('total cash available is '+str(cash))

    print('total shares bought is '+str(sharesbought))

    print('total shares sold is '+str(sharessold))

    print('buy price is '+str(bp))

    print('sell price is '+str(sp))

    x = str(input('buy or sell ?'))
    if x == 'b':
        print('how many shares to buy ?')
        x=int(input(''))
        cash=cash+x*bp
        shares=shares-x
        sharesbought=sharesbought+x
        if sharesbought>sharessold:
            bp=bp+((bp/2)*0.05)*x*0.000005
            sp=bp/(6/5)
    elif x == 's':
        print('how namy shares to sell ?')
        x=int(input(''))
        cash=cash-x*sp
        shares=shares+x
        sharessold=sharessold+x
        if sharesbought>=sharessold:
            sp=sp-((sp/2)*0.05)*x*0.000005
            bp=sp*(6/5)
    else:
        print('only b for buy or s for sell are valid')
