wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input('Enter wall width (feet):\n'))
print("Wall area:", str(wall_height * wall_width), "square feet")
paint_needed = float((wall_width * wall_height)/350)
print("Paint needed:", ('{:.2f}'.format(paint_needed)), "gallons")
print("Cans needed:", round(paint_needed), "can(s)\n")

colors = {
  "red": 35,
  "blue": 25,
  "green": 23
}
color = input("Choose a color to paint the wall:\n")
costofpur = round(paint_needed) * colors[color]
print("Cost of purchasing " + str(color) +  " paint: $" + str(costofpur))
