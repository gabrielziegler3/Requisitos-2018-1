|Data|Versão|Descrição|Autor|
|----|------|---------|-----|
|22/05/2018|0.1|Criação do Documento|Thiago Ferreira|
|23/05/2018|0.2|Adição de descrições e referências|Amanda Pires|
|23/05/2018|0.3|Adição descrições do processo semi-automatizado|Gabriel Ziegler|
|11/06/2018|0.4|Revisão e correção|Gabriel Ziegler|

# Inspecção
A inspeção é um método que contribui para garantir a qualidade do produto de software. Todas as etapas do processo de desenvolvimento de software são suscetíveis à incorporação de defeitos, que podem ser detectados pela inspeção e posteriormente removidos.Logo, revisaremos os documentos de elicitação, os cenários e léxicos, os Casos de Usos produzidos, as histórias de usuário levantas, os diagramas NFR e os diagramas iStar.

O processo de inspeção inclui as seguintes etapas:

### Planejamento

 Nesta etapa, é determinado se os materiais que serão inspecionados são adequados, organiza-se as pessoas que irão participar da inspeção e define-se o local onde serão realizadas as sessões de inspeção.

### Visão Geral

Esta etapa inclui a apresentação do material a ser inspecionado aos participantes e a atribuição de funções aos participantes, durante a inspeção.

### Preparação

Nesta etapa, os participantes são treinados para executarem as funções que lhes foram atribuídas, visando encontrar os defeitos constantes do produto ou artefato de software.

### Realização da Inspeção

 Esta etapa inclui sessões de trabalho, nas quais os participantes analisam o produto ou artefato de software, com o fim de detectar os defeitos existentes nesses produtos.
Existem várias técnicas de inspeção para encontrar defeitos em artefatos, entre elas
* Leitura baseada em Checklist (LBCh)
* Leitura Baseada em Cenário (LBCe)
* Leitura Baseada em Perspectiva (LBPe)

A equipe optou por utilizar a técnica LBCh.

Alguns processos das inspeções foram feitas utilizando-se de scripts que ou automatizavam a correção de erros, ou melhorava a forma com que o inspetor analisava as questões levantadas nos questionários. Esses processos foram documentados na [inspeção semi automatizada](Inspeção-Semi-Automatizada).

### Retrabalho

 Nesta etapa, os defeitos detectados, devidamente documentados, são encaminhados ao autor do produto que foi inspecionado, para que seja providenciada a remoção destes defeitos

### Revisão

 Nesta etapa, o autor confere o produto revisado, juntamente com a equipe de inspeção, para assegurar-se de que todas as correções necessárias foram realizadas e que nenhum defeito novo foi introduzido.

# Verificações
* [Pré Rastreabilidade](Verificação-Pre-Rastreabilidade)
* [Elicitação](Verificação-Elicitação)
* [Cenários e Léxicos](Verificação-Cenários-e-Léxicos)
* [Casos de Uso](Verificação-Casos-de-Uso)
* [Histórias de Usuário](Verificação-Histórias-de-Usuário)
* [NFR](Verificação-NFR)
* [iStar](Verificação-iStar)

# Validação

Como a validação é uma técnica realizada em junta ao cliente, o time de engenharia de requisitos decidiu que não seria adequado a aplicação dessa técnica no momento atual, já que o time está fazendo um estudo em cima de uma plataforma já desenvolvida e não desenvolvendo um sistema novo.

# Referências

* [Técnicas de inspeção](http://www.inf.puc-rio.br/~wer/WERpapers/artigos/artigos_WER06/bertini.pdf)
* [Uma abordagem sobre inspeção de documentos ](http://www.lbd.dcc.ufmg.br/colecoes/sbqs/2006/012.pdf)