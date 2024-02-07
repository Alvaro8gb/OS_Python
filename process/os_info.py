import subprocess

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)
    return result.stdout.strip()

# Get system information
kernel_version = run_command("uname -r")
hostname = run_command("hostname")
cpu_info = run_command("lscpu")
memory_info = run_command("free -h")

# Display the information
print(f"Kernel Version: {kernel_version}")
print(f"Hostname: {hostname}")
print(f"CPU Information:\n{cpu_info}")
print(f"Memory Information:\n{memory_info}")
