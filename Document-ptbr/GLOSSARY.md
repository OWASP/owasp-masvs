# Apêndice A: Glossário

## Arquitetura de Segurança

Uma abstração do planejamento da aplicação que identifica e descreve onde e como os controles de segurança são usados, e também identifica e descreve a localização e sensibilidade dos dados do usuário e da aplicação.

## Autenticação SSO

Autenticação Única (*Single Sign-On* - SSO) ocorre quando um usuário se autentica em um Cliente e então é autenticado em outros Clientes automaticamente, independente da plataforma, tecnologia ou domínio que o usuário está utilizando. Por exemplo, quando você se autentica no Google você será autenticado automaticamente no YouTube, Docs e serviço de email.

## Autenticação

A verificação da identidade reclamada por um usuário da aplicação.

## *Bytecode* Java

*Bytecode* Java é um grupo de instruções da Máquina Virtual Java (JVM). Cada *bytecode* é composto por um, ou em alguns casos dois, *bytes* que representam uma instrução (*opcode*), junto com zero ou mais *bytes* para passagem de parâmetros.

## Certificado X.509

Um certificado X.509 é um certificado digital que utiliza o padrão globalmente reconhecido X.509 de Infraestrutura de Chave Pública (PKI) para verificar que uma chave pública pertence a um usuário, computador ou serviço identificado no certificado.

## Chaves *Hardcoded*

Chaves criptográficas que são armazenadas no próprio dispositivo.

## Código Malicioso

Código introduzido dentro da aplicação durante o seu desenvolvimento sem o consentimento do dono da aplicação, o qual contorna a política de segurança pretendida pela aplicação. Não é a mesma coisa que *malware*, vírus ou *worm*!

## Componente

Uma unidade de código autônoma, associada a um disco e a interfaces de rede que comunicam com outros componentes.

## Comunicação Entre Processos (IPC)

Em IPC os processos se comunicam uns com os outros e com o *kernel* para coordenar suas atividades.

## Configuração de Segurança

A configuração de execução de uma aplicação que afeta como os controles de segurança são utilizados.

## Controle de Segurança

Uma função ou componente que executa uma checagem de segurança (por exemplo, uma checagem de controle de acesso) ou quando chamado tem resultados com efeitos na segurança (por exemplo gerar um registro de auditoria).

## *Cross-Site Scripting* (XSS)

Uma vulnerabilidade de segurança tipicamente encontrada em aplicações *web*, permitindo a injeção de *scripts* no conteúdo do lado do cliente.

## CWE

CWE é uma lista desenvolvida de forma comunitária para falhas comuns de segurança. Ela serve como uma linguagem única, uma medida para ferramentas de segurança de *software* e como embasamento para identificação de falhas e esforços de mitigação e prevenção.

## Executável de Posição Independente (*Position Independent Executable* - PIE)

O PIE é um corpo de código de máquina que, sendo colocado em algum lugar da memória primária, executa corretamente independente do seu endereço absoluto.

## Identificador Único Global (GUID)

Um número único de referência utilizado como identificador em um *software*.

## Informação de Identificação Pessoal (*Personally Identifiable Information* - PII)

PII são informações que podem ser utilizadas sozinhas ou em conjunto com outras informações para identificar, contatar ou localizar uma pessoa específica, ou para identificar um único indivíduo dentro de determinado contexto.

## Infraestrutura de Chave Pública (PKI)

Uma PKI é um arranjo que liga chaves públicas com as respectivas identidades de entidades. A ligação é estabelecida através de um processo de registro e emissão de certificados em e por uma Autoridade Certificadora (CA).

## Injeção de SQL (SQLi)

Uma técnica de injeção de código usada para atacar aplicações orientadas a dados nas quais declarações SQL maliciosas são inseridas em um ponto de entrada.

## Lista Branca (*Whitelist*)

Uma lista de dados ou operações permitidas, por exemplo uma lista de caracteres que são aceitos em uma validação de entradas de usuário.

## *Malware*

Código executável que é introduzido em uma aplicação em execução sem o conhecimento do usuário ou administrador da aplicação.

## Modelagem de Ameaças (*Threat Modeling*)

Técnica que consiste em desenvolver arquiteturas de segurança cada vez mais refinadas a fim de identificar agentes de ameaça, zonas e controles de segurança, técnicas importantes e ativos de negócio.

## Módulo Criptográfico

*Hardware*, *software* e/ou *firmware* que implementa algoritmos criptográficos e/ou gera chaves criptográficas.

## *Projeto Aberto de Segurança de Aplicações *Web* (*Open Web Application Security Project* - OWASP)*

A OWASP é uma comunidade mundial livre e aberta focada na melhoria da segurança de aplicações de *software*. Nossa missão é tornar a segurança de aplicações "visível", então as pessoas e organizações poderão tomar decisões conscientes sobre os riscos de segurança de aplicações. Veja mais: <https://www.owasp.org/>.

## Protocolo de Transferência de Hipertexto (HTTP)

Um protocolo de aplicação para sistemas distribuídos, colaborativos e de informação de hipermídia. Ele é o fundamento para comunicação de dados na Rede Mundial (*World Wide Web* - WWW).

## Randomização de Layout de Espaço de Endereço (*Address Space Layout Randomization* - ASLR)

Uma técnica para tornar mais difícil a exploração de erros de corrupção da memória.

## Relatório de Verificação da Segurança de Aplicações

Um relatório que documenta os resultados gerais e dá suporte a análises produzidas pelo verificador para uma aplicação em particular.

## SDLC

Sigla para Ciclo de Desenvolvimento de *software* (*Software Development Life Cycle*).

## Segurança de Aplicações

Segurança em nível de aplicação foca na análise de componentes que fazem parte da camada de aplicação no Modelo de Referência de Interconexão de Sistemas Abertos (Modelo OSI), em vez de focar, por exemplo, no sistema operacional subjacente ou nas redes conectadas.

## Segurança de Camada de Transporte (*Transport Layer Security* - TLS)

Protocolos criptográficos que oferecem comunicação segura através da Internet.

## Teste Caixa Preta

É o método de teste de *software* que examina a funcionalidade de uma aplicação sem levar em conta suas estruturas ou funcionamentos internos.

## Teste de Aceitação de Usuário (UAT)

Tradicionalmente um ambiente de testes que se comporta como o ambiente produtivo onde todos os testes de *software* são realizados antes de irem para produção.

## Teste Dinâmico de Segurança de Aplicações (DAST)

Tecnologias DAST são desenhadas para detectar indicativos de condições para uma vulnerabilidade de segurança ocorrer em uma aplicação no seu estado funcional.

## Teste Estático de Segurança de Aplicações (SAST)

SAST é um grupo de tecnologias planejadas para analisar o código fonte, *bytecode* e binários de uma aplicação para identificar condições de codificação e planejamento que sejam indicativos de vulnerabilidades de segurança. Soluções SAST analisam a aplicação "de dentro para fora" em um estado de não-execução.

## URI e URL

Identificador de Recurso Uniforme (*Uniform Resource Identifier* - URI) é uma *string* de caracteres usada para identificar um nome ou recurso *web*. Um Localizador de Recurso Uniforme (*Uniform Resource Locator* - URL) é normalmente utilizado como uma referência a um recurso.

## Validação de Entradas

A sanitização e validação de entradas de usuário não-confiáveis.

## Verificação Automatizada

O uso de ferramentas automatizadas (tanto ferramentas de análise dinâmica, ferramentas de análise estática, quanto ambas) que usam assinaturas de vulnerabilidade para identificar problemas.

## Verificação de *Design*

Avaliação técnica da arquitetura de segurança de uma aplicação.

## Verificação de Segurança de Aplicações

Avaliação técnica de uma aplicação do ponto de vista do OWASP MASVS.

## Verificação Dinâmica

O uso de ferramentas automatizadas que usam assinaturas de vulnerabilidades para identificar problemas durante a execução de uma aplicação.

## Verificador

Pessoa ou time que está revisando uma aplicação de acordo com os requisitos OWASP MASVS.
