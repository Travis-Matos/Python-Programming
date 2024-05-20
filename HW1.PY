# Problem 1.1
x = 3
y = 12
print(x + y)


#Problem 1.2
a = 250.75
b = 100.5
print (a - b)


 #Problem 1.3
c = 15.0
d = 10.0
print (c * d)

#Problem 1.4
num1 = 500
num2 = 20
print(num1 / num2)

#Problem 1.5
f = 13.4
g = 27.6
print(f + g)

#Problem 1.6
num3 = 10000.5
num4 = 3000
print(num3 * num4)

#Problem 1.7
num5 = 500.5
num6 = 25
print(num5 / num6)

#Problem 2.1
gpt_version = "GPT-4"
print(gpt_version)

#Problem 2.2
def check_declarations(declarations):
    try:
        exec(declarations)
        return True
    except Exception as e:
        return False 
declarations = [
    'model_version = 3.5',
    'model4 = "GPT-4" ',
    '2model = "GPT-2"',
    'rst_last_name = "john_doe"',
    'Hello! = 0.283',
    'variable_24 = "OpenAI"',
    'str = "string"'
]
print ("which one of the following declarations is incorect? Enter a number.")

for i, declarations in enumerate(declarations,1):
    print(f"{i}. {declarations}")
    
user_input = input("Enter the number of which is incorrect declaration: ").strip()
try:
    user_choices = int (user_input) - 1
    if 0 <= user_choices < len(declarations):
        declarations = declarations[user_choices]
        if check_declarations(declarations):
            print(f"Incorrect. The declaration '{declarations}' is actually correct.")
        else:
            print(f"Correct! The declaration '{declarations}' is incorrect.")
    else:
        print("Invalid choice. Please enter a number that is stated above of one of the declarations.")
except ValueError:
    print("Invalid input. Enter a number form 1-6.")        
    

print()

#Problem 3.1
for i in range (1,6):
    print (i)

#Problem 3.2
