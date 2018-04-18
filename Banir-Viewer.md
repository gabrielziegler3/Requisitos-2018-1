# UC16 - Banir Viewer

## Descrição
* Esse caso de uso descreve o processo de banimento de um Viewer.

## Atores
* Streamer
* Viewer

## Pré-condições
* O usuário deverá ter acesso à internet
* O streamer deverá estar streamando 

## Fluxo de Eventos
### Fluxo Principal
* 1. O streamer abre o stream
* 2. O streamer localiza no seu chat, um viewer indesejado [FE01]
* 3. O streamer clica no nome do viewer
* 4. O streamer seleciona 🕒 
* 5. O streamer bane o viewer do seu chat pelo tempo desejado


### Fluxos Alternativos
*

### Fluxo de Exceção

#### FE01 - Falha na localização do viewer
* 1. O chat ao vivo estará passando muitas mensagens, e não será possível localizar o viewer.

## Pós-condição
* O viewer que foi banido não poderá mais participar do chat do streamer que o baniu.