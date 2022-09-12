import threading
import Flsk
import planesBackEnd

def telegramAPI():
    Flsk.main()

def altCheckLoop():
    planesBackEnd.altCheck()
    threading.Timer(20, altCheckLoop).start()

if __name__ == '__main__':
    t1 = threading.Thread(target=telegramAPI).start()
    t2 = threading.Timer(5, altCheckLoop).start()





