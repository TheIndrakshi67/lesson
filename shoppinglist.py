filename = "shopping_list.txt"

file = open(filename, "w")
file.write("Milk\n")
file.write("Eggs\n")
file.write("Bread\n")
file.close()

file = open(filename, "r")
print("--- Initial List ---")
print(file.read())
file.close()

file = open(filename, "a")
file.write("Apples\n")
file.write("Butter\n")
file.close()

file = open(filename, "r")
print("--- Updated List (Line by Line) ---")
for line in file:
    print(line.strip())
file.close()
