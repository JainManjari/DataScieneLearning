def print_fancy_name(prefix):
    try:
        while True:
            name=(yield)
            print(prefix+":"+name)
    except GeneratorExit:
        print("Done!")


co=print_fancy_name("Cool")

print(type(co))

#Initializing

print(next(co))

#Sending and Controlling

print(co.send("mj"))

print(co.send("bv"))

#Closing

print(co.close())