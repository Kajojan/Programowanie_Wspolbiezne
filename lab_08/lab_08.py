import threading
import numpy as np

sum = 0

def sum_list(list, start, end, lock):
  global sum

  for i in range(start, end + 1):
    with lock:
        sum += list[i]

def calculate_sum(list, num_threads):


  lock = threading.Lock()
  chunks = np.array_split(list, num_threads)

  threads = []
  for chunk in chunks:
    thread = threading.Thread(target=sum_list, args=(chunk, 0, len(chunk) - 1, lock))
    threads.append(thread)

  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()

  print("Suma:", sum)


num_threads = int(input("wątków: "))

list = np.arange(1000000)
calculate_sum(list, num_threads)
