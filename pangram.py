import string
id=input("type your name    ")
v={ "a":0,
   "e":0,
   "i":0,
   "o":0,
   "u":0,
}
for i in id:
    if i in v:
        v[i]+=1

print(v)        
abc={}
for i in string.ascii_lowercase:
    abc[i]=0

pangram=False
count=0
#ifinot inv
for i in id :
    if i in abc:
        abc[i]+=1
for i in abc:
    if abc[i]>0:
      count+=1
if count==26:
    print("pangram")
else:
    print("this is not a panogram")

print (count)
print(abc)    