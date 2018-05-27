# UC09 - Restrições de (Chat)[Group-Chat]
### [Diagrama de caso de uso](Diagrama-Restrições-de-Chat)

## Descrição
* Usuário aplica filtro de acesso ao (chat)[Group-Chat]

## Atores
* Usuário 


## Pré-condições
* O usuário deve ter capacidades administrativas no canal
* O usuário deve ter acesso a internet
* O usuário deve estar logado em sua conta

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário está no canal da transmissão. [FA02]
* 2. O usuário abre as configurações do chat da stream no canto inferior esquerdo do (chat)[Group-Chat]
* 3. O usuário seleciona a opção ```Chat Somente seguidores```[FA02]
* 4. O caso de uso é encerrado

### Fluxos Alternativos
#### FA01 - O usuário está no painel de controle da stream
* 1. O usuário está no painel de controle
* 2. O usuário retorna ao passo 2 do fluxo principal

#### FA02 - O usuário seleciona a opção Chat somente para inscritos
* 1. O usuário seleciona a opção de ```Chat somente para inscritos```.
* 2. O usuário retorna ao passo 4 do fluxo principal.

### Fluxo de Exceção
* Não se Aplica

## Pós-condição
* O chat agora possui restrições de acesso.