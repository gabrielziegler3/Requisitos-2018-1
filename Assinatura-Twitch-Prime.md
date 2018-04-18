# UC13 - Assinatura Twitch Prime

## Descrição
* Este caso de uso descreve a assinatura no Twitch Prime.
* O Twitch Prime é uma experiência Premium da Twitch que vem em uma inscrição Amazon Prime ou Amazon Prime Video. O Twitch Prime inclui jogos e conteúdos de jogos, inscrição de canal a cada 30 dias sem custo adicional, que pode ser usada em qualquer canal de Parceiro ou Afiliado, visualização sem anúncios na Twitch, emotes exclusivos e distintivo de bate-papo.

## Atores
* Usuário Twitch
* Parceiro ou afiliado

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

#### FA02 - Usuário atual membro do Prime Video, e não reside nos Estados Unidos, México, Canadá, Itália, França, Alemanha, Bélgica, Áustria, Espanha, Japão, Singapura, Holanda ou Reino Unido.

* 1. O usuário cria uma conta na Amazon.
* 2. O usuário acessa o Twitch Prime e clica em "Comece a sua avaliação gratuit" a para conectar a conta do Prime Video com a da Twitch.
* 3. Depois de conectado, é um Twich Prime.

### Fluxo de Exceção

## Pós-condição