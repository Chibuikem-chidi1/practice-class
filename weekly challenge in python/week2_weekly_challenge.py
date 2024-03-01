#number 1
num4 = 40
num5 = 50
num6 = 60
num7 = 70
user_input = num4 + num5 + num6 + num6
print(user_input)
#number2
favourite_books = ('Purple hibiscus', 'Americanah', 'Half of a yellow sun')
for x in favourite_books:
    print('these are my favourite books:', x)
#number 3
person_info = {}

# Ask the user for input and store information in the dictionary
person_info['name'] = input("Enter the person's name: ")
person_info['age'] = int(input("Enter the person's age: "))
person_info['favorite_color'] = input("Enter the person's favorite color: ")

# Print the dictionary to the console
print("\nPerson's Information:")
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")



#number 4
num1 = {10, 20, 30, 40, 50, 60, 70}
num2 = {80, 90, 25, 30, 40, 50, 35}
num1.intersection(num2) 
 

#number 5
fruits = ['banana', 'orange', 'mango', 'lemon','tomato', 'potato', 'cabbage','onion', 'carrot']
new_list = []
new_list1 = []
new_list2 = []
for x in fruits:
    if 'a' in x:
        new_list.append(x)
print(new_list)
for x in fruits:
    if "c" in x:
        new_list1.append(x)
print(new_list1)
for x in fruits:
    if "e" in x:
        new_list2.append(x)
print(new_list2)




