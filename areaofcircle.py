def area_of_circle(r):
    pi=3.147
    area= pi*r*r
    return area

radius=float(input("The Radius of the circle: "))
print("The Area of the circle",radius,"is:",area_of_circle(radius))
