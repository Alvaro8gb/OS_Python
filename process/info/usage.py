import psutil


# Get detailed resource usage information
process = psutil.Process()
memory = process.memory_info()

print(f"Memory Usage - RSS: {memory.rss} bytes, VMS: {memory.vms} bytes")

# Other
shared_value = memory.shared
text_value = memory.text
lib_value = memory.lib
data_value = memory.data
dirty_value = memory.dirty

# Print the values
print(f"Shared: {shared_value} bytes")
print(f"Text: {text_value} bytes")
print(f"Lib: {lib_value} bytes")
print(f"Data: {data_value} bytes")
print(f"Dirty: {dirty_value} bytes")

 
scputimes = psutil.cpu_times()

print(f"""
Timing info:
    User Time: {scputimes.user} seconds
    Nice Time: {scputimes.nice} seconds
    System Time: {scputimes.system} seconds
    Idle Time: {scputimes.idle} seconds
    I/O Wait Time: {scputimes.iowait} seconds
    IRQ Time: {scputimes.irq} seconds
    SoftIRQ Time: {scputimes.softirq} seconds
    Steal Time: {scputimes.steal} seconds
    Guest Time: {scputimes.guest} seconds
    Guest Nice Time: {scputimes.guest_nice} seconds
""")
