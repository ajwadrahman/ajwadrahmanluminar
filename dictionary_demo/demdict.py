mob={"brand":"samsung","color":"matt black","model":"s21 ultra","price":"100000"}
print(mob["brand"])
print(mob["model"])
print(mob["color"])
print(mob["price"])

print("price" in mob)

mob["glass"]="victus"
print(mob)

# add
print("display" in mob)
mob["display"]="super amoled"
print(mob)

# update
mob["color"]="burgundy"
print(mob)

if mob["price"] >10000:
    mob["price"]-=50000
else:
    mob["price"]-=1000
print(mob)