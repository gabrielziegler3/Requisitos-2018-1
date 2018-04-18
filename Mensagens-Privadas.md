# UC08 - Mensagens Privadas

## Descrição
* Esse caso de uso descreve como mandar mensagens privadas na Twitch

## Atores
* User

## Pré-condições
* O usuário deve ter acesso à internet
* 

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário seleciona a barra de pesquisa lateral
* 2. O usuário digita o nome do usuário a qual deseja enviar uma mensagem privada[FE01]
* 3. O usuário clica no nome do usuário encontrado desejado
* 4. Um mini chat é aberto na parte inferior da tela
* 5. O caso se encerra


### Fluxos Alternativos
#### FA01 - 


#### FA02 -


### Fluxo de Exceção

#### FE01 - O usuário digita um nome de usuário errado
* 1. O usuário digita o nome de usuário ao qual deseja conversar errado
* 2. Uma mensagem na tela dizendo ```Infelizmente, não encontramos ninguém chamado <nomeDeUsuárioErrado>```
* 3. O usuário volta para o passo 2 do fluxo principal
* 4. O caso se encerra

## Pós-condição
*