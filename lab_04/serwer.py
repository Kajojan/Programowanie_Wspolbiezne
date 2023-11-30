import os
import csv
import time
import errno
import signal


FIFO = 'kolejka_serwera'

try:
  os.mkfifo(FIFO)
except OSError as oe: 
  if oe.errno != errno.EEXIST:
    raise

fifo_in = os.open(FIFO, os.O_RDONLY)

def handle_sigusr1(signum, frame):
    exit(0)

signal.signal(signal.SIGHUP, signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, handle_sigusr1)

database = {}
with open('dane.csv', 'r') as file:
   csv_reader = csv.reader(file)
   for row in csv_reader:
     database[int(row[0])] = row[1]

while True:
  request = b''
  while True:
    r = os.read(fifo_in, 1)
    if r == b'\n':
      break
    request += r
  if request:
    request = request.decode().strip()
    print(request)
    try:
      id, client_queue = request.split(',')
 
      id = int(id) 
      if id in database:
        response = database[id]
      else:
         response = "Nie ma"

      fifo_out_client = os.open(client_queue, os.O_WRONLY)
      os.write(fifo_out_client, response.encode())
      os.close(fifo_out_client)

    except Exception as e:
      print("Wystąpił błąd podczas przetwarzania zapytania:", e)

  time.sleep(5)