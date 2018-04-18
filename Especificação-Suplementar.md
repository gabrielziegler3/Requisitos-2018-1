Data|Versão|Descrição|Autor
-----|------|---------|-------
17/04/2018|1.0|Criação do documento|Thiago Ferreira|
18/04/2018|1.1|Inclusão de conteúdo|Filipe Dias|
18/04/2018|1.2|Inclusão de conteúdo de Qualidade de Software|Gabriel Ziegler|

<h1> 1. Introdução </h1>

## 1.1 Finalidade

Este Documento tem como finalidade armazenar a elicitação de requisítos não funcionais para a plataforma Twitch, feita pela equipe de requisitos de software.
A Especificação Suplementar captura os requisitos de sistema que não são capturados imediatamente nos casos de uso do modelo de casos de uso. Entre os requisitos estão incluídos:

* Requisitos legais e reguladores, incluindo padrões de aplicativo.

* Atributos de qualidade do sistema a ser criado, incluindo requisitos de usabilidade, confiabilidade, desempenho e suportabilidade.

* Outros requisitos, como sistemas operacionais e ambientes, requisitos de compatibilidade e restrições de design.

<h2> 1.2 Escopo </h2>

<p align="justify">Este documento visa apontar requisitos não funcionais, desempenhados pelo sistema, de modo a apresentar assuntos que abrangem funcionalidades referentes a questão de qualidade e desempenho garantidas pelo software. </p>

<h2> 1.3 Definições, Acrônimos e Abreviações </h2>

Alguns dos acrônimos, definições e abreviações usados neste documento são:

* Viewer: Espectador
* Streamer: Transmissor
* Donate: Doação feita à um streamer
* Bits: Forma específica de doação
* UX: User Experience, refere-se à experiência do usuário ao usar a aplicação.

<h2> 1.4 Referências </h2>

[Twitch developer](https://dev.twitch.tv/)

<h2> 1.5 Visão Geral </h2>
<p align="justify">O documento está organizado da seguinte maneira:</p>
<ul>
    <li> Seção 1: Faz uma breve introdução do documento, expondo sua finalidade (para que serve), escopo (conteúdo), definições de termos que serão usadas no documento e referências; </li>
   <li>Seção 2: Explica cada requisito não funcional de usabilidade da aplicação;</li>
   <li>Seção 3: Explica cada requisito não funcional de confiabilidade da aplicação;</li>
   <li>Seção 4:Explica o requisito não funcional de suportabilidade (ou portabilidade) da aplicação;</li>
   <li>Seção 5: Desenvolve as restrições de design;</li>
   <li>Seção 6: Expõe as interfaces do sistema;</li>
   <li>Seção 7: Expõe informações legais e de direitos autorais.</li>
</ul>

<h1> 2. Usabilidade </h1>

<h2> 2.1 Termos Técnicos </h2>

<p align="justify"> O sistema não deve conter termos técnicos para não dificultar a aprendizagem do usuário. A linguagem será formal, no entanto acessível a qualquer um dos tipos de usuários que o sistema deverá ter.</p>

<h2> 2.2 Facilidade de Uso </h2>

<p align="justify">O sistema terá uma forma simples e intuitiva de utilização, sem haver necessidade de algum tipo de treinamento prévio. O uso de interfaces amigáveis em conjunto com design bem trabalhado providenciarão maior entendimento e uma melhor UX.</p>

<h2> 2.3 Relevância de usabilidade </h2>

<p align="justify">O sistema contém apenas soluções e ferramentas realmente relevantes e efetivas ao sistema, de forma simples e funcional, consideradas úteis para toda e qualquer atividade que o usuário decida exercer.</p>

<h2> 2.4 Eficácia </h2>
<p align="justify">O sistema visa ao máximo disponibilizar ferramentas simples, reduzidas e intuitivas ao usuário, mas ao mesmo tempo funcionais e diretas, de modo a tornar a relação do mesmo com o sistema eficaz, visando assim o melhor aproveitamento de seu tempo, evitando ,na medida do possível, operações desnecessárias no sistema.</p>

<h2> 2.5 Tratamento de erros </h2>

<p align="justify">O sistema deve prever e tratar erros. No caso de requisições iguais realizadas em menos de 3 segundos (ao dar F5 enquanto uma requisição está sendo executada, por exemplo), deve-se considerar apenas a primeira, para não gerar múltiplas ações iguais e não comprometer a eficiência do sistema;</p>

<h1> 3. Confiabilidade </h1>

<h2> 3.1 Garantia de funcionamento em tempo integral </h2>
<p align="justify">O nosso software deve funcionar em tempo integral, 24 horas por dia, mesmo com um volume intenso de dados, suportando os possíveis 80 mil usuários que podem utilizar o sistema, sem qualquer tipo de dano ou queda do mesmo, desde que a conexão à internet esteja estabelecida. </p>

<h2> 3.2 Garantia de armazenamento de dados </h2>
<p align="justify">O nosso software deve se comprometer em armazenar de forma correta todos os dados referentes ao usuário, de forma a não apresentar possíveis erros de armazenamento, para que desse modo não ocorra a necessidade de recadastramento do usuário no sistema. </p>

<h2> 3.3 Garantia de segurança no armazenamento de dados </h2>
<p align="justify">O nosso software deve se comprometer em garantir a segurança dos dados informados pelo usuário no momento de seu cadastramento no sistema, de modo que esses dados sejam guardados de forma segura e confiável, não sendo possível o acesso de outros usuários sem a devida permissão.</p>

<h1> 4. Suportabilidade </h1>
<p align="justify">O website será suportado em todos os navegadores e em qualquer sistema operacional (Windows, Mac e Linux). A performance da aplicação pode variar de um sistema para outro e também entre navegadores. É sugerido o uso da aplicação na versão mais atualizada do navegador Google Chrome para melhor UX.</p>
<h1> 5. Restrições de Design </h1>

<h2> 5.1 Interface Responsiva </h2>

<p align="justify">Os inúmeros dispositivos que são usados hoje para acessar a internet possuem diferentes tamanhos de tela, assim como diferentes resoluções e a  interface do sistema deverá se adequar a qualquer tamanho de tela.</p>

<h1> 6. Interfaces </h1>

<h2> 6.1 Interfaces de Usuário </h2>

* Tela de login
* Tela de perfil
* Tela de cadastro
* Tela de alteração de cadastro
* Tela de transmissão
* Tela de vídeos e clipes

<h2> 6.2 Interfaces de Hardware </h2>

* Notebooks
* Computadores de Mesa

<h2> 6.3 Interfaces de Software </h2>

* Todos os sistemas operacionais que possuem suporte a navegadores e acesso a internet.
* Todos navegadores web.

<h2> 7. Qualidade de software </h2>

<p align="justify">
Para mensurar e garantir a qualidade da usabilidade, eficiência, compatibilidade, confiabilidade, segurança, manutenabilidade, portabilidade do sistema, é utilizada a
<a href="http://iso25000.com/index.php/en/iso-25000-standards/iso-25010?limit=3&start=3")>
ISO 25010
</a>
que é utilizada na maior parte dos produtos de software desenvolvidos com boa qualidade.
</p>

![Software Product Quality ](http://iso25000.com/images/figures/en/iso25010.png)

<h1> 8. Observações Legais, Direitos Autorais </h1>

[Twitch copyright](https://www.twitch.tv/p/legal/dmca-guidelines/)