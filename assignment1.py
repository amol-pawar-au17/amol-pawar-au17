#What are the default data types in python? What is typecasting in python? 
#Give two examples each of typecasting between each of the following types:
#a. string to boolean
#b. integer to boolean
#c. boolean to string
#d. string to integer

*data types in python.
string
integer
float
boolean

* typecasting in python -convert one data type from other data type is call typecasting

#a.string to boolean

pr="2<5"
print(pr,type(pr))
pr=bool(pr)
print(pr,type(pr))

num1= 2
num2= 2-5
pr= "num2>num1"
print(pr,type(pr))
pr=bool(pr)
print(pr,type(pr))

#b.integer to boolean

pr=7
print(pr,type(pr))
pr=bool(pr)
print(pr,type(pr))

pr=89*4
print(pr,type(pr))
pr=bool(pr)
print(pr,type(pr))

#c.boolean to string

pr=5>3
print(pr,type(pr))
pr=str(pr)
print(pr,type(pr))

pr=9<2
print(pr,type(pr))
pr=str(pr)
print(pr,type(pr))

#d.string to integer

pr= "2"
print(pr, type(pr))

pr=int(pr)
print(pr,type(pr))

pr="578"
print(pr,type(pr))

pr=int(pr)
print(pr,type(pr))