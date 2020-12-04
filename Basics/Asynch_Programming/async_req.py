import asyncio
import aiohttp
import time


async def fetchFromGoogle():
    url = "https://www.google.com"
    session = aiohttp.ClientSession()
    resp=await session.get(url)

    # async with open("file.txt","r") as file:
    #     await resp.content.read(256)

    await resp.content.read()#print(await resp.content.read())#print(resp.content) #print(resp)
    await session.close() #important


async def main():
    print(time.strftime('%X'))
    await asyncio.gather(
        *[
            fetchFromGoogle() for i in range(70)
        ]
    )
    #await asyncio.gather(
    #  fetchFromGoogle(),
    #  fetchFromGoogle(),
    #  fetchFromGoogle(),
    #  fetchFromGoogle()
    # )
    # for i in range(70):
    #     await fetchFromGoogle()
    print(time.strftime('%X'))


if __name__=="__main__":
    asyncio.run(main())
    print("Program Ended!")