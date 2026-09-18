pasta=("Pasta Arrabiata", "Italian",20,"Medium")
biryani=("Chicken Birayani", "Indian", 45,"Hard")

all_recipes=(pasta,biryani)

print("Recipe 1: ",pasta)
print("Name: ",pasta[0])
print("Cuisine: ", pasta[1])
print("Difficulty: ", pasta[-1])

print("n\First recipe name: ", all_recipes[0][0])
print("Second recipe time: ", all_recipes[1][2],"mins")
print("Pasta details(sliced): ", pasta[1:3])

print("n\Pasta Recipe details: ")
for detail in pasta:
    print("-",detail)

pasta_ingredients={"tomato", "garlic", "olive oil", "chili", "pasta"}
biryani_ingredients={"rice", "chicken", "garlic","onion", "tomato"}

print ("n\Pasta ingredients: ", pasta_ingredients)
print("Biryani ingredients: ", biryani_ingredients)
print("Total pasta ingredients: ", len(pasta_ingredients))

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("Updated pasta ingredients: ", pasta_ingredients)

all_ingredients=pasta_ingredients.union(biryani_ingredients)
common=pasta_ingredients.intersection(biryani_ingredients)
only_pasta=pasta_ingredients.difference(biryani_ingredients)
unique_to_each=pasta_ingredients.symmetric_difference(biryani_ingredients)

print("n\All ingredients (union): ", all_ingredients)
print("Common Ingredients (intersection): ", common)
print("Only in Pasta (difference): ", only_pasta)
print("Not Shared (symm diff): ", unique_to_each)