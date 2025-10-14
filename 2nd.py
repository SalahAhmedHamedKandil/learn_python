# sr 19
# --------------numbers--------------
mycomplexNumber= 5+6j
print(type(mycomplexNumber))
print(f"the real number is :{mycomplexNumber.real}")
print(f"the real imaginary is :{mycomplexNumber.imag}")
print(type(float(10.1)))
print(type(complex(10.1)))
print(int(10.1))
print(type(int(10.1)))
#sr 20
#-----------------arithmetic operator --------------
print(30+10)  #
print(30-10)  #subtraction
print(30*10)  #multiplication
print(30/10)  #division
print(32%10)  #modulus
print(30**10) #exponent
print(35//10) #(=3)floor division
#-----------------list----------------------
my_list_cam_have=["salah","one","one",1,True]
print(my_list_cam_have)
my_list_cam_have[1:3]=["ahmed","hamed"]
print(my_list_cam_have)
# append
myOldFriend=["sala","ahmed"]
myNewFriend=["hamed","kandil"]
myOldFriend.append("hamed")
myOldFriend.append(myNewFriend)
myOldFriend.extend(myNewFriend)

print(myOldFriend)
myOldFriend.remove("ahmed")
print(myOldFriend)
# tuble
mytuple1="salah",
print(type(mytuple1))
mytuple2=("ahmed","hamed")
print(mytuple1+mytuple2)
print(mytuple1*2+mytuple2*3)
mytuple3=(0,1,2,3,4,5,6,7,8,9,10)

a=int(input("please enter the number "))
print(f"the position of the number is {mytuple3.index(a)}") #give you the first index only
print(f"in my tuble three when we use 'index' give\
 us 1 because it take the first index  ")
# ------------- set ---------------
print(" set not ordered and imdex")
myset1={"salah","ahmed",27}
print(f"my set 1 is {myset1}")

myset2={1,2,3,4,5,6,7,8,9,10}
print(f"my set 1 is {myset2}")
myset1.clear()
print(myset1)
print(f"myset1.union(myset2)= {myset1.union(myset2)}")



