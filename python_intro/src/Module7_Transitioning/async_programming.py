"""
Asynchronous programming is a crucial concept in both Python and JavaScript, allowing for non-blocking operations, particularly in I/O-bound applications.

### Python Async Programming
- **Syntax**: Python uses the `async` and `await` keywords. 
    Functions defined with `async` return a coroutine, 
    which can be awaited using the `await` keyword.
- **Concurrency Model**: Python's `asyncio` library provides an event loop 
    that manages the execution of asynchronous tasks. 
    The event loop runs and schedules coroutines, handling context switching.
- **Error Handling**: Errors in asynchronous functions can be handled 
    with try/except blocks, similar to synchronous code.
- **Use Cases**: Ideal for I/O-bound operations, such as web requests, file I/O, and database queries.

### JavaScript Promises
- **Syntax**: JavaScript uses `Promise` objects to handle asynchronous operations. 
    Promises can be in one of three states: pending, fulfilled, or rejected.
- **Chaining**: Promises allow for chaining using `.then()` 
    for fulfilled promises and `.catch()` for handling errors. 
    This provides a clear way to handle sequences of asynchronous operations.
- **Async/Await**: Introduced in ES2017, JavaScript also supports `async` and `await`, similar to Python. 
    This syntactic sugar makes working with promises more readable, 
    allowing you to write asynchronous code that looks synchronous.
- **Use Cases**: Commonly used for handling asynchronous operations like HTTP requests, timers, and event handling.

### Comparison
- **Event Loop**: Both Python and JavaScript use an event loop to manage asynchronous tasks, but their implementations differ. Python's `asyncio` is more explicit, while JavaScript's event loop is integrated into the runtime.
- **Error Handling**: Error handling in Python with async functions is straightforward with `try/except`, while JavaScript uses `.catch()` to handle errors in promise chains.
- **Complexity**: Promises can lead to "callback hell" if not handled correctly, but async/await syntax in JavaScript mitigates this. Python's async/await provides similar clarity.

Overall, both languages offer robust mechanisms for asynchronous programming, each with its own strengths and idiomatic usage patterns.
"""

import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates a network call
    return {"data": "Sample data"}

async def process_data(data):
    print(f"Processing data: {data}")
    await asyncio.sleep(1)  # Simulates processing time
    return f"Processed {data['data']}"

async def main():
    # Fetch data
    data = await fetch_data()
    
    # Process the fetched data
    result = await process_data(data)
    
    print(result)

## Basic Try-Except

# async def main():
#     try:
#         # Fetch data
#         data = await fetch_data()
        
#         # Process the fetched data
#         result = await process_data(data)
#         print(result)
#     except Exception as e:
#         print(f"An error occurred: {e}")

 ## Handling Specific Exceptions

# async def fetch_data():
#     print("Fetching data...")
#     await asyncio.sleep(2)  # Simulates a network call
#     # Simulate an error
#     raise ValueError("Failed to fetch data")

# async def process_data(data):
#     print(f"Processing data: {data}")
#     await asyncio.sleep(1)  # Simulates processing time
#     return f"Processed {data['data']}"

# async def main():
#     try:
#         # Fetch data
#         data = await fetch_data()
        
#         # Process the fetched data
#         result = await process_data(data)
#         print(result)
#     except ValueError as ve:
#         print(f"ValueError occurred: {ve}")
#     except Exception as e:
#         print(f"An error occurred: {e}") 


## Using Finally

# async def main():
#     data = None
#     try:
#         # Fetch data
#         data = await fetch_data()
        
#         # Process the fetched data
#         result = await process_data(data)
#         print(result)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         if data is not None:
#             print("Data fetch was attempted.")
#         else:
#             print("Data fetch was not successful.")

## Nested Try-Except Blocks

# async def main():
#     try:
#         # Fetch data
#         data = await fetch_data()
        
#         try:
#             # Process the fetched data
#             result = await process_data(data)
#             print(result)
#         except RuntimeError as re:
#             print(f"RuntimeError occurred: {re}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())

