import threading
import flaskTG
import planesBackEnd

def telegramAPI():
    flaskTG.main()

def altCheckLoop():
    planesBackEnd.altCheck()
    threading.Timer(20, altCheckLoop).start()

if __name__ == '__main__':
    t1 = threading.Thread(target=telegramAPI).start()
    t2 = threading.Timer(5, altCheckLoop).start()





