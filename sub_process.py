from re import sub
import subprocess

# subprocess.run('htop')  # simple command

list_of_files = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(list_of_files.stdout)
