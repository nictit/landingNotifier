import threading
import flaskTG
import makeItTrack

def telegramAPI():
    flaskTG.mainn()

def altCheckLoop():
    makeItTrack.altCheckRnW()
    threading.Timer(20, altCheckLoop).start()

if __name__ == '__main__':
    t1 = threading.Thread(target=telegramAPI).start()
    t2 = threading.Timer(5, altCheckLoop).start()





