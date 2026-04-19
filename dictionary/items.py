store_item ={
    "name" : "Laptop",
    "price":  40000.34
}
store_item["price"]= store_item["price"]*0.9
store_item["stock"] = 10

if "category" in store_item:
    print("Category already exists!")
else:
    store_item["category"] = "Electronics"
    print("category added successfully.")
print(store_item)