import asyncio

async def funk():
    a = 1
    while a !=25:
        if a%3 == 0:
            print(a)
        a+=1
        await asyncio.sleep(0.1)

async def funk2():
    a = 1
    while a != 25:
        print('Jack {}'.format(a))
        a+=1
        await asyncio.sleep(1)


async def main2():
    task1 = asyncio.create_task(funk())
    task2 = asyncio.create_task(funk2())
    await task1
    await task2

if __name__ == '__main__':
    m_loop = asyncio.get_event_loop()
    m_loop.run_until_complete(main2())
