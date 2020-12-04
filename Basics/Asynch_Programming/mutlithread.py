from threading import Thread
import time
from queue import Queue

def sq(num):
    print("Sq is:", num ** 2)


def cube(num):
    print("Cube is:", num ** 3)


t1=Thread(target=sq,args=(4,))
t2=Thread(target=cube,args=(3,))

print(time.strftime('%X'))
print(t1.start())
print(t2.start())
print("hello")
print(time.strftime('%X'))

#waiting for resouces to get complete=> synch
t1.join()
print(time.strftime('%X'))
t2.join()
print(time.strftime('%X'))


def producer(q):
    for i in range(5):
        q.put(i)
        print("published", i)


def consumer(q):
    while True:
        data = q.get()
        print("consumed", data)



q=Queue()

producer_thread=Thread(target=producer,args=(q,))
consumer_thread=Thread(target=consumer,args=(q,))

print(time.strftime('%X'))
print(consumer_thread.start())
print(producer_thread.start())
print(time.strftime('%X'))

producer_thread.join()
print(time.strftime('%X'))
consumer_thread.join()
print(time.strftime('%X'))








