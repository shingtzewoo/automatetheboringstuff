import pyinputplus as pyip

prices = {
    'wheat': 3,
    'white': 3,
    'sourdough': 4,
    'chicken': 3,
    'turkey': 4,
    'ham': 4,
    'tofu': 3,
    'cheese': 2
}

priceTally = 0
totalPrice = 0

breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Bread Type: ", allowRegexes=['^wheat$|^white$|^sourdough$'])
priceTally += prices.get(breadType, 0)

proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Protein Type: ", allowRegexes=['^chicken$|^turkey$|^tofu$|^ham$'])
priceTally += prices.get(proteinType, 0)

cheese = pyip.inputYesNo(prompt='Do you want cheese?')

if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozarella'], prompt="Cheese Type: ", allowRegexes=['^swiss$|^cheddar$|^mozarella$'])
    priceTally += prices.get('cheese', 0)

condimentType = pyip.inputChoice(['mayo', 'mustard'], prompt="Choose either mayo or mustard: ", allowRegexes=['^mayo$|^mustard$'])

sandwichNumber = pyip.inputInt(prompt='Number of sandwiches: ', min=1)
totalPrice = sandwichNumber * priceTally

print(f'Your total price is ${totalPrice}')
