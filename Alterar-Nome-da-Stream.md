# UC14 - Alterar Nome da [Stream](Stream)
### [Diagrama - Alterar Nome da Stream](Diagrama-Alterar-Nome-da-Stream)
## Descrição
* Este caso de uso descreve a alteração do título/nome de uma stream

## Atores
* [Streamer](Streamer)

## Pré-condições
* O usuário deve ter acesso à internet
* O usuário deve estar logado na twitch

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário abre seu painel de controle [FA01]
* 2. O usuário abre a aba de informações da transmissão
* 3. O usuário digita o novo Título da transmissão
* 4. O usuário confirma a alteração clicando em ```Atualizar Informações```
* 5. O caso de uso se encerra

### Fluxo Alternativo
* [FA01] - O usuário altera o nome da transmissão pela página do canal
    * 1. O usuário acessa a página de seu canal
    * 2. O usuário seleciona a opção ```Editar```, localizada abaixo do player da transmissão
    * 3. O usuário retorna ao item 3 do fluxo principal

## Pós-condição
* O nome da transmissão é alterado