import asyncio
import telnetlib

async def execute_telnet_command(semaphore, host, port):
    async with semaphore:
        try:
            with telnetlib.Telnet(host, port) as tn:
                tn.write(b"PLAY\n")
                tn.write(b"QUIT\n")
        except Exception as e:
            print(f"An error occurred: {e}")

async def main():
    semaphore = asyncio.Semaphore(6)  # Limit to 6 concurrent connections
    tasks = [
        execute_telnet_command(semaphore, "192.168.10.11", 9993),
        execute_telnet_command(semaphore, "192.168.10.12", 9993),
        execute_telnet_command(semaphore, "192.168.10.13", 9993),
        execute_telnet_command(semaphore, "192.168.10.41", 9993),
        execute_telnet_command(semaphore, "192.168.10.42", 9993),
        execute_telnet_command(semaphore, "192.168.10.43", 9993)
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
