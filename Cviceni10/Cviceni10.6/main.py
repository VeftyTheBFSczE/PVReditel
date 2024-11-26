

pole = [100.10, 323.2, 355.9, 214.19, 87.0]

pole2 = list(map(lambda x: x * 1.3, pole))
pole3 = list(filter(lambda x: x > 120, pole))
pole4 = list(map(lambda x: x * 0.3, filter(lambda x: x > 120, map(lambda x: x - 5, pole))))

print(pole2)
print(pole3)
print(pole4)



