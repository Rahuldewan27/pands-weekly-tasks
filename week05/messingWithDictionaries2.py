# messingWithDictionaries2
# author : rahul parvesh dewan

car = {
    "make"  : "Toyota",
    "model" : "Corolla",
    "year"  : 2015,
    "tags"  : ["Preowned", "Best Buy", "Dealer"]
}

#print(car)

#for key in car:
#    print(key, "has value", car[key])

for key, value in car.items():
    print(key, "has value", value)