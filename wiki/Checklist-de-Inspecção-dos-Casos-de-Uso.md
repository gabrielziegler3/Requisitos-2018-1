|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|23/05/2018|0.1|Criação do Documento|Thiago Ferreira|
|24/05/2018|0.2|Adição de tópicos para as respostas e numeração para as perguntas|Thiago Ferreira|
|28/05/2018|0.3|Adição dos resultados da inspecção dos itens 1-8|Thiago Ferreira|
|29/05/2018|0.4|Adição dos resultados da inspecção dos itens 9-16|Thiago Ferreira|

* Checklist de Inspeção dos Casos de Uso
* Inspetor: Thiago Ferreira
* Data: 23/05/2018

|Item|Perguntas para inspeção dos Casos de Uso|
|------|-------|
|1|A descrição é sucinta e suficiente?|
Resposta|Sim|
Modificações|Alterar descrição do UC02, UC09, UC10, UC11, UC19, para o padrão dos demais documentos, que usam 'Este caso de uso' no ínicio da descrição.|
|2|A descrição aborda de forma correta o tema do caso de uso?|
Resposta|Sim|
Modificações|Nenhuma|
|3|Os atores atuantes estão corretos?|
Resposta|Caso, a verificação das modificações esteja correta, sim.|
Modificações|Verificar se, a Twitch contaria como um ator, dentro do envolvimento do usuário com a plataforma em alguns casos, alteração nos hiperlinks do UC16.|
|4|Os atores estão sendo representados corretamente dentro dos casos de uso?|
Resposta|Não|
Modificações|UC01, atores não descritos de forma específica, utilizando um usuário genérico ao invés do geral em casos que existem mais de um ator. UC03, utiliza terminologia confusa quanto à referência do ator. UC05 lista o ator usuário e o ator streamer que é um especialização do ator usuário. UC13 possui ator fora do formato padrão.|
|5|As Pré-Condições são realmente necessárias para o funcionamento do requisito descrito no caso de uso?|
Resposta|Sim|
Modificações|UC14, UC15, alteração da descrição da pre-condição para o padrão do restante dos documentos|
|6|O Fluxo principal segue o padrão adotado na elaboração do documento?|
Resposta|Não|
Modificações|UC13,UC14, UC19, alterações para o padrão|
|7|O Fluxo principal segue a ordem correta para a realização da tarefa do caso de uso?|
Resposta|Não|
Modificações|UC13, adequação à ordem correta da realização das tarefas, UC14 está faltando com alguns passos.|
|8|O Fluxo principal possui as tags representando o fluxo alternativo?|
Resposta|Não|
Modificações|Alteração nas tags de fluxo alternativo nas UC09, UC13, UC15, UC18|
|9|Ao seguir os passos, a tarefa é corretamente concluída?|
Resposta|Não|
Modificações|Adicionar caso de uso completado como passo final nas UC17 e UC18, Adicionar passo de validação dos dados inseridos na UC03, mesclar FA01 ao Fluxo Principal e adicionar passo de seleção de pagamento à UC06, Adicionar tópico de validação dos dados inseridos na UC03.|
|10|Os fluxos alternativos descritos são corretamente representados?|
Resposta|Não|
 Modificações|UC06 possui um fluxo alternativo que deveria estar no fluxo principal.|
|11|Os fluxos alternativos adentram o fluxo principal corretamente?|
Resposta|Não|
Modificações|FA01 da UC03 possui um fluxo alternativo que não segue a linha do fluxo principal nem retorna a ele. FA da UC13 não adentra o fluxo principal.|
|12|Os passos descritos no fluxo alternativo possibilitam a completude correta do fluxo?|
Resposta|Não|
Modificações|FA01 da UC03 possui estado independente e os fluxos alternativos da UC13 não completam adequadamente o fluxo.|
|13|Os fluxos de exceção são corretamente descritos?|
Resposta|Não|
Modificações|UC13, UC16 e UC06 são descritos incorretamente|
|14|Os fluxos de exceção são representados corretamente do fluxo principal?|
Resposta|Não|
Modificações|FE01 inserido ao passo 4 da UC01, FE01 inserido tag ao passo 3 da UC02, FE01 adicionado ao passo 7 do Fluxo Principal, Adicionar tag do FE01 ao passo iv da UC06, adicionar tag FE02 ao passo 5 da UC08 e adicionar tags dos FE da UC13 após a correção.  |
|15|Os erros descritos no fluxo de exceção ocorre de fato?|
Resposta|Não|
Modificações|UC06 possui um fluxo de exceção que é um fluxo alternativo e o UC13 possui um fluxo de exceção escrito de maneira inadequada.|
|16|A Pós-condição é corretamente cumprida e descrita?|
Resposta|Sim|
Modificações|Alteração gramática na UC05, Alteração para descrição mais sucinta da UC13, remoção de numeração em frente a UC14, UC15 e UC19|