# UC20 - Hospedagem

* [Diagrama de Caso de Uso](Diagrama-Hospedagem)

## Descrição
* Este caso de uso descreve o sistema de hospedagem de stream em outros canais
 
## Atores
* Usuário - Streamers

## Pré-condições
* O usuário não deve ter uma stream ativa

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário acessa o painel de controle
* 2. O usuário se direciona à sub-secção de ```Host``` na secção ```Ao Vivo``` do painel
* 3. O usuário abre as configurações do serviço de hosting
* 4. O usuário ativa a opção de hospedagem automática [FA01]
* 5. O usuário seleciona os canais que ele gostaria de hospedar [FA02][FE01]
* 6. O usuário salva as alterações
* 7. O caso de uso é encerrado

### Fluxos Alternativos

#### FA01 - Hospedagem de Equipe
* 1. O usuário ativa a opção de hospedar canais da equipe do usuário (se esta existir), de forma aleatória, automaticamente.
* 2. O usuário retorna ao passo 6 do fluxo principal.

#### FA02 - O usuário seleciona a opção de hospedagem de canais semelhantes ao dele
* 1. O usuário ativa a opção de hospedar canais semelhantes ao dele.
* 2. O usuário retorna ao passo 6 do fluxo principal.

### Fluxo de Exceção
#### FE01 - O usuário não segue nenhum canal.
* Essa excessão ocorre pois o usuário não é seguidor de nenhum canal.
* 1. O sistema não exibe nenhum canal a ser hospedado pelo usuário.
* 2. O fluxo de excessão se encerra.
## Pós-condição
* O canal do usuário agora hospeda, automaticamente os canais selecionados ou associados automaticamente pela twitch