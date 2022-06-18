bank={"accnt no":3333433,
      "accnt name":"aju"}
print("accnt no" in bank)

print(bank.get("accnt no"))

print("accnt id" in bank)
#
# bank["accnt id"]=123
#
# bank["accnt name"]="deeb"
# print(bank)
if "accnt baln" in bank:
       bank["accnt baln"]="1000"
else:
     bank["accnt baln"]="2000"
print(bank)
