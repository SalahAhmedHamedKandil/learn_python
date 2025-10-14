#-------------------string-------------------
salah = "i love my daughter"
print(salah[3])   #index = o
print(salah[4])   #index = v
print(salah[-1])  #index = r
#---------slicing string---------------------
print(salah[1:8]) #' love m'
print(salah[:8])  #'i love m
print(salah[1:])  #' love my daughter'
print(salah[::2]) #' ilv yduhe'
#---------------- len -----------------------
print(len(salah)) #give us the count of the strin 

#--------------- strip & rstrip & lstrip------------------
a = "              i love pytho                "
print(a.strip())
print(a.rstrip())
print(a.lstrip())
print(len(a.strip()))
b="@@@@@@@@@@@@@ i love python @@@@"
print(b)
print(b.strip("@"))
print(b.rstrip("@"))
print(b.lstrip("@"))
print(len(b.strip()))
#--------title - capitalze - zfill - upper - lower ------
print(salah.title())
print(salah.capitalize())
c , d ,e = "1" ,"19" ,"999"
print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))
f="sAlaH"
print(f.upper())
print(f.lower())
# -----------split - rsplit ------------------
print(salah.split())
print(type(salah.split()))
g="i-love-my-doughter"
print(g.split('-'))
print(g.split('-',0))
print(g.split('-',1))    
print(g.split('-',2))    #  ['i','love','my doughter']
print(g.rsplit('-',0))   #  ['i-love-my-doughter']
print(g.rsplit('-',1))   #  ['i-love-my', 'doughter']
print(g.rsplit('-',2))   #  ['i-love', 'my', 'doughter'] 
# -----------center - count --------
h="salah"
print(h.center(9))     #  salah  
print(h.center(9,"*")) #**salah**
i="salah salah ahmed"
print(i.count("la"))     # =2
print(i.count("la",0,4)) # =1
print(i.count("la",0,9)) # =1




# sr 017 sting formating
salahAge=27
name="salah"
rank=10
# print("my name is"+name+"my age is "+salahAge) #error
print("my name is %s and my age is %d" % (name,salahAge))
print("my name is %s and my age is %d and my\
 rank %.3f" % (name,salahAge,rank))
# sr 18
print("my name is {:s}s and my age \
 is {:d}".format (name,salahAge))
print("my name is {} and my age is {} and my\
 rank {:.2f}" .format (name,salahAge,rank))
print("the fist code is {:.4s}".format(salah))
print("the fist code is {:s}".format(salah))
# rearange items
one,two,thre=1,2,3
print("reformating : {2} _ {1:d} _ {0:.4f}"\
.format(one,two,thre))
print(f"(f) reformating : {2} _ {1:d} _ {0:.4f}")





