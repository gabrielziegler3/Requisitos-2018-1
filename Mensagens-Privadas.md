# UC08 - Mensagens Privadas

## Descrição
* Esse caso de uso descreve como mandar mensagens privadas na Twitch

## Atores
* Usuário

## Pré-condições
* O usuário deverá ter acesso à internet
* O usuário deverá estar logado em sua conta twitch

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário seleciona a barra de pesquisa lateral [FA01][FA02]
* 2. O usuário digita o nome do usuário a qual deseja enviar uma mensagem privada[FE01]
* 3. O usuário clica no nome do usuário encontrado desejado
* 4. Um mini chat é aberto na parte inferior da tela
* 5. O usuário envia a mensagem para o usuário desejado
* 6. O caso se encerra



### Fluxos Alternativos
#### FA01 - O usuário vai para a secção de amigos em seu dropdown
* 1. O usuário seleciona a secção de amigos no dropdown de seu perfil
* 2. O sistema redireciona o usuário para a página de amigos
* 3. O usuário seleciona a opção de enviar mensagem privada na box do amigo escolhido
* 4. O usuário retorna ao item 4 do fluxo principal

#### FA02 - O usuario seleciona o amigo pra mandar mensagem na barra lateral
* 1. O usuário seleciona o amigo que gostaria de enviar mensagem na barra lateral do site[FA01]
* 2. O usuário retorna ao item 4 do fluxo principal



### Fluxo de Exceção

#### FE01 - O usuário digita um nome de usuário errado
* 1. O usuário digita o nome de usuário ao qual deseja conversar errado
* 2. Uma mensagem na tela dizendo ```Infelizmente, não encontramos ninguém chamado <nomeDeUsuárioErrado>```
* 3. O usuário volta para o passo 2 do fluxo principal
* 4. O caso de uso se encerra

### FE02 -  O usuário é bloqueado durante a conversa
* 1. O usuário encontra-se no item 5 do fluxo principal
* 2. O usuário destinatário bloqueia o usuário remetente
* 3. O usuário não pode mais enviar mensagens.
* 4. O fluxo de exceção é encerrado

## Pós-condição
* O usuário envia uma mensagem privada e o outro usuário recebe