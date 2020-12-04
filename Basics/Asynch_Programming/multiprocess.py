from multiprocessing import Process

def showSq(num=2):
    print(num**2)


procs=[]

for i in range(5):
    procs.append(Process(target=showSq))

for p in procs:
    p.start()

print("hello")