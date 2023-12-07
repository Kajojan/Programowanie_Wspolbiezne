import sysv_ipc

klucz = 11
NULL_CHAR = "\0"


try:
    sem1 = sysv_ipc.Semaphore(klucz, sysv_ipc.IPC_CREX, 0o700, 0)
    sem2 = sysv_ipc.Semaphore(klucz + 1, sysv_ipc.IPC_CREX, 0o700, 1)
    mem = sysv_ipc.SharedMemory(klucz, sysv_ipc.IPC_CREX)
    mem2 = sysv_ipc.SharedMemory(klucz + 1, sysv_ipc.IPC_CREX)
    player = "player1"
except:
    sem1 = sysv_ipc.Semaphore(klucz)
    sem2 = sysv_ipc.Semaphore(klucz + 1)
    mem = sysv_ipc.SharedMemory(klucz)
    mem2 = sysv_ipc.SharedMemory(klucz + 1)
    player = "player2"


def pisz(mem, s):
    s += NULL_CHAR
    s = s.encode("utf-8")
    mem.write(s)


def czytaj(mem):
    s = mem.read()
    s = s.decode("utf-8")
    i = s.find(NULL_CHAR)
    if i != -1:
        s = s[:i]
    return s


print(player)

for i in range(0, 2):
    if player == "player1":
        sem2.acquire()
        chosen_position = input(
            "Gracz 1: Wybierz pozycję wygrywającej karty (1, 2, 3): "
        )
        pisz(mem2, "")
        sem1.release()
    else:
        print("Gracz 2 czeka na ruch Gracza 1.")

    sem2.acquire()
    if player == "player2":
        chosen_position = input("Gracz 2: Wybierz pozycję karty (1, 2, 3): ")
        pisz(mem2, chosen_position)
        sem1.release()
    else:
        liczba = czytaj(mem)
        if liczba == chosen_position:
            pisz(mem2, f"brawo wygrana, wybrałeś {liczba} i to była wybrana liczba")
            print(f"przegrana gracz2 wybrał {liczba}")
            sem1.release()

        else:
            pisz(mem2, f"przegrana, wybrana liczba była {chosen_position}")
            print(f"brawo wygrana, gracz2 wybrał  {liczba}")
            sem1.release()

    if player == "player2":
        sem2.acquire()
        s = czytaj(mem)
        print(f"odp: {s} end")
        sem1.release()


if player == "player1":
    sem2.acquire()
    sysv_ipc.remove_shared_memory(mem.id)
    sysv_ipc.remove_shared_memory(mem2.id)
    sysv_ipc.remove_semaphore(sem1.id)
    sysv_ipc.remove_semaphore(sem2.id)
