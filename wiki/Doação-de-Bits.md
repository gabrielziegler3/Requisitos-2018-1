# UC05 - Doação de Bits

### [Diagrama de caso de uso](Diagrama-doar-bits)

## Descrição
* Esse caso de uso descreve como doar bits.

## Atores
* Usuário

## Pré-condições
* O usuário deve possuir bits associados à sua conta
* O usuário deve estar assistindo uma transmissão ativa
* O usuário receptor deve ser parceiro twitch

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário está assistindo uma stream
* 2. O usuário deseja doar bits
* 3. O usuário seleciona a opção ```Cheer```[FA01][FE01]
* 4. O usuário seleciona a quantidade de bits que deseja doar
* 5. O usuário doa os bits selecionados
* 6. O caso se encerra

### Fluxos Alternativos
* [FA01] - O usuário não possui bits
    * 1. O usuário não possui bits
    * 2. O usuário realiza as etapas do fluxo principal da [UC06](Compra-de-Bits)
    * 3. O usuário retorna ao passo 4 do fluxo principal.

### Fluxo de Exceção
* [FE01] - O usuário não possui e não deseja comprar bits
    * 1. O usuário não possui bits
    * 2. O usuário não deseja comprar bits
    * 3. O usuário é incapaz de realizar um cheer
    * 4. O fluxo principal não pode ser completado]
    * 5. O fluxo de exceção se encerra

## Pós-condição
* Os bits do cheer são recebidos pelo destinatário