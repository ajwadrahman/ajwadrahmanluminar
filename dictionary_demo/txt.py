txxt="txt hi hello txt"
word=txxt.split(" ")
wor_txtt={}
for co in word:
    if co in wor_txtt:
        wor_txtt[co]+=1
    else:
        wor_txtt[co]=1
print(wor_txtt)