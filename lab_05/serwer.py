import sys
import sysv_ipc
import time


def translate_word(word):
    dictionary = {
        "hello": "cześć",
        "data": "dane",
        "run": "biegać",
    }
    return dictionary.get(word, "Nie ma")


def main():
    key1 = 12
    key2 = 34

    try:
        mq1 = sysv_ipc.MessageQueue(key1, sysv_ipc.IPC_CREAT)
        mq2 = sysv_ipc.MessageQueue(key2, sysv_ipc.IPC_CREAT)
        while True:
            try:
                request, msg_type = mq1.receive(type=0)
                pid = int(msg_type)
                word = request.decode("utf-8")
                print(f"{pid}: {word}")
                time.sleep(5)
                response = translate_word(word)
                mq2.send(response.encode("utf-8"), True, type=pid)
            except sysv_ipc.ExistentialError:
                break

    except Exception as e:
        print(f"Błąd serwera: {e}")
    finally:
        print("Zamykanie serwera...")
        sys.exit(0)


if __name__ == "__main__":
    main()
