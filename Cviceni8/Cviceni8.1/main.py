# main.py
from samla_box import SAMLA_BOX
from lack import LACK
from sjorapport import SJÖRAPPORT

# Testing the classes
samla_box = SAMLA_BOX(10, 'B', 'SAMLA BOX', 5.99, 45, 30, 40, 50, 200)
lack = LACK(5, 'A', 'LACK', 9.99, 'white', 55, 55, 45)
sjorapport = SJÖRAPPORT(20, 'C', 'SJÖRAPPORT', 3.99, '2024-12-31', 500, 100)

# Manipulating attributes
print(samla_box.volume)
print(lack.color)
print(sjorapport.expiration_date)