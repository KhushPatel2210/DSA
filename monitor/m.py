# import psutil
# import time

# def get_cpu_info():
#     print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
#     print("CPU Cores (Logical):", psutil.cpu_count(logical=True))
#     print("CPU Cores (Physical):", psutil.cpu_count(logical=False))


# def get_memory_info():
#     memory = psutil.virtual_memory()
#     print("\nMemory Usage:")
#     print("Total:", round(memory.total / (1024**3), 2), "GB")
#     print("Available:", round(memory.available / (1024**3), 2), "GB")
#     print("Used:", round(memory.used / (1024**3), 2), "GB")
#     print("Percentage:", memory.percent, "%")


# def get_disk_info():
#     disk = psutil.disk_usage('/')
#     print("\nDisk Usage:")
#     print("Total:", round(disk.total / (1024**3), 2), "GB")
#     print("Used:", round(disk.used / (1024**3), 2), "GB")
#     print("Free:", round(disk.free / (1024**3), 2), "GB")
#     print("Percentage:", disk.percent, "%")


# def get_network_info():
#     net = psutil.net_io_counters()
#     print("\nNetwork Usage:")
#     print("Bytes Sent:", round(net.bytes_sent / (1024**2), 2), "MB")
#     print("Bytes Received:", round(net.bytes_recv / (1024**2), 2), "MB")


# def main():
#     while True:
#         print("\n===== SYSTEM MONITOR =====")
#         get_cpu_info()
#         get_memory_info()
#         get_disk_info()
#         get_network_info()
#         print("\nRefreshing in 5 seconds...\n")
#         time.sleep(5)


# if __name__ == "__main__":
#     main()

import os

disk = os.popen("df -h").read()
print(disk)