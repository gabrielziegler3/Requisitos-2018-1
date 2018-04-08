|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|07/04/2018|1.0|Criação do Documento|Filipe Dias|
|08/04/2018|1.1|Revisão e Adição de Conteúdo|João Carlos|
|08/04/2018|1.1|Revisão e Adição de Conteúdo|Filipe Dias|

## Cenário 001 - Viewer assistindo uma stream

|Título|Objetivo|Contexto|Ator(es)|Recursos|Exceções|Episódios|
|---------|---------|--------|--------|--------|--------|---------|
|Assistir uma stream|Descrever como conseguir assistir uma stream|Pessoa busca se entreter assistindo alguém jogar|Viewer, Streamer|Dispositivo eletrônico conectado à internet|Não há streamers streamando|Pessoa está a procura de algo para se entreter|
|X|X|Pessoa busca aprender a respeito de um jogo|X|X|O usuário não tem conexão com a internet|Pessoa está mexendo em alguma rede social|
|X|X|X|X|X|X|Pessoa encontra o link de um Streamer em atividade|
|X|X|X|X|X|X|Pessoa acede ao link|
|X|X|X|X|X|X|Pessoa assiste a stream|


## Cenário 002 - Viewer se cadastrando na Twitch

|Título|Objetivo|Contexto|Ator(es)|Recursos|Exceções|Episódios|
|---------|---------|---------|---------|---------|---------|---------|
|Cadastrar na Twitch|Descrever o processo de cadastro na plataforma|Pessoa deseja se tornar um membro da Twitch|Pessoa não cadastrada na plataforma|Dispositivo eletrônico conectado à internet|Dispositivo eletrônico não estar conectado à internet|A pessoa não cadastrada acessa o site da [Twitch.tv](https://www.twitch.tv)|
|X|X|X|X|Conta no Facebook|Não possuir conta no Facebook|A pessoa não cadastrada clica em Cadastre-se|
|X|X|X|X|X|X|v1: A pessoa preenche os dados requeridos e clica em Cadastrar-se|
|X|X|X|X|X|X|v2: A pessoa clica em Conectar-se com o Facebook|
|X|X|X|X|X|X|v2.1: A pessoa permite a Twitch a usar os dados do Facebook para realizar o cadastro|


## Cenário 003 - Viewer dando follow em um streamer

|Título|Objetivo|Contexto|Ator(es)|Recursos|Exceções|Episódios|
|---------|---------|--------|--------|--------|--------|------------|
|Seguir canal|Se inscrever em um canal para receber suas notificações|Dado que a pessoa esteja autenticada na Twitch|Viewer|Dispositivo eletrônico com acesso à internet|Viewer não estar conectado à internet|Viewer gosta de uma stream específica|
|X|Ter o canal na home page da Twitch.tv|X|Streamer|Ter conta na Twitch|Notificações indesejadas por default|Viewer efetua login|
|X|Saber quando um streamer estiver streamando|X|X|X|X|Viewer clica na stream|
|X|X|X|X|X|X|Viewer clica em ```❤️ Seguir```|
|X|X|X|X|X|X|Notificação na tela comprovando que ele está seguindo o streamer|

### Obs.: 
* O Cenário 004 - Viewer dando susbscribe em um canal possui todas as mesmas características que o Cenário 003, mudando apenas o último episódio em que o Viewer clica em ```Inscrever-se```
________________________

### Palavras chave 🔑:
* Dispositivo eletrônico = Computador, celular ou similar
* Periféricos = Mouse, teclado, tela touch ou similar 
* Transmissão de imagem = Monitor ou similar
* v1 = Primeira vertente do cenário (caminho 1)
* v2 = Segunda vertente do cenário (caminho 2) 
