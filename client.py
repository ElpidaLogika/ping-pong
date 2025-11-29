import pygame
import socket
import json
from threading import Thread

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ping-pong')

fps = pygame.time.Clock()

# підключення до сервера
def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(('localhost', 12345))
            id = int(client.recv(24).decode())
            buffer = ''
            game_state = {}
            return id, game_state, buffer, client
        except:
            pass

def receive():
    global buffer, game_state, game_over
    while not game_over:
        try:
            data = client.recv(1024).decode()
            buffer += data
            while "\n" in buffer:
                packet, buffer = buffer.split('/n', 1)
                if packet.strip():
                    game_state = json.loads(packet)
        except:
            game_state['winner'] = -1

    
id, game_state, buffer, client = connect_to_server()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.flip()
    fps.tick(60)

pygame.quit()
