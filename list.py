names = ['hanna', 'alex', 1,23,4.6, True]
print(type(names))
print(len(names))
print(names[4])
print(names[-6])

# list unpacking 
students =['Beka', 'yeabsira', 'Bisrat', 'Desalegn', 'Josh' , 'abebe']
first, second , *third = students

# negtive indexing 
print(students[-4])

#slicing 
new_students = students[2:4]
print(new_students)

# slicing by negative indexing
top_students = students[-3:-1]
print(top_students)

# modifying 

students[0] = 'Maste'
print(students)

# cheking element in a list 
print('hanna' in students)
print('Bisrat' in students)

# addding element to a list 

students.append('hanna')
print(students)

# Inserting item in specfic index
students.insert(2,'kale')
print(students)

# pop it shows the last element and removes it from the list 
print(students.pop())

# remove removing specfic element
students.remove('Bisrat')
print(students)

# copying a list
new = students.copy()
print(new)

# joining two lists
numbers = ['44', '45', '46', '47']
joined = students + numbers