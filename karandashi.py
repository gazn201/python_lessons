pensil, pen, marker = map(int, input().split())
pensilPrice = 3
penPrice = (pensilPrice+2)
markerPrice = (penPrice+7)
overPrice = ((pensilPrice*pensil)+(penPrice*pen)+(markerPrice*marker))
print(overPrice)
