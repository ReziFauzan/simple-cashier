appleStock = 7
orangeStock = 7
grapeStock = 6

print('=== WELCOME TO FRUIT STORE ===')
print('WE HAVE: ')
print(f'Apple avaible : {appleStock}')
print(f'Orange avaible: {orangeStock}')
print(f'Grape avaible : {grapeStock}')
print(' ')
apple = int(input('how many apple you want : '))
while apple > appleStock:
    print('we dont have that many apple')
    print(f'apple avaible : {appleStock}')
    apple = int(input('how many apple you want : '))

orange = int(input('how many orange you want : '))
while orange > orangeStock:
    print('we dont have that many orange')
    print(f'orange avaible : {orangeStock}')
    orange = int(input('how many orange you want : '))

grape = int(input('how many grape you want : '))
while grape > grapeStock:
    print('we dont have that many grape')
    print(f'grape avaible : {grapeStock}')
    grape = int(input('how many grape you want : '))

applePrice = 10
orangePrice = 15
grapePrice = 20

appleBought = apple*applePrice
orangeBought = orange*orangePrice
grapeBought = grape*grapePrice

total = appleBought + orangeBought + grapeBought

print(' ')
print('price detail')
print(' ')
print(f'Apple: {apple} x ${applePrice} = ${appleBought}')
print(f'Orange: {orange} x ${orangePrice} = ${orangeBought}')
print(f'Grape: {grape} x ${grapePrice} = ${grapeBought}')
print(' ')
print(f'Total: ${total}')
print(' ')

pay = int(input('insert your money : $'))
while total > pay:
    less = total - pay
    print(f'not enough money : {less}')
    pay = int(input('insert your money : $'))
if total == pay:
    print('Thank you!')
else:
    print('Thank you!')
    print('')
    return_ = pay - total 
    print(f'your return : ${return_}')
