import os

FIFO_CLIENT = './klient1/kolejka_klienta'

# Usunięcie kolejki klienta
try:
    os.remove(FIFO_CLIENT)
except OSError as oe:
    print("Błąd podczas usuwania pliku FIFO klienta:", oe)
