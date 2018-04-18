# UC04 - Inscrição em Canal

## Descrição
* Este caso de uso descreve a inscrição em um canal por parte de um usuário.

## Atores
* Usuário

## Pré-condições
* O usuário deve ter acesso à internet
* O canal que está sendo inscrito deverá ser parceiro twitch
* O usuário deverá estar logado

## Fluxo de Eventos
### Fluxo Principal
#### Este fluxo é iniciado quando o usuário já se encontra em um canal
* 1. O usuário clica no botão "Increver-se"
* 2. O usuário seleciona a opção "Inscrever-se agora" [FA-01]
* 3. O sistema redireciona o usuário para uma tela que fornece a ele as opções de planos de inscrição
* 4. O usuário seleciona o plano desejado
* 5. O usuário seleciona a forma de pagamento
* 6. O sistema fornece um formulário para prenchimento das informações de pagamento
* 7. O usuário prenche as informações de pagamento
* 8. O usuário confirma a inscrição
* 9. O caso de uso é encerrado


### Fluxos Alternativos
#### FA01 - O usuário utiliza o serviço da Twitch Prime para de inscrever
* 1. O usuário seleciona a opção Inscrever-se utilizando Twitch Prime
* 2. O usuário retorna ao passo 8 do fluxo principal


### Fluxo de Exceção

#### FE01 - Ocorreu um erro no pagamento
* 1. O usuário preencheu as informações de pagamento
* 2. Algum errou aconteceu no processo
* 3. O caso de uso se encerra incompleto.

## Pós-condição
* O usuário agora está inscrito no canal.