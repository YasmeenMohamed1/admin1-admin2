def calc(shapeName, x, y=1):
    if shapeName == "circle":
        return 3.14 * (x ** 2)
    elif shapeName == "triangle":
        return 0.5 * x * y
    elif shapeName == "rectangle":
        return x * y
    elif shapeName == "square":
        return x ** 2

shapeName = input("Enter Shape Name circle, triangle, rectangle, square : ")
x = float(input("Enter value for x "))
if (shapeName == "triangle" or shapeName == "rectangle"):
    y = float(input("Enter value for y (height for triangle, width for rectangle): "))
else:
    y = 1
    
area = calc(shapeName, x, y)


with open("area.txt", "w") as file:
    file.write(f"Shape: {shapeName}, Area: {area}\n")