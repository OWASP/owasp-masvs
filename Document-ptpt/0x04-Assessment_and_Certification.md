
# Avaliação e Certificação

## A posição da OWASP sobre certificações MASVS e marcas de confiança

A OWASP, como organização sem fins lucrativos e neutra não certifica nenhuma empresa, nem verifica software.

Todo o tipo de confirmações de garantias, marcas de confiança ou certificados não são oficialmente verificados, registados, ou certificados  pela OWASP, por isso uma organização dependente de tal visão tem de ter cuidado com a confiança depositada em qualquer terceiro ou marca de confiança reivindicando certificação (M)ASVS .

Isto não deve inibir organizações de garantirem tais serviços de garantias, desde que não afirmem ser uma certificação oficial da OWASP.

## Orientação para Certificar Aplicações Móveis

A maneira recomendada de verificar a conformidade de uma aplicação móvel com o MASVS é executando uma revisão de "livro aberto", querendo isto dizer que é dado acesso aos testers a recursos chave tais como arquitetos e programadores da aplicação, documentação do projeto, código fonte, acesso autenticado aos pontos de acesso, incluindo acesso a pelo menos uma conta de utilizador por cada função (role).

É importante notar que o MASVS apenas cobre a segurança da aplicação móvel (lado do cliente) e da comunicação de rede entre a aplicação e os seus pontos de acesso remotos, assim como alguns requisitos básicos e genéricos relacionados com autenticação do utilizador e gestão de sessão.  Isso nao inclui requisitos específicos para serviços remotos (ex: web services) associados à aplicação para além de um conjunto limitado de requisitos genéricos relacionados com autorização, autenticação, verificação de controlo e gestão de sessão. Contudo, MASVS V1 especifica que serviços remotos devem ser abrangidos pelo documento de modelo de ameaças (Threat Modeling) e ser verificados contra padrões apropriados, como o OWASP ASVS.

Uma organização certificadora deve incluir em qualquer relatório o âmbito da verificação (especialmente se algum componente chave é deixado de fora do âmbito), um sumário dos resultados da verificação, incluindo testes que passaram e falharam, com claras indicações de como resolver os testes que falharam. Manter documentos detalhados do trabalho, capturas de ecrã ou vídeos, scripts para explorar um problema de forma fiável e repetitiva, e registos eletrónicos dos testes, tais como registos de interceção de um proxy e notas associadas como uma lista de organização, são consideradas boas práticas padrão da indústria. Não é suficiente simplesmente correr uma ferramenta e reportar as falhas. Isto não fornece provas suficientes de que todos os possíveis problemas a um nível da certificação foram testados exaustivamente. Em caso de disputa, deve haver um suporte de provas suficientes para demonstrar que todos os requisitos verificados foram de facto testados.

<!-- \pagebreak -->

### Usando o OWASP Mobile Security Testing Guide (MSTG)

O OWASP MSTG é um manual para testar a segurança de aplicações móveis. Descreve os processos técnicos para verificar os requisitos listados em MASVS. O MSTG inclui uma lista de casos de teste, cada um que corresponde a um requisito no MASVS. Enquanto que os requisitos do MASVS são de alto nível e genéricos, o MSTG fornece recomendações extensivas e procedimentos de testes separados por Sistema Operativo.

### O Papel de Ferramentas de Testes de Segurança Automáticas

O uso de scanners de código fonte e ferramentas de blackbox é aconselhado de forma a aumentar a eficiência sempre que possível. Não é, no entanto, possível completar a verificação MASVS usando apenas ferramentas automatizadas:

Cada aplicação móvel é diferente, e perceber a arquitetura no geral, lógica de negócio, e problemas técnicos das tecnologias e frameworks específicas usadas, é um requisito obrigatório para verificar a segurança da aplicação.

## Outros usos

### Como Orientação Detalhada da Arquitetura de Segurança

Um dos usos mais comuns para Mobile Application Security Verification Standard é como um recurso para arquitetos de segurança. As duas maiores frameworks de arquitetura de segurança, SABSA ou TOGAF, têm uma grande falta de informação que é necessária para completar revisões de arquitetura de segurança de aplicações móveis. O MASVS pode ser usado para preencher essas falhas, permitindo aos arquitetos de segurança escolher melhores controlos para problemas comuns em aplicações móveis.

### Como um Substituto a Listas de Verificação de Código Seguro Prontas a Usar

Muitas organizações podem beneficiar da adoção do MASVS, escolhendo um de dois níveis, ou criando um fork do MASVS e mudando o que é preciso para cada nível de risco da aplicação num domínio específico. Nós aconselhamos este tipo de fork desde que o rastreamento seja mantido, de forma a que se a aplicação passar no requisito 4.1, isso signifique o mesmo para os forks copiados, à medida que o padrão evolui.

### Como uma Base para Metodologias de Testes de Segurança

Uma boa metodologia de testes de segurança de aplicações móveis deve cobrir todos os requisitos listados em MASVS. O OWASP Mobile Security Testing Guide (MSTG) descreve testes de baclbox e whitebox para cada requisito de verificação.

### Como um Guia para Testes Unitários e de Integração Automáticos

O MASVS foi desenhado para ser altamente testável, com a única exceção de requisitos de arquitetura. Testes automatizados, unitários, de integração e de aceitação, baseados nos requisitos do MASVS podem ser integrados no ciclo contínuo de desenvolvimento. Isto não só aumenta a consciência de segurança do programador, como também melhora a qualidade geral das aplicações resultantes e reduz o número de resultados durante testes de segurança na fase anterior ao lançamento de versão.

### Para Treino de Desenvolvimento Seguro

O MASVS pode também ser usado para definir características de segurança de aplicações móveis. Muitos cursos de "Programação segura" são apenas cursos de hacking ético com uma pequena amostra de dicas de programação. Isto não ajuda os programadores. Em vez disso, cursos de desenvolvimento seguro podem usar o MASVS com um forte foco nos controlos proactivos documentados no MASVS, em vez de por exemplo o Top 10 de problemas de segurança.
