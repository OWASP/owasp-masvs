
# Avaliação e Certificação

## A posição da OWASP sobre certificações MASVS e marcas de confiança

A OWASP, como organização sem fins lucrativos e neutra não certifica nenhuma empresa, nem verifica software.

Todo o tipo de confirmações de garantias, marcas de confiança ou certificados não são oficialmente verificados, registados, ou certificados  pela OWASP, por isso uma organização dependente de tal visão tem de ter cuidado com a confiança depositada em qualquer terceiro ou marca de confiança reivindicando certificação (M)ASVS .

Isto não deve de inibir organizações de garantir tais serviços de garantias, desde que estes não afirmem ser uma certificação oficial da OWASP.

## Orientação para Certificar Aplicações Móveis

A maneira recomendada de verificar a conformidade de uma aplicação movel com o MASVS é executando uma revisão de "livro aberto", querendo isto dizer que é dado acesso aos testers a recursos chave tais como arquitetos e programadores da aplicação, documentação do projeto, código fonte, acesso autenticado aos pontos de acesso, incluindo acesso a pelo menos uma conta de utilizador por cada função (role).

É importante de notar que o MASVS apenas cobre a segurança da aplicação movel (lado do cliente) e da comunicação de rede entre a aplicação e os seus pontos de acesso remotos, assim como alguns requisitos básicos e genéricos relacionados com autenticação do utilizador e gestão de sessão.  Não contem requisitos específicos para serviços remotos (ex: web services) associados à aplicação para além de um conjunto limitado de requisitos genéricos relacionados com autorização, autenticação, verificação de controlo e gestão de sessão. Contudo, MASVS V1 especifica que serviços remotos devem de ser abrangidos pelo documento de modelo de ameaças (Threat Modeling) e ser verificado contra padrões apropriados, como o OWASP ASVS.

Uma organização certificadora deve de incluir em qualquer relatório o âmbito da verificação (especialmente se algum componente chave é deixado de fora do âmbito), um sumario das descobertas da verificação, incluindo testes que passaram e falharam, com claras indicações de como resolver os testes que falharam. Manter documentos detalhados do trabalho, capturas de tela, ou vídeos, scripts para de forma fiel e repetitiva explorar um problema, e registos eletrónicos dos testes, como registos de intercessão de um proxy e notas associadas, como uma lista limpa, são consideradas boas praticas padrão da industria. Não é suficiente correr simplesmente uma ferramenta e reportar as falhas. Isto não fornece provas suficientes que todos os possíveis problemas de um nível a ser certificado foram testados ou testados exaustivamente. Em caso de disputa, deve de haver um suporte de provas suficientes para demonstrar que todos os requisitos verificados foram de facto testados.

<!-- \pagebreak -->

### Usar o OWASP Mobile Security Testing Guide (MSTG)

O OWASP MSTG é um manual para testar a segurança de aplicações moveis. Descreve os processos técnicos para verificar os requisitos listados em MASVS. O MSTG inclui uma lista de casos de teste, cada um que corresponde a um requisito no MASVS. Enquanto que os requisitos do MASVS são de alto nível e genéricos, o MSTG fornece recomendações extensivas e procedimentos de testes separados por Sistema Operativo.

### O Papel de Ferramentas de Testes de Segurança Automáticas

O uso de scanners de código fonte e ferramentas de caixa preta é encorajado de forma a aumentar a eficiência sempre que possível. Não é, no entanto, possível completar a verificação MASVS usando apenas ferramentas automatizadas:

Cada aplicação movel é diferente, e perceber a arquitetura no geral, logica de negócio e problemas técnicos das tecnologias e linguagens especificas usadas é um requisito obrigatório para verificar a segurança da aplicação.

## Outros usos

### Como Orientação Detalhada da Arquitetura de Segurança

Um dos usos mais comuns para Mobile Application Security Verification Standard é como um recurso para arquitetos de segurança. As duas maiores frameworks de arquitetura de segurança, SABSA ou TOGAF, tem uma grande falta de informação que é necessária para completar revisões de arquitetura de segurança de aplicações moveis. O MASVS pode ser usado para preencher essas falhas, permitindo aos arquitetos de segurança escolher melhores controlos para problemas comuns em aplicações moveis.

### Como um Substituto a Checklists de Código Seguro Prontas a Usar

Muitas organizações podem beneficiar da adoção do MASVS, escolhendo um de dois níveis, ou por criar um fork do MASVS e mudar o que é preciso para cada nível de risco da aplicação num domínio especifico. Nós encorajamos este tipo de fork desde que o rastreamento seja mantido, de forma a que uma aplicação que passou no requisito 4.1 signifique o mesmo para as versões dos forks, à medida que o padrão evolui.

### Como uma Base para Metodologias de Testes de Segurança

Uma boa metodologia de testes de segurança de aplicações moveis deve cobrir todos os requisitos listados em MASVS. O OWASP Mobile Security Testing Guide (MSTG) descreve testes de caixa preta e caixa branca para cada requisito de verificação.

### Como um Guia para Testes Unitários e de Integração Automáticos

O MASVS foi desenhado para ser altamente testável, com a única exceção de requisitos de arquitetura. Testes unitários, de integração e de aceitação automatizados baseados nos requisitos do MASVS podem ser integrados no ciclo continuo de desenvolvimento. Isto não só aumenta a consciência de segurança do programador, mas também melhora a qualidade geral das aplicações resultantes e reduz o numero de descobertas durante testes de segurança na fase antes do lançamento.

### Para Treino de Desenvolvimento Seguro

O MASVS pode também ser usado para definir características de segurança de aplicações moveis. Muitos cursos de "Programação segura" são apenas cursos de hacking ético com um pequeno ponto de dicas de programação. Isto não ajuda os programadores. Em vez disso, cursos de desenvolvimento seguro podem usar o MASVS com um forte foco nos controlos proactivos documentados no MASVS, em vez de por exemplo o Top 10 de problemas de segurança.