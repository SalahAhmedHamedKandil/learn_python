#for training
name=input("what is your name : ")
rank= input("enter your rank : ")
rank=int(rank)
# print(rank)
# print(name)
list=(f"my name is {name} and my rank is  {rank}")
firstlist=list.split()
print(firstlist)
print(list)

print(f"welcome to our company  {firstlist[3]} ,and yor ramk is\
#  {rank:.1f}")
# cairo= input("is your city nearby cairo ? (yes or no ) :")