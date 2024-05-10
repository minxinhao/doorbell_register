# -*- coding: utf-8 -*-

import threading
from fabric import Connection
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num_servers", type=int, help="Number of servers to run the command on")
parser.add_argument("command_type", choices=["server", "client","clean"], help="Command type to run")
parser.add_argument("--nr_thread", help="number of thread")
parser.add_argument("--rdma_depth", help="outstanding work request per thread")
args = parser.parse_args()

# 然后将 num_servers 用作运行命令的服务器数量
num_servers = args.num_servers
command_type = args.command_type
nr_thread = args.nr_thread
rdma_depth = args.rdma_depth

# Define the connection information for each server
servers = [
    {'host': '192.168.1.51', 'user': 'mxh', 'password': 'mxh'},
    {'host': '192.168.1.52', 'user': 'mxh', 'password': 'mxh'},
    {'host': '192.168.1.53', 'user': 'mxh', 'password': 'mxh'},
    {'host': '192.168.1.10', 'user': 'mxh', 'password': 'mxh'},
    {'host': '192.168.1.11', 'user': 'mxh', 'password': 'mxh'},
    {'host': '192.168.1.12', 'user': 'mxh', 'password': 'mxh'},
    {'host': '192.168.1.13', 'user': 'mxh', 'password': 'mxh'},
    {'host': '192.168.1.14', 'user': 'mxh', 'password': 'mxh'},
    # Add more servers if needed
]

# Create a list of Connection objects for each server
connections = [Connection(host=server['host'], user=server['user'], connect_kwargs={"password": server['password']}) for server in servers]

# Define a task to run on all servers
def server_command(i):
    conn = connections[i]
    print(f"server: {conn.host}")
    # conn.run('killall multi_rdma', warn=True)
    result = conn.run(f'cd server && ./run_mxh.sh server ') 

def client_command(i):
    conn = connections[i]
    print(f"client: {conn.host}")
    print("nr_thread",nr_thread,"rdma_depth",rdma_depth)
    result = conn.run(f'cd client && ./run_mxh.sh {nr_thread} {rdma_depth} ') 

def clean_command(i):
    conn = connections[i]
    print(f"client: {conn.host}")
    conn.run('killall test_rdma', warn=True)
    conn.run('free -h', warn=True)

# Execute the task on all servers
threads = []
for i in range(num_servers):
    if command_type == "server":
        thread = threading.Thread(target=server_command, args=(i,))
    elif command_type == "client":
        thread = threading.Thread(target=client_command, args=(i,))
    elif command_type == "clean":
        thread = threading.Thread(target=clean_command, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()