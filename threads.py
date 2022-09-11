import threading
import tlgAPI
import makeItTrack

def telegramAPI():
    tlgAPI.mainn()

def altCheckLoop():
    makeItTrack.altCheckRnW()
    threading.Timer(20, altCheckLoop).start()

if __name__ == '__main__':
    t1 = threading.Thread(target=telegramAPI).start()
    t2 = threading.Timer(5, altCheckLoop).start()





