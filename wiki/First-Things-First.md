|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|03/04/2018|1.0|Criação do Documento|Filipe Dias|
|11/06/2018|1.1|Conversão da tabela para Markdown|Gabriel Ziegler|

### 1. Introdução
#### 1.1. Propósito
* Este artefato tem como propósito apresentar a análise feita a partir da utilização da técnica de priorização 'First Things First' a partir das funcionalidades da [Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Twitch).

#### 1.2. Escopo
* Serão levantadas as análises das funcionalidades da [Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Twitch), divididas de tal modo que, seja possível levantar cálculos cálculos de benefício, penalidade, custo e risco relativos a tais funcionalidades, indicados pela técnica de priorização utilizada (FTF).

### 2. Objetivos
* Ao utilizar a técnica de priorização de requisitos, o objetivo a se alcançar é estabelecer uma certa ordem de prioridade em relação à implementação de certas funcionalidades, considerando fatores que impactam na disponibilização delas aos usuários da aplicação.

_________

###
|Funcionalidade|Estado|Justificativa|
|---|---|----|
|Assistir Stream|Permanece||
|Participar do Group Chat|Não permanece|Depende de "Assistir Stream"|
|Dar Subscribe/Follow|Não permanece|Depende de "Assistir Stream"|
|Cadastrar na Twitch|Permanece||
|Editar/Atualizar Perfil|Permanece||
|Tornar-se Twitch Prime|Não permanece|Depende de "Cadastrar na Twitch"|
|Realizar Donates|Não permanece|Depende de "Assistir Stream"|
|Realizar uma Stream|Permanece||
|Adicionar Add-ons|Não permanece|Depende de "Realizar uma Stream"|
|Tornar-se Twitch-Partner|Não permanece|Depende de "Realizar uma Stream"|
|Banir alguém do chat|Não permanece|Depende de "Realizar uma Stream"|
|Alterar o conteúdo da Stream|Não permanece|Depende de "Realizar uma Stream"|
|Clipar uma Stream|Não permanece|Depende de "Realizar uma Stream"|
|Fazer login|Permanece||
|Traduzir para várias linguagens|Permanece||
|Adicionar amigos|Não permanece|Depende de "Cadastrar" na Twitch|
|Visualizar dados Pessoais|Permanece||
|Funcionar 24/7|Permanece||
|Receber notificações|Não permanece|Depende de "Cadastrar na Twitch"|
|Adicionar formas de pagamento|Não permanece|Depende de "Cadastrar na Twitch"|
|Realizar Cadastro por redes sociais|Não permanece|Depende de outras ferramentas alheias à Twitch|

### 3. Tabela de Prioridade
FEATURES/FUNCIONALIDADES|BENEFÍCIO RELATIVO|PENALIDADE RELATIVA|VALOR TOTAL|VALOR %|CUSTO RELATIVO|CUSTO %|RISCO RELATIVO|RISCO %|PRIORIDADE
|------|------|------|------|------|------|------|------|------|------|
Cadastrar-me na [Twitch](https://github.com/gabrielziegler3/Requisitos-2018-1/wiki/Twitch).|5|6|16|14.95327103|2|6.25|2|7.407407407|0.6459813084
Fazer login|5|6|16|14.95327103|2|6.25|2|7.407407407|0.6459813084
Traduções|7|2|16|14.95327103|7|21.875|4|14.81481481|0.09228304406
Atualizar meus dados pessoais.|2|1|5|4.672897196|3|9.375|2|7.407407407|0.1345794393
Vizualizar meus dados pessoais.|1|1|3|2.803738318|3|9.375|2|7.407407407|0.08074766355
Assistir uma streaming sem estar logado.|7|6|20|18.69158879|6|18.75|7|25.92592593|0.07690253672
Recuperar username.|6|6|18|16.82242991|2|6.25|2|7.407407407|0.726728972
Funcionar 24/7.|6|1|13|12.14953271|7|21.875|6|22.22222222|0.04998664887
TOTAL|39|29|107|100|32|100|27|100|

### 4. Resultados
* Ao todo, foram analisadas 21 funcionalidades. Apesar do número pequeno de funcionalidades analisadas, o objetivo fora analisar as funcionalidades cruciais para o funcionamento da plataforma de LiveStreaming. Cada uma delas recebeu uma atribuição de benefício (agregação de valor), penalidade (perda de valor com a falta da funcionalidade), custo (custo de desenvolvimento) e risco (viabilidade de implementação), o que, pela utilização da técnica fornecida pelo FTF, possibilitou o cálculo da prioridade de cada uma.

### 5. Conclusão
* A utilização da técnica 'First Things First' como priorização de requisitos possibilita a definição de funcionalidades que devem ser consideradas prioridade na hora da implementação. Tal fato, permite aos desenvolvedores e toda a equipe entenderem os eventos que podem exercer influência no planejamento de um software.
[Dados e Estatísticas](Dados-e-Estat%C3%ADsticas)