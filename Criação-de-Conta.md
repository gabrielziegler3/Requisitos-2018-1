# UC03 - Criação de Conta

### [Diagrama de caso de uso](Diagrama-criar-conta)

## Descrição
* Este caso de uso descreve como um ator externo pode [criar uma conta](Criar-Conta) na Twitch.

## Atores
* Ator externo

## Pré-condições
* O ator deve ter acesso à internet.
* O ator não deve estar logado em uma conta na twitch.

## Fluxo de Eventos
### Fluxo Principal
* 1. O ator acessa o site da Twitch 
* 2. O ator seleciona a opção ```Cadastrar-se``` 
* 3. O ator usuário preenche os campos necessários [FA01][FE01][FE02]
* 4. O sistema valida os dados do usuário
* 5. O ator é cadastrado
* 6. O caso de uso se encerra

### Fluxos Alternativos
#### FA01 - O usuário seleciona a opção ```Conectar-se com o Facebook```.
* 1. O ator seleciona a opção ```Cadastrar-se```.
* 2. O ator seleciona a opção ```Conectar-se com o Facebook```. 
* 3. O ator autoriza o uso do Facebook por parte da Twitch .
* 4. O ator retorna ao passo 5 do fluxo principal

### Fluxo de Exceção
#### FE01 - O futuro usuário não preenche os dados corretamente
* 1. O ator preenche os campos incorretamente
* 2. O ator clica em confirmar
* 3. Uma mensagem na tela avisa que o cadastro não foi efetivado
* 4. O caso de uso se encerra incompleto

#### FE02 - O futuro usuário deixa de preencher algum campo
* 1. O ator deixa de preencher algum campo
* 2. O ator clica em confirmar
* 3. Uma mensagem na tela avisa que o campo é necessário
* 4. O caso de uso se encerra incompleto

## Pós-condição
* O ator agora é um usuário, possuindo conta na twitch