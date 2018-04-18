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
* 1. Na barra de busca de usuário escreve o nome de desejo.
* 2. Uma lista de usuário aparecerá na barra lateral.**[FE01]** **[FE02]**
* 3. O usuário encontra o nome.
* 4. Usuário adiciona o amigo.
### Fluxo de Exceção

**[FE01] - Nenhum usuário é encontrado**
* 1. O usuário preenche o campo com um nome invalido ou inexistente, gerando uma mensagem de nenhum usuário encontrado.

**[FE02] - Usuário de desejo não é encontrado**
* 1. Usuário não consegue encontrar um nome correspondente ao digitado.

## Pós-condição
* Uma solicitação de amizade ou adcionamento é enviada ao usuário selecionado.