|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|05/06/2018|1.0|Criação do Documento|Amanda Pires|
|05/06/2018|1.1|Edição do Documento|Filipe Dias|
|05/06/2018|1.2|Adição de conteúdo ao Documento|Filipe Dias, João Carlos, Gustavo Carvalho, Amanda Pires, Thiago Ferreira, Gabriel Ziegler|
|06/06/2018|1.3|Adição de conteúdo na tabela Backward From|Filipe Dias, João Carlos, Gustavo Carvalho, Amanda Pires, Thiago Ferreira, Gabriel Ziegler|
|10/06/2018|1.4|Adição de conteúdo na tabela Forward From|Gabriel Ziegler|

# Pós rastreabilidade

## Matriz de Rastreabilidade - Forward From

|Requisito|Descrição|NFR|I*|Artefato de Desenho|
|---------|------|------|-------|------|
|RF1|Cadastrar usuário|-|[SR Visitante](Strategic-Rationale#visitante)|-|
|RNF2|Logar via Facebook|-|[SR Visitante](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#visitante)|-|
|RF3|Editar perfil|-|[SR Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#usu%C3%A1rio)|-|
|RF4|Desabilitar conta|-|[SR Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#usu%C3%A1rio)|-|
|RF5|Tornar-se Twitch Prime|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|-|
|RF6|Tornar-se parceiro [Twitch](Twitch)|-|-|-|
|RF7|Compartilhar uma [Stream](Stream)|-|-|-|
|RF8|Seguir um [Streamer](Streamer)|-|[SD Viewer - Streamer](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#viewer---streamer-22)|-|
|RF9|Acessar os chats|-|-|-|
|RF10|Filtrar quem digita no chat|-|-|-|
|RF11|Banir alguém do chat|-|-|-|
|RF12|Alterar conteúdo da [Stream](Stream)|-|-|-|
|RF13|Visualizar chat de [Stream](Stream)|-|-|-|
|RF14|Subir um vídeo na [Twitch](Twitch)|-|-|-|
|RF15|Deletar um vídeo|-|-|-|
|RF16|Programar uma premiere|-|-|-|
|RF17|Gravar uma transmissão|-|-|-|
|RF18|Destacar um vídeo|-|-|-|
|RF19|Buscar outros usuários|-|[SR Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#usu%C3%A1rio)|-|
|RF20|Adicionar outro usuário como amigo|-|[SR Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#usu%C3%A1rio)|-|
|RF21|Mandar mensagens privadas|-|-|-|
|RF22|Participar de chats|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF23|Mandar emoticons|-|-|-|
|RF24|Bloquear alguém em uma conversa|-|-|-|
|RF25|Sincronizar add-ons|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF26|Filtrar os add-ons vistos|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF27|Instalar novos add-ons|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF28|Deletar add-ons|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF29|Disponibilizar novos add-ons|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF30|Atualizar os add-ons de forma automatizada|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF31|Criar uma nova chamada de voz|-|-|-|
|RF32|Filtrar usuários que entrarem na chamada|-|-|-|
|RF33|Realizar uma vídeo conferência|-|-|-|
|RF34|Usar uma video conferência em um servidor|-|-|-|
|RF35|Criar um grupo para chamadas permanentes|-|-|-|
|RNF36|Opções de planos de inscrições|-||-|
|RF37|Inscrever-se em um canal|-|-|-|
|RF38|Comprar bits|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|-|
|RNF39|Assinar o serviço Twitch Prime|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|-|
|RF40|Doar bits|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|-|
|RF41|Aderir Twitch Turbo|-|-|-|

______________________

## Matriz de Rastreabilidade - Backward From
Requisito|Descrição|Product Backlog|Esp. Casos de Uso|Cenário|Léxico|Moscow|First Things First|Introspecção|Análise de Protocolo/Observação Participativa|Storytelling|Questionário|RichPicture|Argumentação
---------|------|------|------|------|------|------|------|------|------|------|------|------|------
RF1|Cadastrar usuário|[US01](Product-Backlog)|[UC03 - Criar de Conta](Criação-de-Conta)|[Cenário 002](Cenário-002)|[Criar Conta](Criar-Conta)|[MoSCoW](MoSCoW)|[First Things First](First-Things-First)|-|-|-|-|-|-
RNF2|Logar via Facebook|[US02](Product-Backlog)|[UC03 - Criar de Conta](Criação-de-Conta)|[Cenário 002](Cenário-002)||[MoSCoW](MoSCoW)|-|-|-||||
RF3|Editar perfil|[US03](Product-Backlog)|-|[Cenário 023](Cenário-023)|-|[MoSCoW](MoSCoW)|[First Things First](First-Things-First)|-|-|-|-|-|-
RF4|Desabilitar conta|[US04](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-
RF5|Tornar-se Twitch Prime|[US05](Product-Backlog)|[UC13 - Assinar Twitch Prime](Assinar-Twitch-Prime)|-|[Twitch Prime](Twitch-Prime)|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|[RichPicture](RichPicture)|[Argumentação](Argumentação)
RF6|Tornar-se parceiro [Twitch](Twitch)|[US06](Product-Backlog)|-|-||-|-|-|-||||
RF7|Compartilhar uma [Stream](Stream)|[US07](Product-Backlog)|[UC18 - Compartilhar uma transmissão]()|-||-|-|-|-|-|-|[RichPicture](RichPicture)|
RF8|Seguir um [Streamer](Streamer)|[US08](Product-Backlog)|[UC15 - Seguir Canal]()|-||-|-|-|-|-|||
RF9|Acessar os chats|[US09](Product-Backlog)|-|-||-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|||
RF10|Filtrar quem digita no chat|[US010](Product-Backlog)|[UC09 - Restringir Chat]()|-||-|-|-|-|-|||
RF11|Banir alguém do chat|[US011](Product-Backlog)|[UC16 - Banir Viewer]()|-||-|-|-|-|-|||
RF12|Alterar conteúdo da [Stream](Stream)|[US012](Product-Backlog)|-|-||[MoSCoW](MoSCoW)|-|-|-|-|-||
RF13|Visualizar chat de [Stream](Stream)|[US013](Product-Backlog)|-|-||[MoSCoW](MoSCoW)|[First Things First](First-Things-First)|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|||
RF14|Subir um vídeo na [Twitch](Twitch)|[US014](Product-Backlog)|[UC19 - Criar Vídeo]()|-||-|-|-|-|-|||
RF15|Deletar um vídeo|[US015](Product-Backlog)|-|-||-|-|-|-|-|||
RF16|Programar uma premiere|[US016](Product-Backlog)|[UC19 - Criar Vídeo]()|-||-|-|-|-|-|-|[RichPicture](RichPicture)|
RF17|Gravar uma transmissão|[US017](Product-Backlog)|[UC02 - Transmitir Multimídia]()|-||-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|||
RF18|Destacar um vídeo|[US018](Product-Backlog)|-|[Cenário 005](Cenário-005)||[MoSCoW](MoSCoW)|-|-|-|-|||
RF19|Buscar outros usuários|[US019](Product-Backlog)|[UC17 - Adicionar Amigo]()|-||-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|||
RF20|Adicionar outro usuário como amigo|[US20](Product-Backlog)|[UC17 - Adicionar Amigo]()|-||-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|||
RF21|Mandar mensagens privadas|[US21](Product-Backlog)|[UC08 - Enviar Mensagens Privadas]()|-||-|-|-|-|-|||
RF22|Participar de chats|[US22](Product-Backlog)|-|-||-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|||
RF23|Mandar emoticons|[US23](Product-Backlog)|-|-||-|-|-|-|-|||
RF24|Bloquear alguém em uma conversa|[US24](Product-Backlog)|[UC08 - Enviar Mensagens Privadas]()|-||-|-|-|-|-|||
RF25|Sincronizar add-ons|[US25](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|||
RF26|Filtrar os add-ons vistos|[US26](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|||
RF27|Instalar novos add-ons|[US27](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|||
RF28|Deletar add-ons|[US28](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|||
RF29|Disponibilizar novos add-ons|[US29](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|||
RF30|Atualizar os add-ons de forma automatizada|[US30](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|||
RF31|Criar uma nova chamada de voz|[US31](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-||-|-|-|-|-|||
RF32|Filtrar usuários que entrarem na chamada|[US32](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-||-|-|-|-|-|||
RF33|Realizar uma vídeo conferência|[US33](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-||-|-|-|-|-|||
RF34|Usar uma video conferência em um servidor|[US34](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-||-|-|-|-|-|||
RF35|Criar um grupo para chamadas permanentes|[US35](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-||-|-|-|-|-|||
RNF36|Opções de planos de inscrições|[US36](Product-Backlog)|[UC04 - Inscrever em canal]()|-||-|-|-|-|-|||
RF37|Inscrever-se em um canal|[US37](Product-Backlog)|[UC04 - Inscrever em canal]()|-||-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|[RichPicture](RichPicture)|
RF38|Comprar bits|[US38](Product-Backlog)|[UC06 - Comprar Bits]()|-||-|-|-|-|-|-|[RichPicture](RichPicture)|
RNF39|Assinar o serviço Twitch Prime|[US39](Product-Backlog)|[UC13 - Assinar Twitch Prime]()|-||-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|[RichPicture](RichPicture)|
RF40|Doar bits|[US40](Product-Backlog)|[UC05 - Doar Bits]()|-||-|-|-|-|-|-|[RichPicture](RichPicture)|
RF41|Aderir Twitch Turbo|[US41](Product-Backlog)|-|-||-|-|-|-|-|||
