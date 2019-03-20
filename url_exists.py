import requests
try:
    request = requests.get('https://www.isystematic.com.pk/')
    print('Web site exists')
except Exception:
    print('Web site does not exist')

# if request.status_code == 200:
#     print('Web site exists')
# else:
#     print('Web site does not exist')