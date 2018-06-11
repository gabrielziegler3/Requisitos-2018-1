|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|05/06/2018|1.0|Criação do Documento|Amanda Pires|
|05/06/2018|1.1|Edição do Documento|Filipe Dias|
|05/06/2018|1.2|Adição de conteúdo ao Documento|Filipe Dias, João Carlos, Gustavo Carvalho, Amanda Pires, Thiago Ferreira, Gabriel Ziegler|
|06/06/2018|1.3|Adição de conteúdo na tabela Backward From|Filipe Dias, João Carlos, Gustavo Carvalho, Amanda Pires, Thiago Ferreira, Gabriel Ziegler|
|10/06/2018|1.4|Adição de conteúdo na tabela Forward From|Gabriel Ziegler|
|10/06/2018|1.5|Adição US42 a 52|Gustavo Carvalho|
|10/06/2018|1.6|Inserção de rastreabilidade de artefato de desenho|Gustavo Carvalho|
|10/06/2018|1.7|Adição de conteúdo na tabela Forward From e correção no artefato|Gabriel Ziegler|
|10/06/2018|1.8|Adição de conteúdo na tabela Forward From|João Carlos|
|10/06/2018|1.9|Adição de conteúdo na tabela Backward From|Gustavo Carvalho|

# Pós rastreabilidade

## Matriz de Rastreabilidade - Forward From

|Requisito|Descrição|NFR|I*|Artefato de Desenho|
|:---------:|:------|:------:|:-------:|:------:|
|RF1|Cadastrar usuário|-|[SR Visitante](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#visitante)|[Tela de cadastro usuário](./images/artefato-de-desenho/RF1.png)|
|RNF2|Logar via Facebook|-|[SR Visitante](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#visitante)|[Tela login via facebook](./images/artefato-de-desenho/RNF2.png)|
|RF3|Editar perfil|-|[SR Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#usu%C3%A1rio)|[Tela de editar perfil](./images/artefato-de-desenho/RF3.png)|
|RF4|Desabilitar conta|-|[SR Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#usu%C3%A1rio)|[Tela de desabilitar conta](./images/artefato-de-desenho/RF6.png)|
|RF5|Tornar-se Twitch Prime|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|[Tela de cadastro Twitch Prime](./images/artefato-de-desenho/RF5.png)|
|RF6|Tornar-se parceiro [Twitch](Twitch)|-|-|[Tela de cadastro parceiro Twitch](./images/artefato-de-desenho/RF6.png)|
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
|RF21|Mandar mensagens privadas|-|-|[Tela mandar mensagem privada](./images/artefato-de-desenho/RF21.png)|
|RF22|Participar de chats|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|[Tela participar de chat](./images/artefato-de-desenho/RF22.png)|
|RF23|Mandar emoticons|-|-|[Tela mandar emoctions](./images/artefato-de-desenho/RF23.png)|
|RF24|Bloquear alguém em uma conversa|-|-|[Tela bloquear usuário](./images/artefato-de-desenho/RF24.png)|
|RF25|Sincronizar [add-ons](Mods)|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF26|Filtrar os [add-ons](Mods) vistos|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF27|Instalar novos [add-ons](Mods)|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF28|Deletar [add-ons](Mods)|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF29|Disponibilizar novos [add-ons](Mods)|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF30|Atualizar os [add-ons](Mods) de forma automatizada|-|[SR Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Rationale#twitch)|-|
|RF31|Criar uma nova chamada de voz|-|-|[Tela criar nova chamada de voz](./images/artefato-de-desenho/RF31.png)|
|RF32|Filtrar usuários que entrarem na chamada|-|-|-|
|RF33|Realizar uma vídeo conferência|-|-|-|
|RF34|Usar uma video conferência em um servidor|-|-|-|
|RF35|Criar um grupo para chamadas permanentes|-|-|-|
|RNF36|Opções de planos de inscrições|-||[Tela de opções de inscrições](./images/artefato-de-desenho/RNF36.png)|
|RF37|Inscrever-se em um canal|-|-|[Tela de se inscrever em canal](./images/artefato-de-desenho/RF37.png)|
|RF38|Comprar [bits](Bits)|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|[Tela de comprar bits](./images/artefato-de-desenho/RF38.png)|
|RNF39|Assinar o serviço Twitch Prime|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|[Tela para assinar Twitch Prime](./images/artefato-de-desenho/RNF39.png)|
|RF40|Doar [bits](Bits)|-|[SD Twitch - Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Strategic-Dependency#twitch---usu%C3%A1rio-32)|[Tela de doar bits](./images/artefato-de-desenho/RF40.png)|
|RF41|Aderir Twitch Turbo|-|-|[Tela para aderir a Twtich Turbo](./images/artefato-de-desenho/RF41.png)|
|RF42|Recuperar senha e usuário|-|-|[Tela de recuperação de senha e usuário](./images/artefato-de-desenho/RF42.png)|
|RF43|Assistir stream sem estar logado|-|-|[Tela de stream sem login](./images/artefato-de-desenho/RF43.png)|
|RF44|Criar [clips](Clipes)|-|-|[Tela de criar clips](./images/artefato-de-desenho/RF44.png)|
|RNF45|Boa usabilidade|[Usabilidade](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us48---usabilidade)|-|-|
|RNF46|Suportar muitos acessos/visitas|[Perfomance para Usuário](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us49---performance-para-o-usu%C3%A1rio)|-|-|
|RNF47|Segurança em transações financeiras|[Segurança](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us50---seguran%C3%A7a)|-|-|
|RNF48|Sistema de login robusto|[Confiabilidade](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us54---confiabilidade), [Segurança](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us50---seguran%C3%A7a)|-|-|
|RNF49|Fluidez em transmissões|[Performance](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us51--performance-para-a-stream)|-|-|
|RNF50|Funcionamento 24h/7|[Disponibilidade](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us53---disponibilidade)|-|-|
|RNF51|Portabilidade|[Portabilidade](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/NFR#us52---portabilidade)|-|[Tela do app para desktop](./images/artefato-de-desenho/RNF51.png)|
|RF52|Tradução|-|-|[Tela de opções de idiomas](./images/artefato-de-desenho/RF52.png)|

______________________

## Matriz de Rastreabilidade - Backward From
Requisito|Descrição|Product Backlog|Esp. Casos de Uso|Cenário|Léxico|Moscow|First Things First|Introspecção|Análise de Protocolo/Observação Participativa|Storytelling|Questionário|RichPicture|Argumentação
---------|------|------|------|------|------|------|------|------|------|------|------|------|------
|RF1|Cadastrar usuário|[US01](Product-Backlog)|[UC03 - Criar de Conta](Criação-de-Conta)|[Cenário 002](Cenário-002)|[Criar Conta](Criar-Conta)|[MoSCoW](MoSCoW)|[First Things First](First-Things-First)|-|-|-|-|-|-
|RNF2|Logar via Facebook|[US02](Product-Backlog)|[UC03 - Criar de Conta](Criação-de-Conta)|[Cenário 002](Cenário-002)||[MoSCoW](MoSCoW)|-|-|-|-|-|-|
|RF3|Editar perfil|[US03](Product-Backlog)|-|[Cenário 023](Cenário-023)|-|[MoSCoW](MoSCoW)|[First Things First](First-Things-First)|-|-|-|-|-|-
|RF4|Desabilitar conta|[US04](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-
|RF5|Tornar-se Twitch Prime|[US05](Product-Backlog)|[UC13 - Assinar Twitch Prime](Assinar-Twitch-Prime)|-|[Twitch Prime](Twitch-Prime)|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|[RichPicture](RichPicture)|[Argumentação](Argumentação)
|RF6|Tornar-se parceiro [Twitch](Twitch)|[US06](Product-Backlog)|-|-||-|-|-|-|-|-|-|
|RF7|Compartilhar uma [Stream](Stream)|[US07](Product-Backlog)|[UC18 - Compartilhar uma transmissão]()|-||-|-|-|-|-|-|[RichPicture](RichPicture)|
|RF8|Seguir um [Streamer](Streamer)|[US08](Product-Backlog)|[UC15 - Seguir Canal]()|-|-|-|-|-|-|-|-|-|
|RF9|Acessar os chats|[US09](Product-Backlog)|-|-|-|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|-|
|RF10|Filtrar quem digita no chat|[US010](Product-Backlog)|[UC09 - Restringir Chat]()|-||-|-|-|-|-|-|-|
|RF11|Banir alguém do chat|[US011](Product-Backlog)|[UC16 - Banir Viewer]()|-|-|-|-|-|-|-|-|-|
|RF12|Alterar conteúdo da [Stream](Stream)|[US012](Product-Backlog)|-|-|-|[MoSCoW](MoSCoW)|-|-|-|-|-|-|
|RF13|Visualizar chat de [Stream](Stream)|[US013](Product-Backlog)|-|-||[MoSCoW](MoSCoW)|[First Things First](First-Things-First)|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|-|
|RF14|Subir um vídeo na [Twitch](Twitch)|[US014](Product-Backlog)|[UC19 - Criar Vídeo]()|-||-|-|-|-|-|-|-|
|RF15|Deletar um vídeo|[US015](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|
|RF16|Programar uma premiere|[US016](Product-Backlog)|[UC19 - Criar Vídeo]()|-|-|-|-|-|-|-|-|[RichPicture](RichPicture)|
|RF17|Gravar uma transmissão|[US017](Product-Backlog)|[UC02 - Transmitir Multimídia]()|-|-|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|-|
|RF18|Destacar um vídeo|[US018](Product-Backlog)|-|[Cenário 005](Cenário-005)|-|[MoSCoW](MoSCoW)|-|-|-|-|-|-|
|RF19|Buscar outros usuários|[US019](Product-Backlog)|[UC17 - Adicionar Amigo]()|-|-|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|-|
|RF20|Adicionar outro usuário como amigo|[US20](Product-Backlog)|[UC17 - Adicionar Amigo]()|-|-|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|-|
|RF21|Mandar mensagens privadas|[US21](Product-Backlog)|[UC08 - Enviar Mensagens Privadas]()|-|-|-|-|-|-|-|-|-|
|RF22|Participar de chats|[US22](Product-Backlog)|-|-|-|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|-|
|RF23|Mandar emoticons|[US23](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|
|RF24|Bloquear alguém em uma conversa|[US24](Product-Backlog)|[UC08 - Enviar Mensagens Privadas]()|-|-|-|-|-|-|-|-|-|
|RF25|Sincronizar [add-ons](Mods)|[US25](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-|-|-|-|-|-|-|-|-|
|RF26|Filtrar os [add-ons](Mods) vistos|[US26](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|-|-|
|RF27|Instalar novos [add-ons](Mods)|[US27](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|-|-|
|RF28|Deletar [add-ons](Mods)|[US28](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|||
|RF29|Disponibilizar novos [add-ons](Mods)|[US29](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-||-|-|-|-|-|-|-|
|RF30|Atualizar os [add-ons](Mods) de forma automatizada|[US30](Product-Backlog)|[UC10 - Adicionar Add-ons em jogos]()|-|-|-|-|-|-|-|-|-|
|RF31|Criar uma nova chamada de voz|[US31](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-|-|-|-|-|-|-|-|-|
|RF32|Filtrar usuários que entrarem na chamada|[US32](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-|-|-|-|-|-|-|-|-|
|RF33|Realizar uma vídeo conferência|[US33](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-|-|-|-|-|-|-|-|-|
|RF34|Usar uma video conferência em um servidor|[US34](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-|-|-|-|-|-|-|-|-|
|RF35|Criar um grupo para chamadas permanentes|[US35](Product-Backlog)|[UC11 - Enviar Chat de Voz]()|-|-|-|-|-|-|-|-|-|
|RNF36|Opções de planos de inscrições|[US36](Product-Backlog)|[UC04 - Inscrever em canal]()|-|-|-|-|-|-|-|-|-|
|RF37|Inscrever-se em um canal|[US37](Product-Backlog)|[UC04 - Inscrever em canal]()|-|-|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|[RichPicture](RichPicture)|
|RF38|Comprar [bits](Bits)|[US38](Product-Backlog)|[UC06 - Comprar Bits]()|-|-|-|-|-|-|-|-|[RichPicture](RichPicture)|
|RNF39|Assinar o serviço Twitch Prime|[US39](Product-Backlog)|[UC13 - Assinar Twitch Prime]()|-|-|-|-|-|[Análise de Protocolo](Híbrido-(Análise-de-Protocolo--&-Observação-Participativa))|-|-|[RichPicture](RichPicture)|
|RF40|Doar [bits](Bits)|[US40](Product-Backlog)|[UC05 - Doar Bits]()|-|-|-|-|-|-|-|-|[RichPicture](RichPicture)|
|RF41|Aderir Twitch Turbo|[US41](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|
|RF42|Recuperar senha e usuário|[US42](Product-Backlog)|-|-|-|-|[First Things First](First-Things-First)|-|-|-|-|-|[Cadastro 1.1.0](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Argumenta%C3%A7%C3%A3o#cadastro-110)|
|RF43|Assistir stream sem estar logado|[US43](Product-Backlog)|-|-|-|-|[First Things First](First-Things-First)|-|-|-|-|-|-|
|RF44|Criar [clips](Clipes)|[US44](Product-Backlog)|-|-|-|[MoSCoW](MoSCoW)|-|-|-|[Storytelling](Storytelling)|-|-|-|
|RNF45|Boa usabilidade|[US45](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-|
|RNF46|Suportar muitos acessos/visitas|[US46](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-|
|RNF47|Segurança em transações financeiras|[US47](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-|
|RNF48|Sistema de login robusto|[US48](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-|
|RNF49|Fluidez em transmissões|[US49](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-|
|RNF50|Funcionamento 24h/7|[US50](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|-|
|RNF51|Portabilidade|[US51](Product-Backlog)|-|-|-|-|-|-|-|-|-|-|[Twitch Desktop App 1.0](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Argumenta%C3%A7%C3%A3o#twitch-desktop-app-100)|
|RF52|Tradução|[US52](Product-Backlog)|-|-|-|-|[First Things First](First-Things-First)|-|-|-|-|-|-|

