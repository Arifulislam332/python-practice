"""# this is the X value.
x=5
# this is the Y value.
y=2
# summation
sum=x+y
# subtraction
sub=y-x
# multiplication
# mul=x*y
# division
divi=x/y"""

""""
hello bangladesh!
"""

"""print(sum)
print(sub)
print(mul)
print(divi)"""

# country_name="Bangladesh"

# print(country_name)

# _my_name="Ayatullah Arif"

# print(_my_name)

# MY_EMAIL_ID='ayatullaharif332@gmail.com'
# print(MY_EMAIL_ID)

# DATA TYPE
"""# integer data type
telephone= 1936711314
# print(telephone)
roll_number=56
# print(roll_number)

result=55.5
# print(result)"""

"""international_country=["denmark","australia","japan","china"]

print(international_country)
print(international_country[3])"""

"""mul_data=[2,"arif",2.45,55,"bangladesh","XIII"]

print(mul_data[5])

dabble__data=[2,2,3,3,"china","thailand","china"]

print(dabble__data[5])
"""

"""complex_data=2.2+4j

print(complex_data)"""


"""players=("naymar","messi","ronaldo",'martinij')

print(*players)
"""

"""numbers=range(1,13,5)
print(*numbers)"""

# BOOLEAN DATA TYPE

"""isBangladeshi= True
print(isBangladeshi)"""

# NONE DATA TYPE
"""name=None
print(name)"""

# MAPPING DATA TYPE
# dictionary data
"""student= {
    'name':'Ariful Islam',
    'roll':34,
    'class':'XIII',
    'isBangladeshi': True
}"""

# print(student['roll'])
# print(student['class'])
# print(student['isBangladeshi'])

# SET - mutable

"""common_str= {"Arif", "Sofik", "Rofik", "Arif",2,5,2}

print(common_str)

# frozenSet - immutable
common_str=frozenset([1,2,34,1,3,43,34])
check= type(common_str)
print(check)
"""

"""student={
    'name':'Arif'
}
print(student)"""

# IMMUTABLE TYPES DATA
# 1- integer
# 2- floating point numbers
# 3- strings
# 4- tuples
# 5- frozen sets

# ----string---
"""national_fish="cat-fish"
location_check1=id(national_fish)

national_fish="Hilsha"
location_check2=id(national_fish)

print(national_fish)
print(location_check1)
print(location_check2)"""

# --- tuples----
"""fruits_name= ("mango", "litchi", "papaya", "cherry")
tuples1_location=id(fruits_name)

fruits_name=("banana","pine-apple","apple","grap")
tuples2_location=id(fruits_name)

print(tuples1_location)
print(tuples2_location)"""

# ---frozenSet---
"""human_names=frozenset({"alex","jemmy","richard","rose"})
frozenSet_location=id(human_names)
human_names=frozenset({"alex","jemmy","richard","rose"})
frozenSet2_location=id(human_names)
print(frozenSet_location)
print(frozenSet2_location)"""

# MUTABLE TYPES DATA
# 1- list
# 2- dictionaries
# 3- sets

# ----lists----
"""numbers=[1,23,43,54]
first_numbers=id(numbers)
numbers[3]="litchi"
second_numbers=id(numbers)
print(first_numbers)
print(second_numbers)"""

# ----dictionaries----
"""tiger={
    'name':'Tiger',
    'live':'forest',
    'isDangerous':True
}
tiger1_location=id(tiger)
tiger['isDangerous']=False
tiger['live']="home"
print(tiger)
tiger2_location=id(tiger)
print(tiger1_location)
print(tiger2_location)"""

# ----sets---
"""str= {"a", "b", "c","a","c"}
str1=id(str)
str.add(23)
str2=id(str)
print(str1)
print(str2)
"""

"""x=56
y=str(x)
z=float(x)
check=type(z)
# print(check)

try:
    animal = "Lion"
    convert_float = float(animal)
    print(convert_float)
except Exception as e:
    print(e)"""