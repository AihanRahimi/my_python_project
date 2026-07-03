#list of products
products={'milk':{'price':'2$','exp':'01/20'},
          'chips':{'price':'1$','exp':'01/30'},
          'salad':{'price':'5$','exp':'01/12'},
          'panir':{'price':'4$','exp':'01/18'},
          'water':{'price':'0.5$', 'exp':'12/30'}}

#input name of products
name = input('PRODUCT:')

#input price or exp
price_exp = input('price(p),exp(exp)')

r= {'price':'price','exp':'exp'}
if price_exp == 'p':key = 'price' 
if price_exp == 'exp':key = 'exp'
if name in products :print(('%s %s is %s ')%(name,r[key],products[name][key]))