fruits_list=["Apple", "Banana","Mango","Strawberry", "Blueberry"]
print("Original list:", fruits_list)

print("Total Fruits: ",len(fruits_list))
print("First Fruit: ",fruits_list[0])
print("Last fruit:",fruits_list[-1])
print("First three: ", fruits_list[:3])

fruits_list.append("Orange")
print("After adding Orange: ", fruits_list)

fruits_list.sort()
print("Sorted alphabetically: ", fruits_list)

fruits_list.reverse()
print("reversed: ", fruits_list)


fruit_info={"name":"mango","type":"Tropical","color":"yellow","stock":50}
print("Fruit profile: ",fruit_info)

print("Type: ", fruit_info["type"])
print("Stock: ", fruit_info.get("stock","not found"))
fruit_info["stock"]=60
fruit_info["price"]=2.50
fruit_info.pop("stock")
print("updated fruit profile: ", fruit_info)

fruit_ids=[1,2,3,4,5]