import requests
def send_req(ip):
    myobj = {'somekey': 'somevalue'}
    x = requests.post(ip, data = myobj)

    print(x.text)

ip = input("Enter ip: ")
while True:
    send_req(ip)