# UC03 - Criação de Conta

### [Diagrama de caso de uso](Diagrama-criar-conta)

## Descrição
* Este caso de uso descreve como uma pessoa pode [criar uma conta](Criar-Conta) na Twitch.

## Atores
* Pessoa não cadastrada na Twitch.

## Pré-condições
* O usuário deve ter acesso à internet.

## Fluxo de Eventos
### Fluxo Principal
* 1. O futuro usuário acessa o site da Twitch 
* 2. O futuro usuário seleciona a opção ```Cadastrar-se``` 
* 3. O futuro usuário preenche os campos necessários [FA01][FE01][FE02]
* 4. O futuro usuário é cadastrado
* 5. O caso de uso se encerra

### Fluxos Alternativos
#### FA01 - O usuário seleciona a opção ```Conectar-se com o Facebook```.
* 1. O futuro usuário acessa a Twitch.
* 2. O futuro usuário seleciona a opção ```Cadastrar-se```.
* 3. O futuro usuário seleciona a opção ```Conectar-se com o Facebook```. 
* 2. O futuro usuário autoriza o uso do Facebook por parte da Twitch .

### Fluxo de Exceção
#### FE01 - O futuro usuário não preenche os dados corretamente
* 1. O futuro usuário preenche os campos incorretamente
* 2. O futuro usuário clica em confirmar
* 3. Uma mensagem na tela avisa que o cadastro não foi efetivado

#### FE01 - O futuro usuário deixa de preencher algum campo
* 1. O futuro usuário deixa de preencher algum campo
* 2. O futuro usuário clica em confirmar
* 3. Uma mensagem na tela avisa que o campo é necessário


## Pós-condição
* Não se Aplica