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
* 1. O usuário acessa o site.
* 2. Na barra de busca de usuário escreve o nome de desejo.**[FE01]**
* 3. Uma lista de usuário aparecerá na barra lateral

### Fluxo de Exceção

**[FE01] - Nenhum usuário é econtrado**
* 1. O usuário preenche o campo com um nome invalido ou inexistente, gerando uma mensagem de nenhum usuário encontrado.

## Pós-condição
* Uma solicitação de amizade ou adcionamento é enviada ao usuário selecionado.