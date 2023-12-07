import os

FIFO_SERVER = "../kolejka_serwera"
FIFO_CLIENT = "kolejka_klienta"

# Utworzenie kolejki klienta
try:
    os.mkfifo(FIFO_CLIENT)
except OSError as oe:
    if oe.errno != 17:
        raise

query = "2," + "klient2/" + FIFO_CLIENT + "\n"

try:
    fifo_out = os.open(FIFO_SERVER, os.O_WRONLY)
    os.write(fifo_out, query.encode())
    os.close(fifo_out)
    print(query)

    try:
        fifo_in = os.open(FIFO_CLIENT, os.O_RDONLY)
        response = os.read(fifo_in, 256).decode().strip()
        os.close(fifo_in)
        print("Odpowiedź serwera:", response)

    except OSError as e:
        print("Błąd odczytu z kolejki klienta:", e)

except OSError as e:
    print("Błąd zapisu do kolejki serwera:", e)
