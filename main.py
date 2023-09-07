# LINK TO THE PROGRAMMING PLAN : https://docs.google.com/document/d/1N-U7uMd1P9Ag5RtAJrodDq-DSvFPyUtatrgQ6N0LC2s/edit?usp=sharing


import array as arr  

data_list1 = arr.array('f', [])
data_list2 = arr.array('f', [])

def findMaleBodyDensity():
  chestSkinfold = float(input("Enter chest skinfold (mm): "))
  data_list1.append(chestSkinfold)
  abdomenSkinfold = float(input("Enter abdomen skinfold (mm): "))
  data_list1.append(abdomenSkinfold)
  thighSkinfold = float(input("Enter thigh skinfold (mm): "))
  data_list1.append(thighSkinfold)
  age = int(input("Enter your age in years: "))
  data_list1.append(age)
  waistCircumfrence = float(input("Enter your waist circumfrence in m: "))
  data_list1.append(waistCircumfrence)
  forearmCircumference = float(input("Enter your forearm circumference in m: "))
  data_list1.append(forearmCircumference)
  sumOfAllSkinfolds =(chestSkinfold+abdomenSkinfold+thighSkinfold)
  data_list1.append(sumOfAllSkinfolds)
  BodyDensity = 1.0990750 - 0.0008209*(sumOfAllSkinfolds) + 0.0000026* (sumOfAllSkinfolds**2) - 0.0002017*(age) - 0.005675*(waistCircumfrence) + 0.018586*(forearmCircumference)
  data_list1.append(BodyDensity)
  bodyFat = (495 / BodyDensity) - 450
  data_list1.append(bodyFat)
  print(bodyFat)
  if bodyFat <= 0:
    print("Oh, your body fat percentage calculations came out as a negative number or zero so you probably have done something wrong, so please make sure you put in the right numbers!")
    #print(type(data_list1))

def findFemaleBodyDensity():
  tricepsSkinfold = float(input("Enter triceps skinfold (mm): "))
  data_list2.append(tricepsSkinfold)
  thighSkinfold = float(input("Enter thigh skinfold (mm): "))
  data_list2.append(thighSkinfold)
  suprailiacSkinfold = float(input("Enter suprailiac skinfold (mm): "))
  data_list2.append(suprailiacSkinfold)
  age = int(input("Enter your age in years: "))
  data_list2.append(age)
  glutealCircumference = float(input("Enter your gluteal circumference in cm: "))
  data_list2.append(glutealCircumference)
  sumOfAllSkinfolds =(tricepsSkinfold+suprailiacSkinfold+thighSkinfold)
  data_list2.append(sumOfAllSkinfolds)

  BodyDensity = 1.1470292 - 0.0009376*(sumOfAllSkinfolds) + 0.0000030* (sumOfAllSkinfolds**2) - 0.0001156*(age) - 0.0005839*(glutealCircumference)
  data_list2.append(BodyDensity)
  bodyFat = (495 / BodyDensity) - 450
  data_list2.append(bodyFat)
  print("Your body fat is:",bodyFat,"%")
  if bodyFat <= 0:
    print("Oh, your body fat percentage calculations came out as a negative number or zero so you probably have done something wrong, so please make sure you put in the right numbers")
    


# def pop_function():
#   choice = input("Are you a male or female: ")
#   if choice.lower() == "male":
#     print(data_list1)
#     pop = int(input("For the data you want to delete, type the number: ")) 
#     pop = pop-1
#     data_list1.pop(pop)
#     print(data_list1)
#   if choice.lower() == "female":
#     print(data_list2)
#     pop = int(input("For the data you want to delete, type the number: "))
#     pop = pop-1
#     data_list1.pop(pop)
#     print(data_list2)
  
def menu():
  while True:
    print("1. Find Male Body Density")
    print("2. Find Female Body Density")
    print("3. Delete all Data")
    mode = input("Enter your choice: ")
    #userGender = input("Enter your gender(Male/Female): ")
    
    if mode == "1":
        findMaleBodyDensity()

    elif mode == "2":
        findFemaleBodyDensity()

    elif mode == "3":
        gender = input("What is your gender?\n Enter '1' for male\n Enter '2' for female: ")
        if gender == "1":
          for x in data_list1[:]: 
            data_list1.pop(-1)
          print(data_list1)
          break
        elif gender == "2":
          for y in data_list2[:]:
            data_list2.pop(-1)
          print(data_list2)
          break
    else:
      print("Not an available option")
      break

menu()


