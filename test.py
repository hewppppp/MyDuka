from database import get_products

products = get_products()
print(products)

# (3, 'bread', Decimal('60.00'), Decimal('65.00'))

#for i in products:
#print(i[1])