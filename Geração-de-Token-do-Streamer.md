# UC07 - Geração de Chave de Transmissão

### [Diagrama de Caso de uso](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Diagrama-Gera%C3%A7%C3%A3o-de-Token-do-Streamer)

## Descrição
* Este caso de uso descreve o processo de gerar a chave de transmissão para o usuário.

## Atores
* Usuário

## Pré-condições
* O usuário deve ter acesso à internet
* O usuário deve estar logado na Twitch

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário acessa o site da Twitch 
* 2. O usuário seleciona a sessão ```Painel de Controle``` no dropdown do usuário
* 3. O usuário vai até a secção de configurações e seleciona ```preferencias de stream``` [FA01]
* 4. O usuário clica em chave de transmissão
* 5. O sistema envia uma mensagem de aviso e confirmação
* 6. O usuário concorda com os termos [FE01]
* 7. O caso se encerra



### Fluxos Alternativos
#### FA01 - O usuário acessa a chave de treanmissão através do teste de integridade da transmissão
* 1. Na seção ```Integridade da transmissão``` o streamer seleciona a opção ```Saiba como realizar um teste de transmissão```
* 2. O usuário seleciona a opção ```Pegue a sua chave de transmissão no Painel de controle do Twitch.```
* 3. O usuário retorna ao item 4 do fluxo principal.

### Fluxo de Exceção
#### FE01 - O streamer não concorda com os termos
* 1. O streamer faz todo o fluxo até o passo 5
* 2. O streamer não concorda com os termos
* 3. O streamer não visualiza a Chave de Transmissão
* 4. O caso de uso se encerra

## Pós-condição
* O usuário agora possui a chave de transmissão