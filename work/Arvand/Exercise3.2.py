import subprocess

try:
    subprocess.run("nice -n -19 sleep 30", shell=True, check=True) # shell = true to utilize bash shell; check = true to raise a CalledProcessError
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")