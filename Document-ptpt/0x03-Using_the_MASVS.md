# O Mobile Application Security Verification Standard

O MASVS pode ser usado para estabelecer um nível de confiança na segurança de aplicações móveis. Os requisitos foram estabelecidos tendo em conta os seguintes objetivos:

- Usar como uma métrica - Para providenciar um padrão de segurança com o qual as aplicações móveis podem ser comparadas pelos programadores e proprietários das aplicações;
- Usar como um guia - Para orientar durante todas as fases de desenvolvimento e teste das aplicações móveis;
- Usar durante o aprovisionamento - Para fornecer um ponto de partida para a verificação da segurança das aplicações móveis.

## Modelo de Segurança em Aplicações Móveis

O MASVS define dois níveis de verificação de segurança (MASVS-L1 e MASVS-L2), bem como um conjunto de requisitos de resiliência de engenharia reversa (MASVS-R). O MASVS-L1 contém requisitos de segurança genéricos recomendados para todas as aplicações móveis, enquanto que o MASVS-L2 deve ser aplicado a aplicações que lidam com dados extremamente sensíveis. O MASVS-R cobre os controlos de proteção adicional que podem ser aplicados para prevenir vulnerabilidades do lado do cliente, caso isso seja um objectivo.

Cumprir os requisitos em MASVS-L1 resulta numa aplicação segura que segue as melhores práticas de segurança e que não sofre vulnerabilidades comuns. o MASVS-L2 adiciona controlos para uma maior profundidade na defesa como SSL pinning, que resulta numa aplicação resiliente contra ataques mais sofisticados - assumindo que os controlos de segurança do sistema operativo móvel estão intactos e que o utilizador final não é visto como um potencial adversário. Satisfazer todos os requsitos de proteção do software em MASVS-R, ou subgrupos, ajuda a impedir riscos especificos nos quais o utilzador final é malicioso e/ou o sistema operativo móvel está comprometido.

**I: Ainda que a nossa recomendação seja implementar os controlos MASVS-L1 em todas as aplicações, aplicar um controlo efectivamente ou não deverá ser em último caso uma decisão baseada no risco, que é decidida/comunicada com os seus proprietários.**

**II: De notar que os controlos de proteção de software listados em MASVS-R e descritos no OWASP Mobile Security Testing Guide podem em última instância ser contornados e nunca ser usados como substitutos para os controlos de segurança. Em vez disso, eles têm como propósito adicionarameças controlos de proteção a ameaças específicas em aplicações que também cumpram os requistos MASVS em MASVS-L1 e MASVS-L2.**

<img src="images/masvs-levels-new.jpg" title="Níveis de Verificação" width="600px" height="253px" />

### Estrutura do Documento

A primeira parte do MASVS contaem uma descrição do modelo de segurança e respectivos níveis de verificaçãos disponiveis, seguido de recomendações acerca da utilização do modelo na prática.  Os requisitos de segurança detalhados, bem como o mapeamento com os níveis de verificação, estão listados na segunda parte. Os requsitos foram agrupados em oito categorias (V1 ao V8) consoante os objectivos tecnicos e o âmbito. A seguinte numencatura é usada ao longo do MASVS e do MSTG:

- *Categoria do requisito:* MASVS-Vx, ex MASVS-V2: Armazenamento de dados e privacidade
- *Requisito:* MASVS-Vx.y, ex MASVS-V2.2: "Nenhuma informação sensível está a ser escrita nos logs."  

### Níveis de Verificação em Detalhe

#### MASVS-L1: Padrão de Segurança

Uma apllicação móvel que atinga o MASVS-L1 aceita as melhores práticas de segurança. Preenche requisitos básicos em termos de qualidade de código, tratamento de informação sensível, e interação com o ambiente móvel. Deve ser implementado um processo de teste para verificar os controlos de segurança. Este nível é apropriado para todas as aplicações móveis.

#### MASVS-L2: Defesa em Profundidade

O nível MASVS-L2 introduz controlos de segurança avançados que vão para além dos requisitos padrão. Para estar em concordância com o MASVS-L2, deve existir um modelo de ataque e a segurança deve ser parte integral da arquitetura e desenho da aplicação. Baseado no modelo de ataque, devem ser escolhidos os controlos MASVS-L2 corretos e implementados com sucesso. Este nível é apropriado para aplicações que lidam com grandes volumes de dados sensíveis, como aplicações bancárias.

#### MASVS-R: Resiliência Contra Engenharia Reversa e Adulteração

A aplicação tem segurança de ponta, e também é resiliente contra ataques específicos e claramente definidos do lado do cliente, como adulteração, alteração da aparência ou engenharia reversa para extrair código ou informação sensivel. Uma aplicação deste género ou deverá possuir recursos de hardware de segurança ou técnicas de proteção suficientemente fortes e verificáveis. O MASVS-R é extensível a todas as aplicações que lidam com grandes volumes de dados sensíveis e podem servir como um meio de proteção de propriedade intelectual ou tornar uma aplicação inviolável.

### Uso Recomendado

As aplicações podem ser testadas para MASVS L1 ou L2 com base numa avaliação de risco e no nível global de segurança requerido. O nível L1 é aplicável a todas as aplicações móveis, enquanto que o L2 é recomendado em geral para aplicações que operam com dados ou fincionalidades mais sensivéis. Os MASVS-R(ou uma parte deles) podem ser aplicados para verificar resiliência contra ameaças especificas, como reempacotar a aplicação ou extrair dados sensiveis, *em adição* a verificação de segurança apropriada.

Em resumo, estão disponíveis os seguintes tipos de verificação:

- MASVS-L1
- MASVS-L1+R
- MASVS-L2
- MASVS-L2+R

As diferentes combinações refletem diferentes níveis de segurança e resiliência. O objetivo é permitir flexibilidade: por exemplo, um jogo de télemovel pode não justificar a adição dos controlos de segurança de MASVS-L2, como a verificação de dois fatores, por razões de usabilidade, mas ter uma forte necessidade comercial de prevenção de falsificação.

#### Que Tipo de Verificação Escolher

Implementar os requisitos do MASVS L2 aumenta a segurança, enquanto que ao mesmo tempo aumenta o custo de desenvolvimento e diminui potencialmente a usabilidade para o utilizador final (o clássico conflito de escolha). Em geral, o L2 deve ser usado para aplicaçãos sempre que faça sentido do ponto de vista risco *versus* perpectiva de custo (ex quando a potencial perda causada pelo compromisso de confidencialidade ou integridade é maior que o custo incorrido pelos adicionais controlos de segurança). Uma avaliação do risco deve ser o primeiro passo antes de aplicar o MASVS.

##### Exemplos

###### MASVS-L1

- Todas as aplicações móveis. O MASVS-L1 lista as melhores práticas de segurança que podem ser seguidas com um impacto razoável no custo do desenvolvimento e na experiência do utilizador. Aplique os requisitos em MASVS-L1 para qualquer aplicação que não se qualificar para um dos níveis mais altos.

<!-- \pagebreak -->

###### MASVS-L2

- Indústria da Saúde: aplicações móveis que guardam informação pessoal e identificável que pode ser usada para roubo de identidade, pagamentos fraudulentos, ou uma variedade de esquemas fraudulentos. Para o sector da saúde dos Estados Unidos, considerações de conformidade incluem a Health Insurance Portability and Accountability Act (HIPAA), Privacidade, Segurança, Regras de Notificações em Caso de Brecha e Regras de Segurança do Utente.

- Indústria Financeira: aplicações que permitem o acesso a informação altamente sensível como números de cartão de crédito, informação pessoal, ou permitem aos utilizadores movimentar fundos. Estas aplicações garantem controlos de segurança adicionais para prevenir fraude. Aplicações financeiras precisam de assegurar conformidade com o Payment Card Industry Data Security Standard (PCI DSS), Gramm Leech Bliley Act e Sarbanes-Oxley Act (SOX).

###### MASVS L1+R

- Aplicações móveis em que a proteção da Propriedade Intelectual é um objetivo de negócio. Os controlos de resiliência listados na MASVS-R podem ser usados para aumentar o esforço necessário para obter o código-fonte original e para impedir a adulteração/quebra do sistema.

- Indústria dos jogos: jogos com um objetivo essencial de prevenir alteração visual ou fazer batota, como jogos de competição online. Fazer batota é um problema importante em jogos online, sendo que um número elevado de batoteiros leva a que os jogadores fiquem descontentes e em última instância poderá levar a que o jogo falhe. O MASVS-R providencia controlos de anti-falsificação básicos que ajudam a aumentar o esforço dos batoteiros.

###### MASVS L2+R

- Indústria Financeira: aplicações online de bancos que permitem a movimentação de fundos, onde técnicas como injecção de código e instrumentalização em equipamentos comprometidos representam um risco. Neste caso, os controlos do MASVS-R podem ser usados pra impedir a adulteração, aumentando a fasquia para autores de malware.

- Todas as aplicações móveis que, propositadamente, necessitem de guardar dados sensíveis no equipamento móvel, e ao mesmo tempo suportam um leque alargado de equipamentos e versões do sistema operativo. Neste caso, os controlos de resiliência podem ser usados como uma medida da defesa em profundidade para aumentar o esforço para atacantes que queiram extrair dados sensíveis.

- Aplicações que incluem compras de serviços no seu interior devem usar controloes no lado do servidor e controlos MASVS-L2 para proteger conteúdo pago. Contudo, poderão haver casos em que não haja possibilidade de proteção no lado do servidor. Nestes casos, os controlos MASVS-R devem ser aplicados adicionalmente para aumentar o esforço da engenharia reversa e adulteração.
