import aiohttp
import asyncio
import aiofiles


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        html = await response.text()
        return html


async def write_to_file(file, text):
    async with aiofiles.open(file, 'w') as f:
        await f.write(text)


async def main(urls):
    tasks = []
    for url in urls:
        file = f'{url.replace(":","_").replace("/","_").split("//")[-1]}.txt'
        html = await fetch(url)
        tasks.append(write_to_file(file, html))

    await asyncio.gather(*tasks)


urls = ["http://127.0.0.1:8000/category/1/", "http://127.0.0.1:8000/category/2/", "http://127.0.0.1:8000/category/3/"]

asyncio.run(main(urls))

