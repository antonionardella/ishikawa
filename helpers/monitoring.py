import json
import subprocess
import time
from helpers.logger import setup_logger
from ping3 import ping

# Set up the logger
setup_logger()


def ping_hosts(bot, channel_id, hosts):
    for host in hosts:
        try:
            response = ping(host)
            if response is not None:
                print(f'{host}: Ping response time is {response} ms')
            else:
                print(f'{host}: No response. Sending message to Discord...')
                send_discord_message(bot, channel_id, f"{host} is not responding!")
        except Exception as e:
            print(f'Error pinging {host}: {e}')

async def send_discord_message(channel_id, message):
    channel = channel_id
    if channel:
        await channel.send(message)
    else:
        print(f"Error: Channel with ID {channel_id} not found.")

def ping_bot(hosts):
    hosts = hosts
    
    if not hosts:
        print("No hosts found in the JSON file.")
        return
    
    print("Starting Ping Bot...")
    
    while True:
        ping_hosts(hosts)
        time.sleep(60)  # Adjust the interval as needed

if __name__ == "__main__":
    json_file = "ping_bot_hosts.json"  # Change this to your JSON file path
    ping_bot(json_file)