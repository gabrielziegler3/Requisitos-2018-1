* Checklist de Inspeção dos Cenários e Léxicos
* Inspetor: Gabriel Ziegler
* Data: 23/05/2018

#### 1. Cenários
|Item de Inspeção|Cenários|
|------|-------|
Questões|1 - Todos os cenários possuem título?|
Resposta|Sim|
Modificações|Nenhuma|
Commit|-|
Questões|2 - Todos os cenários possuem objetivo?|
Resposta|Sim|
Modificações|Nenhuma|
Commit|-|
Questões|3 - Estão inseridos em um contexto?|
Resposta|Sim|
Modificações|Nenhuma|
Commit|-|
Questões|4 - Todos os atores estão devidamente definidos?|
Resposta|Não, o ator do Cenário-013 estava mal definido, visto que definia duplamente o [Streamer](Streamer) como ator|
Modificações|Um único ator foi mantido|
Commit|6711c3|
Questões|5 - Os cenários se enquadram em todos os fluxos para a execução de uma tarefa?|
Resposta|Sim|
Modificações|Nenhuma|
Commit|-|
Questões|6 - Os episódios estão bem definidos?|
Resposta|Sim|
Questões|7 - Existem padrões entre as descrições dos episódios dos cenários?|
Resposta|Sim|
Modificações|Nenhuma|
Commit|-|
Questões|8 - Todos os cenários estão linkados com os léxicos?|
Resposta|Não, os cenários que envolviam [Streamer](Streamer) possuiam dois léxicos distintos.| 
Modificações|O léxico correto foi mantido e os *hyperlinks* dos léxicos foram consertados|
Commit|ef44e3b|
Questões|9 - Os atores estão linkados com os léxicos?
Resposta|Não, Usuários não possuiam léxicos, [Streamer](Streamer) e [Viewer](Viewer) possuiam algumas menções sem representação de seus léxicos|
Modificações|Todos atores foram linkados com seus respectivos léxicos. O léxico de Usuário teve de ser criado para adequar aos padrões|
Commit|e9343e0, a626ec|
Questões|10 - Os links para os léxicos estão funcionando?
Resposta|Sim|
Modificações|Nenhuma|
Commit|-|

#### Léxicos

|Item de Inspeção|Léxico|
|------|-------|
|Questões|1 - Os sinônimos dos léxicos possuem e seguem uma padronização?|
|Resposta|Sim|
|Modificação|Nenhuma|
|Commit|-|
|Questões|2 - As noções dos léxicos possuem e seguem uma padronização?|
|Resposta|Sim|
|Modificação|Nenhuma|
|Commit|-|
|Questões|3 - Os impactos dos léxicos possuem e seguem uma padronização?|
|Resposta|Sim|
|Modificação|Nenhuma|
|Commit|-|
|Questões|4 - Todos os impactos estão definidos?|
|Resposta|Sim|
|Modificação|Nenhuma|
|Commit|-|
|Questões|5 - Os léxicos contém sinônimos?|
|Resposta|Não todos, mas mais de 90%, então não há necessidades de mudanças|
|Modificação|Nenhuma|
|Commit|-|
|Questões|6 - Os links dos léxicos estão funcionando?|
|Resposta|Não, alguns não estavam linkados(viewer, streamer, stream) outros estavam com links quebrados|
|Modificação|Links reparados e funcionando corretamente|
|Commit|718fe4054|

