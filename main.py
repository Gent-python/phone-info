try:
    import requests
except ImportError:
    import os
    os.system('pip install requests')

try:
    import time
except ImportError:
    import os
    os.system('pip install time')

import os

os.system('clear')

print('\n        \033[33mGit hub \033[36m: \033[35mgent_python')
time.sleep(1)
print('\n        \033[33mInstagram \033[36m: \033[35mgent_python')
time.sleep(1)
print('\n        \033[33mTelegram \033[36m: \033[35mgent_python')
time.sleep(1)
print('\n        \033[91mcreat by \033[36m: \033[34mMr Sadeghi\n\n\n')

Licens = input('\033[31mEnter your license \033[32m >>>')
num = input('\033[93menter the phone number \033[0m(09*********)\033[91m>>> \033[97m')

req = requests.get(f'https://api3.haji-api.ir/majid/tools/number/book?phone={num}&license={Licens}').json()['result'][0]

print(f'\033[95mNumber \033[97m: \033[32m{req["Number"]}\n')
print(f'\033[95mName \033[97m: \033[32m{req["Name"]}\n')
print(f'\033[95mFamily \033[97m: \033[32m{req["Family"]}\n')
print(f'\033[95mAddress \033[97m: \033[32m{req["Address"]}\n')
print(f'\033[95mCity \033[97m: \033[32m{req["City"]}\n')
print(f'\033[95mPersonal Code \033[97m: \033[32m{req["PersonalCode"]}\n')
print(f'\033[95mOther number \033[97m: \033[32m{req["Othernumber"]}\n')
print(f'\033[95mMail \033[97m: \033[32m{req["Mail"]}\n')
