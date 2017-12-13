import os

command = raw_input("Enter a command")
print(type(command))
result = os.popen(command)

print(result.read())