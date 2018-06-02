# UC06 - Compra de Bits

### [Diagrama de caso de uso](Diagrama-comprar-bits)

## Descrição
* Esse caso de uso descreve como comprar Bits.
 
## Atores
* Usuário

## Pré-condições
* O usuário deve ter acesso à internet
* O usuário deve estar logado

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário abre uma stream desejada
* 2. O usuário seleciona a opção ```Adquira Bits``` na parte superior da tela
* 3. O usuário seleciona a quantidade de bits desejada
* 4. O usuário é seleciona a forma de pagamento [FE01]
* 5. O usuário preenche as informações de pagamento
* 6. O usuário finaliza a compra
* 7. O caso se encerra

### Fluxos Alternativos
* Não se Aplica

### Fluxo de Exceção
#### FE01 - O usuário não possui conta nas plataformas de pagamento
* 1. O usuário seleciona a forma de pagamento
* 2. O usuário não possui conta na plataforma de pagamento selecionada
* 3. O usuário não consegue completar a conta
* 4. O caso de uso é encerrado incompleto 

## Pós-condição
* O usuário possui a quantidade de bits adquirida