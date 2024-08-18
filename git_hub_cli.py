import requests
username  =  input()
url  = f'https://api.github.com/users/{username}/events'
try :
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        posts = response.json()
        print("OutPut:")
        print (posts)
    else:
        print('Error:', response.status_code)
except requests.exceptions.RequestException as e:
    print('Error:', e)
    
if __name__ == '__main__':
    pass 
