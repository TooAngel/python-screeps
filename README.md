# Screeps library

Library to connect to the screeps API either via REST or websocket.
Example for using the library can be seen at
https://github.com/TooAngel/screeps-cli.


## Rest

 - `get_me()` Returns the user object for the logged in user
 - `console(command)` Sends the command to the console

## Websocket
Websocket connection for fetching the console log
```
from screeps.screeps import Connection

def sysout(message):
    print(message)

conn = Connection(email, password, arguments['--ptr'])
conn.startWebSocket(sysout)
```


## Deploy

`python setup.py sdist upload`
