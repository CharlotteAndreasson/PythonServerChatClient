import threading
import queue
import time


def main():
    send_queue = queue.Queue()

    def consumer():
        for _ in range(10):
            value = send_queue.get()
            print(value)
            send_queue.task_done()


    def producer():
        for i in range(10):
            send_queue.put(i)
            #time.sleep(2)

    # Skapar tråd 1, lägger in argument för thread_func efter args
    # Kommat visar att det är en tuple
    pt1 = threading.Thread(target=consumer)
    pt1.start()

    pt2 = threading.Thread(target=producer)
    pt2.start()

    send_queue.join()
    print("All done")
    #pt1.join()
    #pt2.join()



if __name__ == '__main__':
    main()
