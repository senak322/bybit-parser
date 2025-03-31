from utils import multiply

number = 10
text = "Hello python"

def greet(name):
    if name:
        print(f"hello {name}")
    else:
        print("hello stranger")

greet("Иван")
greet("")

names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)

count = 0

while count < 3:
    print(f"Счетчик {count}")
    count +=1

result = multiply(5, 12)
print(result)