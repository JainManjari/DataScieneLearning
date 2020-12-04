def add(a, b):
    return a+b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def sub(a, b):
    return a - b


def mod(a, b):
    return a % b

#this part will only run when we particularly run simple.py


if __name__ == "__main__":
    print("hello")
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print(add(a,b))