
tupple=(1,2,3,4,5)
print(tupple)
the_tupple=list(tupple)        #we have changed the value of the tuple
the_tupple[2]=78
print(the_tupple)
the_tupple=tuple(the_tupple)
print(the_tupple)



#to create the dictionary
stle={}
stle[1]=[1,2,3,4,5]
stle[2]=(2,3,4)
stle[23]={2:"monday","d":34}
stle[100]={2,4,6}
print(stle.keys())
print(stle.values())
print(type(stle[1]))
print(type(stle[2]))
print(type(stle[23]))
print(type(stle[100]))
print(stle)
