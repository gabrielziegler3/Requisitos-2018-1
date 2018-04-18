# UC06 - Compra de Bits

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
* 3. O usuário seleciona a quantidade de bits desejada [FA01]
* 4. O usuário finaliza a compra
* 5. O caso se encerra

### Fluxos Alternativos
#### FA01 - O usuário seleciona a forma de pagamento
* 1. Após selecionada a quantidade de bits, o usuário é direcionado à uma página para selecionar a forma de pagamento
* 2. O usuário escolhe entre ```Amazon``` ou ```PayPal```
* 3. O usuário volta para o passo 4 do fluxo principal

### Fluxo de Exceção
#### FE01 - O usuário não possui conta nas plataformas de pagamento
* 1. O usuário vai finalizar a compra
* 2. O usuário não possui uma conta em nenhuma plataforma de pagamento
* 3. O usuário cancela a compra
* 4. O usuário volta para o passo 1 do fluxo principal 

## Pós-condição
* O usuário passa a ter bits associados à sua conta