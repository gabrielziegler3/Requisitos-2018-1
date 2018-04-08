|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|07/04/2018|1.0|Criação do Documento|Filipe Dias|
|08/04/2018|1.1|Revisão e Adição de Conteúdo|João Carlos|

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


## Cenário 003 - Viewer dando follow em uma stream

|Título|Objetivo|Contexto|Ator(es)|Recursos|Exceções|Episódios|
|---------|---------|--------|--------|--------|--------|---------|
|Seguir canal|Receber notificações de um canal|Dado que a pessoa esteja autenticada na twitch|Viewer|Dispositivo eletrônico com acesso à internet|Sem transmissão de imagem e Periféricos|Viewer gosta de uma stream específica|
|X|Ter o canal na home page da twitch|X|X|X|X,notificações indesejadas por default|X|
|X|Receber notificações de um canal|Dado que a pessoa não esteja autenticada na twitch|X|X, ter conta na twitch|Sem transmissão de imagem e Periféricos|X|
|X|X|X|X|X|X|V1: Efetuar login|
* Dispositivo eletrônico = Computador, celular ou similar
* Periféricos = Mouse, teclado, tela touch ou similar 
* Transmissão de imagem = Monitor ou similar
* X = Replica da célula acima
