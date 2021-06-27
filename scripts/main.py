from datetime import datetime
from os import read

user_data = "No Test"

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('user_data.txt', 'r') as f:
    user_data = f.readline()
    print("PRINT FROM PYTHON: USAR_DATA = " + user_data)

    with open('output.txt', 'w') as w:
        w.write(user_data + ' #  ' + timestamp)
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
