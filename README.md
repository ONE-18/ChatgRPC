# Chat gRPC

Este proyecto implementa un sistema de chat utilizando gRPC (Google Remote Procedure Call) y Protocol Buffers. Permite que múltiples clientes envíen y reciban mensajes de chat a través de un servidor centralizado.

## Instalación

1. Clona este repositorio:

   git clone https://github.com/tu-usuario/chat-grpc.git

2. Instala las dependencias necesarias:

   pip install -r requirements.txt

## Uso

1. Inicia el servidor de chat:

   python chat_server.py

   El servidor comenzará a escuchar en el puerto 50051.

2. En una terminal separada, inicia el cliente de chat:

   python chat_client.py

   El cliente te pedirá que ingreses un nombre de usuario.

3. Puedes abrir múltiples instancias de `chat_client.py` para simular varios clientes conectados al chat.

4. Escribe tus mensajes de chat y presiona Enter para enviarlos. Verás los mensajes enviados por otros clientes en tu terminal.

5. Para salir del chat, presiona Ctrl+C.

## Cómo funciona

El servidor de chat (`chat_server.py`) define un servicio gRPC llamado `ChatServer` con dos métodos:

- `ChatStream`: Un flujo de mensajes de chat que envía los nuevos mensajes a los clientes conectados.
- `SendMessage`: Un método para que los clientes envíen nuevos mensajes al servidor.

El cliente de chat (`chat_client.py`) se conecta al servidor y utiliza estos métodos para enviar y recibir mensajes de chat.

Los mensajes de chat se definen en el archivo `chat.proto` utilizando Protocol Buffers.
