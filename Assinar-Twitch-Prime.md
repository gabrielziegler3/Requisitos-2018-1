# UC13 - Assinar Twitch Prime

### [Diagrama de Caso de Uso](Diagrama-Assinar-Twitch-Prime)

## Descrição
* Este caso de uso descreve a assinatura no Twitch Prime.

## Atores
* Usuário
* Sistema

## Pré-condições
* O usuário deve ter acesso à internet
* O usuário deve estar logado no sistema
* O usuário não deve possuir uma assinatura ativa
* O caso de uso é iniciado na página principa da Twitch

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário clica em Twitch Prime.
* 2. O usuário faz login em sua conta da Amazon
* 3. O usuário preenche os dados da fatura [FE01]
* 4. O usuário seleciona ```Comece a assistir agora```
* 5. O usuário conecta sua conta da Twitch
* 6. O sistema sincroniza valida a conta Prime Vídeo
* 7. O sistema fornece o serviço twitch prime[FA01]
* 8. O caso de uso se encerra

### Fluxos Alternativos
#### [FA01] O usuário deseja fazer um teste de 7 diais
* 1. O usuário se direciona às opções do Prime Vídeo
* 2. O usuário vai até a parte de pagamento
* 3. O usuário cancela o pagamento
* 4. O usuário possui 7 dias gratuitos de avaliação da Twitch Prime e Prime Vídeo
* 5. O usuário retorna ao item 8 do fluxo principal

#### [FA02] O usuário Já possui o serviço Prime Vídeo e quer obter o Twitch Prime
* 1. O usuário se encontra no site da prime vídeo
* 2. O usuário vai até opções
* 3. O usuário seleciona a opção de vincular uma conta twitch
* 4. O usuário realiza os procedimentos de validação do vínculo
* 5. As contas agora estão sincronizadas
* 6. O usuário seleciona a opção de ativar gratuitamente o serviço Twitch Prime
* 7. O usuário agora é um usuário prime da Twitch
* 8. O caso de uso se encerra.
 
### Fluxo de Exceção
#### [FE01] O usuário não deseja preencher as informações de pagamento
* 1. O usuário está na página de pagamento
* 2. O usuário não quer utilizar seu cartão de crédito
* 3. O usuário desiste de obter o Twitch Prime
* 4. O caso de uso é encerrado incompleto

## Pós-condição
* O usuário agora possui uma conta Prime na Twitch e na Amazon Vídeo