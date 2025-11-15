def greet(name):
    return 'hello ' + name

name = str(input('Insert your name: '))
height = float(input('Insert your height (in meters): '))
weight = float(input('Insert your weight (in kg): '))
age = int(input('Insert your age: '))
gender = str(input('Insert your gender (m/f): '))

def bmi():
    BMI = weight / (height ** 2)
    print('Your BMI is: ' + str(BMI))

def bmr_men():
    BMR = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    print('Your BMR is: ' + str(BMR))

def bmr_female():
    BMR = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)
    print('Your BMR is: ' + str(BMR))

if gender.lower() == "m":
    bmi()
    bmr_men()
else:
    bmi()
    bmr_female()
def bk():
    print('Beka')    
