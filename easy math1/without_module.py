def paint_calc(height, width, cover):
    calc1 = (hei*wei)/cover
    calc2 = round(calc1)
    if calc1 > calc2:
        calc2 += 1
    print(f"You'll need {calc2} cans of paint.")

hei = int(input("Height of wall: "))
wei = int(input("Width of wall: "))
coverage = 5
paint_calc(height=hei, width=wei, cover=coverage)

