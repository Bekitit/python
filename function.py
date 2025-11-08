def greet(name):
    return 'hello ' + name

name = str(input('Insert your name: '))
height = float(input('Insert your height (in meters): '))
weight = float(input('Insert your weight (in kg): '))
age = int(input('Insert your age: '))
sex = str(input('Insert your gender (m/f): '))

def bmi():
    BMI = weight / (height ** 2)
    print('Your BMI is: ' + str(round(BMI, 2)))

def bmr_men():
    BMR = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    print('Your BMR is: ' + str(round(BMR, 2)))

def bmr_female():
    BMR = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)
    print('Your BMR is: ' + str(round(BMR, 2)))

if sex.lower() == "m":
    bmi()
    bmr_men()
else:
    bmi()
    bmr_female()
