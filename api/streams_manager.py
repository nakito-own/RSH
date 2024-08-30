import asyncio

clients_distribution = []

def add_distribution_client():
    queue = asyncio.Queue()
    clients_distribution.append(queue)
    return queue

async def notify_distribution_clients(data):
    for client in clients_distribution:
        await client.put(data)
