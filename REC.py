import asyncio
import telnetlib

# NOTICE : the hyperdeck have a strange behaviour : if the PLAY button was pressed before launching this RECORD command, the REC does NOT start, 
# it has to be triggered twice. Yet, the server replies 200 OK as usual even if it does not start recording. 
# As it is not possible to know beforehand if PLAY was pressed, the only workaround is to check if all the recorders have started. 
# If not, use the STOP command and trigger the REC command a second time and it will always work.

async def execute_telnet_command(semaphore, host, port):
    async with semaphore:
        try:
            with telnetlib.Telnet(host, port) as tn:
                tn.write(b"RECORD\n")
                tn.write(b"QUIT\n")
        except Exception as e:
            print(f"An error occurred: {e}")

async def main():
    semaphore = asyncio.Semaphore(6)  # Limit to 3 concurrent connections
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
