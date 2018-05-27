# UC02 - Transmissão Multimídia

### [Diagrama de caso de uso](Diagrama-transmitir-multimídia)

## Descrição
* O Usuário capturará dados e os enviará por streaming e esse conteúdo será transmitido no player da Twitch.

## Atores
* [Streamer](Streamer)

## Pré-condições
* O usuário deverá ter acesso à internet
* O usuário deverá ter um software de captura
* O usuário deverá ter os requisitos de hardware adequados para uma transmissão
* O usuário deverá possuir uma conta na twitch
* O usuário deverá estar logado na twitch
* O usuário deverá ter inserido sua token de streaming no software

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário abre o software de captura [FA01][FA02]
* 2. O usuário configura o ambiente de captura
* 3. A Chave de Transmissão é sincronizada
* 4. O usuário inicia a stream
* 5. A stream é transmitida no canal do usuário da Twitch
* 6. O caso de uso é encerrado


### Fluxos Alternativos
#### FA01 - O Usuário transmitirá através de um Console
* 1. O usuário aperta o botão de SHARE enquanto joga o jogo
* 2. O usuário seleciona o serviço da Twitch
* 3. O usuário retorna ao item 2 do fluxo principal

#### FA02 - O usuário utiliza o aplicativo mobile para transmitir
* 1. O usuário abre o aplicativo mobile
* 2. O usuário seleciona a opção de transmissão do aplicativo
* 3. O usuário retorna ao item 4 do fluxo principal


### Fluxo de Exceção

#### FE01 - Erro de sincronização da chave de transmissão
* 1. No 3o item do fluxo principal, se a chave estiver incorreta ou não existir, um erro ocorre a mensagem de erro é exibida.

## Pós-condição
* A transmissão está ocorrendo de forma adequada e os dados capturados estão sendo mostrados corretamente no canal do usuário.