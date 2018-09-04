# UC17 - Adição de Amigo

## Descrição
* Este caso de uso descreve o adicionamento de usuários como amigos.

## Atores
* Usuário

## Pré-condições
* O usuário deve ter acesso à internet
* O usuário deve estar logado

## Fluxo de Eventos
### Fluxo Principal
* Este fluxo se inicia na página principal da Twitch.
* 1. O usuário escreve na barra de busca o nome de desejo.
* 2. O sistema gera uma lista de usuários**[FE01]** **[FE02]**
* 3. O usuário encontra o nome.
* 4. O Usuário adiciona o amigo.
* 5. O caso de uso é encerrado
### Fluxo de Exceção

**[FE01] - Nenhum usuário é encontrado**
* 1. O usuário preenche o campo com um nome invalido ou inexistente
* 2. O sistema gera uma mensagem de nenhum usuário encontrado.
* 3. O caso de uso se encerra incompleto

**[FE02] - Usuário de desejo não é encontrado**
* 1. Usuário não consegue encontrar um nome correspondente ao digitado.
* 3. O caso de uso se encerra incompleto
## Pós-condição
* Uma solicitação de amizade ou adcionamento é enviada ao usuário selecionado.