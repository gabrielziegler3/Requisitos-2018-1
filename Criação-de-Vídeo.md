# UC19 - Criação de Vídeo

* [Diagrama de Caso de Uso](Diagrama-Criar-Video)

## Descrição
* Este caso de uso descreve como criar vídeos na plataforma.
## Atores
* Usuário

## Pré-condições
* O usuário deverá ter acesso a internet
* O usuário deverá ter um arquivo multimídia a ser subido para a plataforma
* O video não deve ferir as guidelines da twitch

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário seleciona o dropdown do usuário 
* 2. O usuário seleciona a opção de ```Estúdio de Vídeo```
* 3. O usuário clica na secção de upload
* 4. O usuário arrasta ou seleciona o vídeo na pasta [FE01]
* 5. O usuário clica em ```agende uma premiere```
* 6. O usuário preenche as informações solicitadas
* 7. O vídeo é criado na plataforma
* 8. O caso de uso é encerrado

### Fluxos Alternativos
* Não se aplica

### Fluxo de Exceção
#### FE01 - O usuário não possui o email verificado
* 1. O usuário realiza a etapa do item 4
* 2. O usuário recebe uma notificação de que não é possível subir o vídeo por não possuir email verificado
* 3. O caso de uso é encerrado

## Pós-condição
* O vídeo agora está disponível na plataforma