import threading

import tlgAPI

def dele():
    print('hello')
    threading.Timer(1.0, dele).start()

t1 = threading.Thread(target=dele)
tlg = threading.Thread(target=tlgAPI.app)

t1.start()
tlg.start()


