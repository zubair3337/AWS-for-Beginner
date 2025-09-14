import subprocess

cmd = "df -h"
result = subprocess.run(cmd, shell=True, text=True, capture_output=True)

print(result.stdout)  # Output of the command
