# UC01 - Visualização de Stream

## Descrição
* Este caso de uso descreve a visualização de conteúdo multimídia ao vivo.

## Atores
* Streamer
* Telespectador

## Pré-condições
* O usuário deve ter acesso à internet
* O canal selecionado para visualização da transmissão deverá estar online ou hospendando alguma stream.

## Fluxo de Eventos
### Fluxo Principal
* 1. O Usuário acessa o site da Twitch [FA01][FA02]
* 2. O Usuário seleciona um jogo que gostaria de assistir[FA03][FA04][FA05]
* 3. O Usuário seleciona algum canal disponível
* 4. O Usuário assiste a stream
* 5. O caso de uso se encerra

### Fluxos Alternativos
#### FA01 - O Usuário acessa a plataforma Desktop da Twitch.
* 1. O Usuário abre a plataforma desktop.
* 2. O Usuário seleciona Secção de Streams da plataforma.
* 3. O usuário retorna ao passo 2 do fluxo principal.

#### FA02 - O Usuário abre a plataforma com o aplicativo mobile.
* 1. O Usuário abre o aplicativo.
* 2. O Usuário retorna ao passo 2 do fluxo principal.

### FA03 - O Usuário procura a stream através da barra de busca.
* 1. O Usuário procura o jogo através da barra de buscas.
* 2. O Usuário retorna ao passo 4 do fluxo principal.

### FA04 - O Usuário seleciona uma stream dos canais em destaque.
* 1. O Usuário escolhe uma stream dos streamers em destaque.
* 2. O Usuário retorna ao passo 4.

### FA05 - O Usuário escolhe uma stream, dos canais que ele segue
* 1. O Usuário escolhe uma stream dos canais seguidos.
* 2. O Usuário retorna ao passo 4.

### Fluxo de Exceção

[FE01] - O Player da Stream apresenta um erro
* 1. O Usuário está assistindo a uma stream
* 2. O player da stream apresenta um erro
* 3. O Usuário refresca a página ou sai da stream
* 4. O Usuário retorna ao passo 5 do fluxo principal

## Pós-condição
* Não se Aplica