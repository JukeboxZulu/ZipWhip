import requests

auth_url = 'https://api.zipwhip.com/user/login'
logout_url = 'https://api.zipwhip.com/user/logout'
send_url = 'https://api.zipwhip.com/message/send'
contact_url = 'https://api.zipwhip.com/contact/save'


def login():
    # Start Session and define session ID
    print('Logging in...')
    res = requests.post(auth_url, data={'username': 'brad5416860001@(541) 686-0001', 'password': '0r4ng3W@1ru535'})
    session = res.json().get('response')
    return session


def logout(session):
    # End Session w/ Session ID
    res = requests.post(logout_url, data={'session': session})
    if res.json().get('success'):
        print('Logged out successfully.')
    elif not res.json().get('success'):
        print('Logout failed.')
    return res


def send(session, contacts, message):
    res = requests.post(send_url, data={'session': session, 'contacts': contacts, 'body': message})
    if res.json().get('success'):
        print('Sent successfully.')
    elif not res.json().get('success'):
        print('WARNING: Sending failed.')
    return res


def create_contact(session, first, last, number):
    requests.post(contact_url, data={
        'session': session,
        'firstName': first,
        'lastName': last,
        'mobileNumber': number
    }
                                   )