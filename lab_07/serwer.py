import socket
import sys


def play_round(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 0
    elif (
        (player1_choice == "P" and player2_choice == "K")
        or (player1_choice == "K" and player2_choice == "N")
        or (player1_choice == "N" and player2_choice == "P")
    ):
        return 0
    else:
        return 1


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    players = {}

    while True:
        data, client_address = server_socket.recvfrom(1024)
        player_choice, player_port = data.decode().split(",")

        if player_port not in players:
            players[player_port] = {
                "choice": player_choice,
                "address": client_address,
                "score": 0,
            }
        else:
            players[player_port]["choice"] = player_choice

        if player_choice.lower() == "koniec":
                for player_data in players.values():
                    print(player_data["address"])
                    server_socket.sendto("koniec".encode(), player_data["address"])
                players.clear()
        else:
            for player in players:
                if player != player_port and players[player]["choice"] is not None:

                    result = play_round(players[player]["choice"], player_choice)
                    result2 = play_round(player_choice, players[player]["choice"])

                    players[player]["score"] += result2
                    players[player_port]["score"] += result

                    players[player]["choice"] = None
                    players[player_port]["choice"] = None


                    print(
                        f"{player} - {players[player]['score']} \n {player_port} - {players[player_port]['score']}"
                    )

                    server_socket.sendto(str(result).encode(), client_address)
                    server_socket.sendto(
                        str(result2).encode(), players[player]["address"]
                    )




if __name__ == "__main__":
    main()
