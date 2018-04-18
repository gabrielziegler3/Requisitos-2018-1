# UC07 - Geração de Token de Streamer

## Descrição
* Este caso de uso descreve o processo de gerar um token ao Streamer.

## Atores
* Streamer

## Pré-condições
* O streamer deve ter acesso à internet
* O streamer deve estar logado na Twitch

## Fluxo de Eventos
### Fluxo Principal
* 1. O streamer acessa o site da Twitch 
* 2. O streamer seleciona a sessão ```Painel de Controle```
* 3. Na seção ```Integridade da transmissão``` o streamer seleciona a opção ```Saiba como realizar um teste de transmissão```
* 4. O streamer seleciona a opção ```Pegue a sua chave de transmissão no Painel de controle do Twitch.```
* 5. O streamer clica em ```Mostrar chave``` e concorda com os termos [FE01]
* 6. O streamer visualiza sua Chave de Transmissão
* 7. O caso se encerra

### Fluxos Alternativos
* Não se aplica

### Fluxo de Exceção
#### FE01 - O streamer não concorda com os termos
* 1. O streamer faz todo o fluxo até o passo 5
* 2. O streamer não concorda com os termos
* 3. O streamer não visualiza a Chave de Transmissão
* 4. O streamer retorna ao passo 5 dos fluxo principal

## Pós-condição
* Não se aplica