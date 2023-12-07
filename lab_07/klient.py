import socket


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    player_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    player_socket.bind(("127.0.0.1", 0))

    player_port = player_socket.getsockname()[1]

    print(f"Twoj numer portu to: {player_port}")
    score = 0

    while True:
        choice = input("Wybierz (P - papier, K - kamień, N - nożyce, koniec - koniec ): ").upper()
        while choice.lower() not in ("p","n","k","koniec"):
            choice = input("Wybierz (P - papier, K - kamień, N - nożyce): ").upper()



        player_socket.sendto(
            f"{choice},{player_port}".encode(), (server_ip, server_port)
        )

        result, _ = player_socket.recvfrom(1024)
        print(result.decode())
        if result.decode() == "koniec":
            break
        score += int(result.decode())
        print(f"score : {score}")


if __name__ == "__main__":
    main()
