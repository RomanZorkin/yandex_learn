from datetime import datetime
import json

'''
market = json.loads(input())
param_1 = input().split(' ')
param_2 = input().split(' ')
param_3 = input().split(' ')
param_4 = input().split(' ')
param_5 = input().split(' ')
'''



market = json.loads('[{"id": 1, "name": "Asus notebook","price": 1564,"date": "23.09.2021"},{"price": 2500, "id": 3, "date": "05.06.2020", "name": "Keyboardpods" }, {"date": "23.09.2021", "name": "Airpods","id": 5, "price": 2300}, {"name": "EaRPoDs", "id": 2, "date": "01.01.2022", "price": 2200}, { "id": 4, "date": "23.09.2021", "name": "Dell notebook",  "price": 2300}]')
param_1 = 'PRICE_LESS_THAN 2400'.split(' ')
param_2 = 'DATE_AFTER 23.09.2021'.split(' ')
param_3 = 'NAME_CONTAINS pods'.split(' ')
param_4 = 'PRICE_GREATER_THAN 2200'.split(' ')
param_5 = 'DATE_BEFORE 02.01.2022'.split(' ')

requirements = {
    'market': market,
    param_1[0]: param_1[1],
    param_2[0]: param_2[1],
    param_3[0]: param_3[1],
    param_4[0]: param_4[1],
    param_5[0]: param_5[1],
}

requirements['PRICE_LESS_THAN'] = int(requirements['PRICE_LESS_THAN'])
requirements['PRICE_GREATER_THAN'] = int(requirements['PRICE_GREATER_THAN'])
requirements['DATE_AFTER'] = datetime.strptime(requirements['DATE_AFTER'],'%d.%m.%Y').date()
requirements['DATE_BEFORE'] = datetime.strptime(requirements['DATE_BEFORE'],'%d.%m.%Y').date()
requirements['NAME_CONTAINS'] = requirements['NAME_CONTAINS'].lower()


result = []

for article in requirements['market']:
    name_low = article['name'].lower()
    name = article['name']
    price = int(article['price'])
    prod_date = datetime.strptime(article['date'], '%d.%m.%Y').date()
    id_num = int(article['id'])
    
    if requirements['NAME_CONTAINS'] in name_low:        
        if requirements['DATE_AFTER'] <= prod_date <= requirements['DATE_BEFORE']:
            if requirements['PRICE_GREATER_THAN'] <= price <= requirements['PRICE_LESS_THAN']:
                result.append(article)




from operator import itemgetter
newlist = sorted(result, key=itemgetter('id'))

print(json.dumps(newlist))
#print(requirements)
[{"name": "EaRPoDs", "id": 2, "date": "01.01.2022", "price": 2200}, {"date": "23.09.2021", "name": "Airpods", "id": 5, "price": 2300}]