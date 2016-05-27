import requests
import websocket


class Connection(object):
    def __init__(self, email, password, ptr=False):
        self.email = email
        self.password = password
        self.url = 'https://screeps.com/api'
        self.url_wss = 'wss://screeps.com/socket/websocket'
        self.token = None
        if ptr:
            self.url = 'https://screeps.com/ptr/api'
            self.url_wss = 'wss://screeps.com/ptr/socket/websocket'

    # REST connection
    def signin(self):
        url = '{}/auth/signin'.format(self.url)
        data = dict(email=self.email, password=self.password)
        response = requests.post(url=url, data=data)
        response.raise_for_status()
        self.token = response.json()['token']

    def get_me(self):
        if not self.token:
            self.signin()
        url = '{}/auth/me'.format(self.url)
        headers = {'X-Token': self.token, 'X-Username': self.token}
        response = requests.get(url=url, headers=headers)
        return response.json()

    def console(self, command):
        if not self.token:
            self.signin()
        url = '{}/user/console'.format(self.url)
        headers = {'X-Token': self.token, 'X-Username': self.token}
        data = {'expression': command}
        response = requests.post(url=url, headers=headers, data=data)
        return response.json()

    def get_memory(self, path=''):
        if not self.token:
            self.signin()
        url = '{}/user/memory'.format(self.url)
        headers = {'X-Token': self.token, 'X-Username': self.token}
        data = {'path': path}
        response = requests.get(url=url, headers=headers, data=data)
        return response.json()

    # Websocket connection
    def on_message(self, ws, message):
        if (message.startswith('auth ok')):
            ws.send('subscribe user:' + self.user_id + '/console')
            return

        self.messageCallback(message)

    def on_error(self, ws, error):
        raise Exception(error)

    def on_close(self, ws):
        raise Exception("### closed ###")

    def on_open(self, ws):
        ws.send('auth {}'.format(self.token))

    def connect(self):
        ws = websocket.WebSocketApp(url=self.url_wss,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close,
                                    on_open=self.on_open)
        ws.run_forever(ping_interval=1)

    def startWebSocket(self, messageCallback):
        self.messageCallback = messageCallback
        self.signin()
        me = self.get_me()
        self.user_id = me['_id']
        self.connect()
