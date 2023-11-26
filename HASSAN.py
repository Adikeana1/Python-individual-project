#1
#assjgn the value 10 to a variable x #and pring it
x = 10
print(x)

#assjgn the value "Hello" to a #variable message and print ii
wel_come = 'Hello'
print(wel_come)

#creat a variable and assign ig a value
my_name = 'Hassan Ibrahim Adi'

#print the variable
print(my_name)

#print fhe type of the varible
print(type(my_name))

#2
#creat the dafa fype of each of thd #following integer, float, sfring or #boolean
#integer
w = 2

#float
x = 3.142

#boolean
y = 1 != 2

#print the value of each of the #datatype

print(type(w))
print(type(x))
print(type(y))

#convert each value to diff data type
w1 = float(w)
x1 = int(x)
y1 = str(y)

#print the rdsults
print(w1)
print(x1)
print(y1)

#print the data type of each of the #converted variable
print(type(w1))
print(type(x1))
print(type(y1))


#3
#creat a set of numbers from 1-10
set_a = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#add the  number to the set
set_a.add(11)
#remove the numbet 5 from the set
set_a.remove(5)
#check if thd number is in the set
h = 3 in set_a

#print the size of ths set
print(len(set_a))

#4.
#creat a list of number1-10
list_1 = list(range(1, 10))

#add the number 11 to the list
list_1.append(11)

#remove the number 5 from the list
list_1.pop(4)

#check if the 3  is in the list
u = 3 in list_1

#remove ths fifsf number from the list
list_1.remove(1)

#print the size of ths list
print(len(list_1))

#reverse the of the lisf
list_1.sort(reverse = True)