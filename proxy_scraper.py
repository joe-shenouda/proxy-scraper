import asyncio
import re
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text

async def extract_proxies(url):
    content = await fetch(url)
    pattern = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}(?::\d{1,5})?")
    proxies = re.findall(pattern, content)
    return proxies

async def main():
    proxy_sources = [
        "https://spys.me/proxy.txt",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4",
        "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5",
    ]

    proxies = []
    tasks = []

    for source in proxy_sources:
        tasks.append(asyncio.ensure_future(extract_proxies(source)))

    results = await asyncio.gather(*tasks)

    for result in results:
        proxies.extend(result)

    with open("proxies.txt", "w") as f:
        f.write("\n".join(proxies))

    print("Proxies have been saved to proxies.txt")

if __name__ == "__main__":
    asyncio.run(main())
