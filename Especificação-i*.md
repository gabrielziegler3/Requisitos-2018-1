|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|15/05/2018|1.0|Criação do Documento |Thiago Ferreira|
|15/05/2018|1.1|Adição dos atores e do tópico explicando o documento |Thiago Ferreira|
|15/05/2018|1.2|Adição do documento completo e formatação do mesmo|Thiago Ferreira|
|09/06/2018|1.3|Revisão|Gabriel Ziegler|

## O Documento

Este artefato conta com a especificação textual dos goals, hardgoals, tasks e softgoals levantados de forma prévia à criação dos diagramas utilizando o framework iStar. O documento foi elabora por toda a equipe, de forma incremental, de modo que, a elaboração dos diagramas fosse facilitada e possuísse maior qualidade. Este documento não é diretamente requisitado pela metodologia, entretanto, por ter sido um artefato produzido pela equipe, estará aqui armazenado. O conteúdo aqui localizado não corresponde ao conteúdo final que foi implementado nos diagramas

## Especificação Textual i*

### Atores

* Agente Usuário
    - Papel [Viewer](Viewer)
    - Papel [Streamer](Streamer)
* Agente Patrocinador
    - Posição Patrocinador Twitch
    - Posição Patrocinador [Streamer](Streamer)
* Agente Plataforma Twitch
    - Desenvolvimento
    - Financeiro
    - Marketing

### Relações

* [Viewer](Viewer) e [Streamer](Streamer)
* Patrocinador e [Streamer](Streamer)
* Patrocinador e [Viewer](Viewer)
* Patrocinador e Twitch
* Twitch e Usuário
* Twitch e [Streamer](Streamer)

### Hardgoals, Tasks, Softgoals e Resources

#### Hardgoals [Viewer](Viewer) e [Streamer](Streamer)

* Stream seja visualizada
    - Buscar stream
    - Selecionar [Stream](Stream)
* Doar Bits
    - Seja possível enviar bits ao longo de uma stream
    - [Condição] O [Streamer](Streamer) precisa ser parceiro da Twitcht
* Ocorra Comunicação entre as partes
    - Seja possível enviar mensagens privadas
    - Seja possível se comunicar através de mensagens de doação
    - Seja possível se comunicar através do chat do canal
* Acompanhar canal
    - Seguir Canal
    - Se inscrever em canal

#### Hardgoals Patrocinador e [Streamer](Streamer)

* [Streamer](Streamer) Seja Patrocinado
   - O patrocinado receba exclusividades
   - O patrocinado receba divulgação
   - Patrocinador seja divulgado
   - O produto do patrocinador seja divulgado
   - Os serviços do patrocinador sejam divulgados
* Stream seja monetizada pela publicidade
* [Recurso]Capital

#### Hardgoals Patrocinador e [Viewer](Viewer)

* Anúncios sejam transmitidos nas transmissões
    - Espectador assiste anúncios e transmissor recebe com a audiência nos anúncios

#### Hardgoals Patrocinador e Twitch

* Stream seja monetizada com publicidade
    - Inserir publicidade em stream de parceiro
    - [Recurso] Visualizações na stream
    - Receber capital por publicar anúncios
    - [Recurso]Capital

#### Hardgoals Twitch e [Viewer](Viewer)

* Usuário seja cadastrado
* Dashboard seja disponibilizado
    - Ter acesso a lives
    - Poder instalar extensão
    - Adicionar evento
        - Fazer upload de imagem
        - Inserir dados do evento
        - Validar dados
* Subscriptions sejam visualizadas
       - Ter acesso as subscriptions
       - Listar subscriptions
* Pagamentos sejam disponibilizados
    - Adicionar forma de pagamento
    - Visualizar histórico de pagamento
* Pesquisa seja realizada
    - Pesquisar por Jogos
    - Pesquisar por Comunidades
    - Pesquisar por Comunidades criativas
    - Pesquisar por canais
    - Ordenar pesquisa por relevância
    - Ordenar pesquisa por popularidade

#### Hardgoals Twitch e Usuário

* Conta na Twitch seja gerenciada
    - Cadastrar nova conta
        - Inserir dados válidos
    - Atualizar dados da conta
    - Desativar conta

* Login seja efetuado
    - Inserir dados válidos

* Twitch prime seja ativado
    - Pagamento

* Bits sejam obtidos
    - Seja possível comprar um determinado número de bits

#### Hardgoals Twitch -- [Streamer](Streamer)

* [Streamer](Streamer) seja efetuado como Twitch Partner
    - O usuário seja regular, transmitindo ao menos 3x por semana
    - O usuário aplicante tenha um Público e chat crescente
    - Conteúdo transmitido seja adequado às regras de conduta, Termos de serviço e Diretrizes DMCA da Twitch
* Plataforma supra as necessidades de [streaming](Streaming)
    - A twitch consiga transmitir conteúdo multimídia em tempo real
    - A twitch disponibilize um meio de interação para o [streamer](Streamer)
    - A twitch disponibilize alguma forma de monetização para o [streamer](Streamer)
    - A twitch disponibilize controle sobre a transmissão para o usuário, em tempo real

### Strategic Rationale

#### Usúario[Geral]

* Cadastro seja realizado
    - Inserir Dados[Dados gerais]
* Perfil seja acessado
    - Acessar configurações
    - Sair das configurações
* Dados seja atualizados[Dados do usuário]
    - Atualizar dados
    - Atualizar foto do perfil
    - Atualizar faixa do perfil
    - Atualizar denifinições do perfil
    - Cancelar conta

#### [Streamer](Streamer)

* Stream seja inicializada
    - Iniciar uma stream
* Stream key seja adquirida
    - Usuário [Streamer](Streamer) possua conta ativa na twitch
    - Stream key seja inicializada em software de captura
    - Usuário possua software de captura ou qualquer outro método de upload para a twitch em seu dispositivo o qual será realizada a captura

#### [Viewer](Viewer)

* [Viewer](Viewer) participe ativamente da stream
   - [Viewer](Viewer) participe do (chat)[Group-Chat]

#### Twitch

* Seja capaz de hospedar stream
    - Hospedar stream
    - Transmitir multimídia ao vivo
* Criar coleções de stream por um tempo limitado
* Seja capaz enviar notificações em tempo real para usuários
    - Enviar notificações aos usuários
    - Enviar solicitações de amizade
* Enviar sussurros
    - Enviar notificações de mensagens
    - Enviar notificações de publicações
* Seja capaz de estabelecer comunicação entre usuários
    - Estabelecer comunicação entre usuários
* Criar um chat de voz
    - Enviar mensagens
* Possuir capacidade de até 10 milhões de acessos simultâneos [Softgoal]
* [SoftGoal]Lidar com grande número de requisicoes
* [SoftGoal]Ter segurança

* Serviço de Add-ons seja disponibilizado
    - Seja possível adicionar add-ons à plataforma
    - Seja possível remover add-ons da plataforma
    - Seja possível baixar add-ons da plataforma
    - Seja possível instalar add-ons diretamente pela plataforma
    - Seja possível filtrar add-ons mostrados pela plataforma
    - Seja possível sincronizar add-ons automaticamente pela plataforma

* Serviço de Chat de Voz seja disponibilizado
    - Seja possível iniciar uma sala de chamada
    - Seja possível criar um servidor de chamada
    - Seja possível alterar a chamada de voz para vídeo chamada
    - Seja possível convidar pessoas para a chamada
    - Seja possível expulsar pessoas da chamada
    - [Softgoal] Chamadas de qualidade
