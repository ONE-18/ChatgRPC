import grpc
from concurrent import futures
import chat_pb2
import chat_pb2_grpc

class ChatService(chat_pb2_grpc.ChatServerServicer):
    def __init__(self):
        # Lista para almacenar los mensajes de chat
        self.mensajes = []
        
    # Método para retransmitir los mensajes de recibidos a todos los clientes
    def ChatStream(self, request_iterator, context):
        lastindex = 0
        while True:
            # Envía los nuevos mensajes a los clientes
            while len(self.mensajes) > lastindex:
                n = self.mensajes[lastindex]
                lastindex += 1
                if n.message.strip() != "":
                    yield chat_pb2.ChatMessage(username=n.username, message=n.message)
    
    # Método para recibir y almacenar los mensajes de los clientes 
    # Es el método que se llama cuando un cliente envía un mensaje
    def SendMessage(self, request, context):
        # print(f"Nombre de usuario recibido: {request.username}")
        print(f"[{request.username}] {request.message}")
        self.mensajes.append(request)
        return chat_pb2.Nada()

if __name__ == '__main__':
    try:
        # Crea el servidor gRPC
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        chat_pb2_grpc.add_ChatServerServicer_to_server(ChatService(), server)
        print('Servidor de chat iniciado. Escuchando en puerto 50051...')
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
        print('Servidor detenido.')