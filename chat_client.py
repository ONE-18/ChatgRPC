import grpc
import chat_pb2
import chat_pb2_grpc
import threading

class Client:
    def __init__(self):
        # Crea un canal de comunicación con el servidor
        channel = grpc.insecure_channel('localhost:50051')
        self.connection = chat_pb2_grpc.ChatServerStub(channel)

        # Crea un canal de comunicación con el servidor
        self.user = input("Ingresa tu nombre de usuario: ")

        # Inicia un hilo para escuchar los mensajes del servidor
        threading.Thread(target=self.listen_for_messages, daemon=True).start()
        
        print(f"{self.user}: ", end='')

    # Método para recibir los mensajes del servidor
    def listen_for_messages(self):
        req = chat_pb2.Nada()
        for message in self.connection.ChatStream(req):
            if message.username != self.user:
                print(f"{message.username}-> {message.message}\n{self.user}: ", end='')

    # Método para enviar mensajes al servidor
    def send_messages(self):
        while True:
            message = input()
            message = chat_pb2.ChatMessage(username=self.user, message=message)
            self.connection.SendMessage(message)
            print(f"{self.user}: ", end='')


if __name__ == '__main__':
    try:
        c = Client()
        c.send_messages()
    except KeyboardInterrupt:
        print('Chat finalizado.')