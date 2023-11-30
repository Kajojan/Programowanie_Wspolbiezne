import sysv_ipc

klucz = 11
NULL_CHAR = '\0'
rounds =3
score=0

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




try:
    sem1 = sysv_ipc.Semaphore(klucz, sysv_ipc.IPC_CREX,0o700,1)
    sem2 = sysv_ipc.Semaphore(klucz+1, sysv_ipc.IPC_CREX,0o700,0)
    mem = sysv_ipc.SharedMemory(klucz, sysv_ipc.IPC_CREX)
    mem2 = sysv_ipc.SharedMemory(klucz+1, sysv_ipc.IPC_CREX)

    for i in range(0, rounds):
        sem1.acquire()
        chosen_position = input("Gracz 1: Wybierz pozycję wygrywającej karty (1, 2, 3): ")
        pisz(mem, chosen_position)
        sem2.release()

        sem1.acquire()
        liczba = czytaj(mem2)
        if(liczba == chosen_position):
            print(f" \n przegrana drugi gracz wybrał {liczba} \n")
            sem2.release()
        else:
            print(f" \n brawo wygrana, drugi gracz wybrał  {liczba} \n")
            score +=1 
            sem2.release()

    sem1.acquire()
    score2 = czytaj(mem2)
    if(int(score2) > score):
        wynik=f"Wygrał player2 wynikiem {score2} do {score}"
        pisz(mem, wynik)
        print(wynik)
    elif int(score2) == score:
        wynik=f"Remis player2- {score2} , player1 -  {score}"
        pisz(mem, wynik)
        print(wynik)
    else:
        wynik=f"Wygrał Player1  wynikiem {score} do {score2} "
        pisz(mem, wynik)
        print(wynik)
    sem2.release()


    sysv_ipc.remove_shared_memory(mem.id)
    sysv_ipc.remove_shared_memory(mem2.id)
    sysv_ipc.remove_semaphore(sem1.id)
    sysv_ipc.remove_semaphore(sem2.id)   

except:
    sem1 = sysv_ipc.Semaphore(klucz)
    sem2 = sysv_ipc.Semaphore(klucz+1)
    mem = sysv_ipc.SharedMemory(klucz)
    mem2 = sysv_ipc.SharedMemory(klucz+1)
    for i in range(0, rounds):
        print("Gracz 2 czeka na ruch Gracza 1.")

        sem2.acquire()
        chosen_position = input("Gracz 2: Wybierz pozycję karty (1, 2, 3): ")
        pisz(mem2,chosen_position)
        sem1.release()

        sem2.acquire()
        liczba = czytaj(mem)
        if(liczba != chosen_position):
            print(f" \n przegrana drugi gracz wybrał {liczba} \n")
            sem1.release()
        else:
            print(f"\n brawo wygrana, drugi gracz  wybrał  {liczba} \n")
            score +=1 
            sem1.release()

    
    pisz(mem2, str(score))
    sem1.release()
    sem2.acquire()
    score = czytaj(mem)
    print(score)
    
   

