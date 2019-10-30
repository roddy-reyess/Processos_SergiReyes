from datetime import datetime
import time
from multiprocessing import Process


def t(s):
    while (True):
        print(datetime.today())
        time.sleep(s)
def main():
    p = Process(target=t, args= (1,))
    p.start()
    for i in range(10):
        print(p.pid)
        time.sleep(0.5)
    p.terminate()
    print("fi")
main()
