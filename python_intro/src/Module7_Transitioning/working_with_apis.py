import asyncio
import httpx

async def fetch_data(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def process_data(data):
    print(f"Processing data: {data}")
    await asyncio.sleep(1)  # Simulates processing time
    return f"Processed data: {data['key']}"  # Example key

async def main():
    url = "https://api.example.com/data"  # Replace with a valid API URL
    data = await fetch_data(url)
    
    if data:
        result = await process_data(data)
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
