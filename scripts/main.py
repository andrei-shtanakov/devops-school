from os import read

user_data = ""

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('user_data.txt', 'r') as f:
    user_data = f .readline()

with open('log.md', 'w') as f:
    f.write(f'# {timestamp}')

with open('output.txt', 'w') as f:
    f.write(f'{user_data}  # {timestamp}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
