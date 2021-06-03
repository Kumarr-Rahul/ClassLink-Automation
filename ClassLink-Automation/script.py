from twilio.rest import Client

account_sid = 'Your account sid'
auth_token = 'Your token'
client = Client(account_sid, auth_token)

MathsLink = "https://meet.google.com/rqz-ijub-qhm"
FLATlink = "https://meet.google.com/xgf-xpxr-xjz"
CALink = "https://meet.google.com/iyq-jdri-djk"
AnalysisAlgoLink = "https://meet.google.com/jfw-aitt-iub"
EVSlink = "https://meet.google.com/ryg-ppvq-zxs"
BiologyLink = "https://meet.google.com/hyz-oryj-auh"

def send():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Maths class is "+ MathsLink,
        to='whatsapp:+9195********'
    )
    print(message.sid)


def send1():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for Formal Language & Automata theory class is "+ FLATlink,
        to='whatsapp:+9195********'
    )
    print(message.sid)


def send2():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Computer Architecture class is "+ CALink,
        to='whatsapp:+9195********'
    )
    print(message.sid)


def send3():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Design And Analysis of Algorithm class is "+ AnalysisAlgoLink,
        to='whatsapp:+9195********'
    )
    print(message.sid)

def send4():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Environmental Science class is "+ EVSlink,
        to='whatsapp:+9195********'
    )
    print(message.sid)

def send5():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Biology class is "+ BiologyLink,
        to='whatsapp:+9195********'
    )
    print(message.sid)    