
fruits = ['apple', 'banana', 'cherry', 'date']


print("Fruits in the list:")
for fruit in fruits:
    if fruit == 'cherry':
        continue  
    print(fruit)


print("\nNumbers from 0 to 4:")
count = 0
while count < 5:
    if count == 3:
        break 
    print(count)
    count += 1


print("\nMultiplication Table:")
for i in range(1, 4):  
    for j in range(1, 4): 
        print(f"{i} * {j} = {i * j}")
    print()  


print("Enumerating fruits:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
