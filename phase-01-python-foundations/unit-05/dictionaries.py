product = {"item_id": 1234,
           "name": "Palesa",
           "colour": "Green"
           }

# to access keys in the dictionary

#print(product["item_id"])
#print(product["colour"])

# to add a key and value for our dictionary
#product["size"] = "small"

#print(product)

#to delete a key

#del product["size"]
print(product)

#adding a list to our dictionary

product["size"] = ["Small", "medium", "large"]
print(product["size"][0])
