import requests

payload = {
    'content': "Hello" 
}

header = {
    'authorization': "OTAyMDc0MTY1MjUzNzkxNzk1.YbENYQ.oODAGhGs15r4G35hpplQR87Ryh4"
}

files = {
    'file': ('./EXPRESS_GAME.pdf', open('./EXPRESS_GAME.pdf', 'rb'))
}

# dm_data = [x for x in r if x['recipients'][0]['id'] == users_to_send_message[0]]
# r = requests.post(f"https://discord.com/api/v9/channels/{dm_data[0]['id']}/messages", headers=headers, data={'content': message_to_send, 'tts': False}, files=files)

with open('f.txt') as f:
    a = []
    for line in f.readlines():
        log, passw, ip, port = line.strip().split(':')
        a.append({'http' : f'http://{log}:{passw}@{ip}:{port}'})
    print(a)