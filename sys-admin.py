import os
os.system("ls")

print()
print()

import subprocess
subprocess.run(["ls"])

print()
print()

import subprocess
subprocess.run(["ls","-l"])

print()
print()

import subprocess
subprocess.run(["ls","-l","README.md"])

print()
print()

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print()
print()


command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])