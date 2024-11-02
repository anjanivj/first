h={"name":"malu","place":"aluva","pin":683520}
print(h)
print(type(h))
print(len(h))#length ariyan
print(h["pin"])
print(h.get("place"))#get aluva
print(h.keys())#keys means :malu,aluva,etc
print(h.items())#variables ellam varum
print(h.values())#values means :malu,aluva,etc
print("name" not in h)
print("pin" in h)
h["place"]="paravoor"
print(h)
h.update({"pin": 8778})
print(h)
h["class"]=12#add cheyanum change cheyanum  same to 12th line
print(h)
h.update({"department":"commerce"})
print(h)
for i in h:
    print(i)#loop ethill ouput ayi kittane variables ayi koduthekunna iteams an (name,place,pin,etc)
for i in h:
    print(h[i])#ethill koduthekunna alla iteam kittum
for i in h.keys():
    print(i)
for i in h.values():
    print(i)
for i in h.items():
    print(i)
l=h.copy()#to copy the iteams we entered
print(l)
p=dict(h)
print(p)
h.pop("name")
print(h)#its means remove the selected iteam
h.popitem()#remove last iteam
print(h)
del h["place"]#delete
print(h)
h.clear()
print(h)
del h