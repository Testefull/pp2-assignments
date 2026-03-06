import re
import json

#1 Extracting prices
price_pattern = re.compile(r'Стоимость\s*\n\s*([\d\s]+,\d+)')

#2 Extracting product names
name_pattern = re.compile(r'\d+\.\s*\n([^\n]+)')

#3 Extracting amount of product
amount_pattern = re.compile(r'\d+,0{3} x')

#4 Extracting date and time information
date_pattern = re.compile(r'\d{2}\.\d{2}\.\d{4}')
time_pattern = re.compile(r'\d{2}:\d{2}:\d{2}')

#5 Payment method
payment_pattern = re.compile(r'[а-яА-яa-zA-z\s]+:\n\s*\d[\d\s]*,\d+')

with open('raw.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    matches_prices = price_pattern.findall(contents)
    prices = [int(v.replace('Стоимость\n', '').replace(',00', '').replace(' ', '')) for v in matches_prices]

    names = name_pattern.findall(contents)

    amount_matches = amount_pattern.findall(contents)
    amounts = [int(v.replace(',000 x', '')) for v in amount_matches]
    total_amount = sum(amounts)

    date_val = date_pattern.findall(contents)[0]
    time_val = time_pattern.findall(contents)[0]
    print(date_val, time_val, sep='\n')

    payment_matches = payment_pattern.findall(contents)
    payment = payment_matches[0].strip().replace(':\n18 009,00', '')
    total = payment_matches[1].replace('ИТОГО:\n', '').replace(',00', '').replace(' ', '').strip()

    items = []
    order = {}

    for name, price in zip(names, prices):
        items.append(
            {
                'name': name,
                'price': price
            }
        )
    
    order['items'] = items
    order['payment method'] = payment
    order['total'] = int(total)


with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(order, f, ensure_ascii=False, indent=2)
    

    
