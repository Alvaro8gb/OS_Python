import subprocess

command = ['nice', '-n', '19', 'sleep', '30']

process = subprocess.Popen(command)
process.wait()
