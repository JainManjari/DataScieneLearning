import asyncio
import time


async def waited(n):
    await asyncio.sleep(n)
    print(f"waited for {n} seconds")


async def main():
    # asynchro creating tasks

    task1=asyncio.create_task(waited(2))
    task2=asyncio.create_task(waited(3))

    print(time.strftime('%X'))
    # await task1 #leading to completion
    # await task2 #leading to completion
    # await asyncio.sleep(10)
    print(time.strftime('%X'))


    # synchronously waiting for the program to end
    # print(time.strftime('%X'))
    # await waited(2)
    # await  waited(3)
    # print(time.strftime('%X'))
    # print("Hello")
    # await asyncio.sleep(1)
    # print("World!")


if __name__=="__main__":
    asyncio.run(main())
    print("Program ended!")