# UC13 - Assinatura Twitch Prime

### [Diagrama de Caso de Uso](Diagrama-Assinatura-Twitch-Prime)

## Descrição
* Este caso de uso descreve a assinatura no Twitch Prime.
* O Twitch Prime é uma experiência Premium da Twitch que vem em uma inscrição Amazon Prime ou Amazon Prime Video. O Twitch Prime inclui jogos e conteúdos de jogos, inscrição de canal a cada 30 dias sem custo adicional, que pode ser usada em qualquer canal de Parceiro ou Afiliado, visualização sem anúncios na Twitch, emotes exclusivos e distintivo de bate-papo.

## Atores
* Usuário Twitch

## Pré-condições
* O usuário deve ter acesso à internet
* O usuário deve estar logado no sistema

## Fluxo de Eventos
### Fluxo Principal
* 1. O usuário acessa o site da Twitch
* 2. O usuário clica em iniciar um teste gratuito.
* 3. O usuário conecta sua conta do Twitch a sua conta na Amazon.
* 4. O usuário automaticamente terá o Twitch Prime.

### Fluxos Alternativos
#### FA01 - O usuário é um Turbo Twitch
* 1. O usuário vai até a aba "Turbo" em configurações.
* 2. O clica na opção "Não renovar" no centro da página, ao lado do cronograma de cobrança.
* 3. Na próxima página, o usuário confirma que deseja cancelar ao clicar no botão "Não renovar".
* 4. O usuário volta ao passo 2 do fluxo principal.

#### FA02 - Não é umusuário Turbo nem membro do Amazon Prime, e nem reside nos Estados Unidos, México, Canadá, Itália, França, Alemanha, Bélgica, Áustria, Espanha, Japão, Singapura, Holanda ou Reino Unido.

* 1. O usuário cria uma conta na Amazon.
* 2. O usuário conecta a conta na Amazon a conta no Twitch.
* 3. O usuário é um Twitch Prime.

#### FA03 - Usuário atual membro do Prime Video, e não reside nos Estados Unidos, México, Canadá, Itália, França, Alemanha, Bélgica, Áustria, Espanha, Japão, Singapura, Holanda ou Reino Unido.

* 1. O usuário cria uma conta na Amazon.
* 2. O usuário acessa o Twitch Prime e clica em "Comece a sua avaliação gratuita" a para conectar a conta do Prime Video com a da Twitch.
* 3. Depois de conectado, é um Twich Prime.

#### FA04 - Usuário  não é membro do Amazon Prime nem membro do Amazon Prime Video, e não reside nos Estados Unidos, México, Canadá, Itália, França, Alemanha, Bélgica, Áustria, Espanha, Japão, Singapura, Holanda ou Reino Unido.

* 1. O usuário cria uma conta na Amazon Prime Video.
* 2. O usuário faz login na conta da Amazon.
* 3. O usuário faz login na conta do Twitch.
* 4. O usuário conecta a conta da Amazon a da Twitch.

### Fluxo de Exceção
* 1. O Usuário digita algum dado do cartão inválido na hora de cadastrar na Amazon (Erro ne negócio - deve ser tratado).
* 2. O usuário insere o login ou senha errados na hora do login (Erro de negócio).
* 3. O Usuário perde conexão com a internet.

## Pós-condição
* Não se aplica.