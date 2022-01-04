import math
def paint_calc(height, width, cover):
    area = hei*wei
    calc = math.ceil(area/cover)
    print(f"You'll need {calc} cans of paint.")

hei = int(input("Height of wall: "))
wei = int(input("Width of wall: "))
coverage = 5
paint_calc(height=hei, width=wei, cover=coverage)

