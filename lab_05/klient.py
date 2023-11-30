import os
import sys
import sysv_ipc

def main():
    key1 = 12
    key2 = 34

    try:
        mq1 = sysv_ipc.MessageQueue(key1)
        mq2 = sysv_ipc.MessageQueue(key2)
        pid = os.getpid()
        print(pid)

        while True:
            try:
                word = input("Podaj słowo: ")
                if not word:
                    continue

                mq1.send(word.encode('utf-8'), type=pid)
                response, msg_type = mq2.receive(True, type=pid)

                result = response.decode('utf-8')
                print(f"Odpowiedź serwera: {result}")

            except sysv_ipc.ExistentialError:
                print("Błąd komunikacji z serwerem.")
                break  

    except KeyboardInterrupt:
        print("\nZamykanie klienta...")
        sys.exit(0)
    except Exception as e:
        print(f"Błąd klienta: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
