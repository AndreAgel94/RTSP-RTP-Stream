# RTSP-RTP-Stream

autores:

.André Lannes Bernardes Agel 

.Samuel Fernandes Terra dos Reis

Uma implementaçao python da tarefa de programação do capítulo Redes Multimídia do livro do kurose: "Computer Networking: A Top-Down Approach". [programming assignment 7](http://media.pearsoncmg.com/aw/aw_kurose_network_3/labs/lab7/lab7.html)
 
A aplicação implementa um servidor de vídeo streaming e um cliente, comunicando-se usando o protocolo de transmissã em tempo real(RTSP) e o protocolo de transferência em tempo real(RTP)

![Demonstration](Streaming.gif)

## Usando

Clone o repositório $git clone https://github.com/AndreAgel94/RTSP-RTP-Stream

	Abra um terminal:
   		 python Server.py 1025

	Em um outro terminal:
   		 python ClientLauncher.py 127.0.0.1 1025 5008 video.mjpeg
       
# Funções

Botão SETUP:
* Envia a solicitação p/ configuração do servidor
* Insere o cabeçalho de transporte(especificando a porta do socket de dados RTP criado)
* RTP - Protocolo de Transporte em tempo real
* Escuta/lê a resposta do servidor
* Analisa o cabeçalho de sessão (da resposta) pra pegar a id da sessão RTSP
* Cria um socket datagrama para receber os dados RTP
* Coloca o timeout nesse socket de 0.5 segundos

Botão PLAY:
* Envia a solicitação para dar play no vídeo
* Insere o cabeçalho de sessão
* Usa a id da sessão (que foi retornada na fase de configuração)
* Não colocar o cabeçalho do transporte nesta requisição
* escuta a resposta do servidor

Botao PAUSE:
* Envia a solicitação para pausar o vídeo
* Insere o cabeçalho de sessão
* Usa a id da sessão (que foi retornada na fase de configuração)
* Não colocar o cabeçalho do transporte nesta requisição
* escuta a resposta do servidor

Botao TEARDOWN:
* Envia a solicitação para encerrar o vídeo
* Insere o cabeçalho de sessão
* Usa a id da sessão (que foi retornada na fase de configuração)
* Não colocar o cabeçalho do transporte nesta requisição
* escuta a resposta do servidor

