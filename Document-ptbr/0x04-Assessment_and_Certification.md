# Avaliação e Certificação

## Posição da OWASP sobre Certificações e Marcas de Confiança do MASVS

A OWASP, como uma organização neutra e sem fins lucrativos, não certifica nenhum fornecedor, testador ou _software_.

Todas essas afirmações de garantia, marcas de confiança ou certificações não são oficialmente examinadas, registradas ou certificadas pela OWASP. Portanto, uma organização que dependa de tal visão precisa ser cautelosa com a confiança depositada em qualquer órgão terceirizado ou certificado de confiança (M)ASVS.

Isso não deve dificultar as organizações de oferecer tais serviços de garantia, desde que não reivindiquem a certificação Oficial OWASP.

## Orientação para Certificação de Aplicativos Móveis

A maneira recomendada de verificar a conformidade de um aplicativo móvel com o MASVS é realizando uma revisão do tipo "_open book_", o que significa que os testadores têm acesso a recursos-chave, como arquitetos e desenvolvedores do aplicativo, documentação do projeto, código-fonte e acesso autenticado a terminais, incluindo acesso a pelo menos uma conta de usuário para cada função.

É importante notar que o MASVS abrange apenas a segurança do aplicativo móvel (lado do cliente) e a comunicação de rede entre o aplicativo e seus terminais remotos, bem como alguns requisitos básicos e genéricos relacionados à autenticação do usuário e gerenciamento de sessões. Ele não contém requisitos específicos para os serviços remotos (por exemplo, serviços _web_) associados ao aplicativo, além de um conjunto limitado de requisitos genéricos relativos à autorização, autenticação, verificação de controle e gerenciamento de sessões. No entanto, o MASVS V1 especifica que os serviços remotos devem estar seguros usando o modelo global de ameaças e devem ser analisados em relação à utilização dos padrões apropriados como o OWASP ASVS.

Uma organização certificadora deve incluir em qualquer relatório o escopo da verificação (particularmente se um componente-chave estiver fora do escopo), um resumo dos resultados de verificação, incluindo testes aprovados e reprovados, com indicações claras de como corrigir os testes em que houve falha. Manter documentação detalhada, captura de tela ou vídeo, _scripts_ para explorar de forma confiável e repetidamente um problema e registros eletrônicos de testes, como interceptar registros de _logs_ de um _proxy_ e notas associadas, como uma lista de limpeza, é considerada prática padrão do setor. Não basta simplesmente executar uma ferramenta e relatar as falhas; isso não fornece evidências suficientes de que todas as questões em nível de certificação foram testadas e testadas minuciosamente. Em caso de contestação, deve haver evidências suficientes para demonstrar que todos os requisitos verificados foram de fato testados.

<!-- \pagebreak -->

### Usando o Guia de Testes de Segurança Móvel (MSTG) da OWASP

O OWASP MSTG é um manual para testar a segurança dos aplicativos móveis. Descreve os processos técnicos para verificar os requisitos listados no MASVS. O MSTG inclui uma lista de casos de teste, cada um dos quais mapeia para um requisito no MASVS. Embora os requisitos do MASVS sejam de alto nível e genéricos, o MSTG fornece recomendações e procedimentos de teste em profundidade por sistema operacional móvel.

### O papel das Ferramentas Automatizadas de Teste de Segurança

O uso de escâneres de código-fonte e ferramentas de teste de caixa preta é incentivado a fim de aumentar a eficiência, sempre que possível. No entanto, não é possível concluir a verificação do MASVS usando apenas ferramentas automatizadas: cada aplicativo móvel é diferente e entender a arquitetura geral, a lógica de negócios e os artifícios técnicos das tecnologias e _frameworks_ específicos que estão sendo usados é um requisito obrigatório para verificar a segurança do aplicativo.

## Outros Usos

### Como Orientação Detalhada da Arquitetura de Segurança

Um dos usos mais comuns para o Padrão de Verificação de Segurança de Aplicativos Móveis é a utilização como um recurso para arquitetos de segurança. As duas principais estruturas de arquitetura de segurança, SABSA ou TOGAF, carecem de uma grande quantidade de informações necessárias para concluir as avaliações de arquitetura de segurança de aplicativos móveis. O MASVS pode ser usado para preencher essas lacunas, permitindo que arquitetos de segurança escolham melhores controles para problemas comuns em aplicativos móveis.

### Como Substituto para _Checklists_ de Desenvolvimento Seguro de Aplicativos Móveis

Muitas organizações podem se beneficiar da adoção do MASVS, escolhendo um dos dois níveis, ou fazendo seu próprio _fork_ do MASVS e alterando o que for necessário para o contexto e o nível de risco de cada aplicativo. Nós estimulamos esse tipo de _fork_ enquanto a rastreabilidade for mantida, de modo que se um aplicativo cumprir o requisito 4.1, o mesmo ocorra nos _forks_ do padrão à medida que ele evolui.

### Como Base para Metodologias de Testes de Segurança

Uma boa metodologia de teste de segurança de aplicativos móveis deve cobrir todos os requisitos listados no MASVS. O Guia de Teste de Segurança Móvel OWASP (MSTG) descreve os casos de teste de caixa preta e caixa branca para cada requisito de verificação.

### Como Guia para Testes Automatizados de Unidade e Integração

O MASVS foi projetado para ser altamente testável, com a única exceção dos requisitos de arquitetura. Os testes automatizados unitários, integração e aceitação com base nos requisitos do MASVS podem ser integrados ao ciclo de vida de desenvolvimento contínuo. Isso não só aumenta a consciência de segurança do desenvolvedor, mas também melhora a qualidade geral dos aplicativos resultantes e reduz a quantidade de descobertas durante os testes de segurança na fase prévia ao _release_.

### Para Treinamento de Desenvolvimento Seguro

O MASVS também pode ser usado para definir características de aplicativos móveis seguros. Muitos cursos de "desenvolvimento seguro" são simplesmente cursos de _ethical hacking_ com poucas dicas de codificação segura. Isso não ajuda os desenvolvedores. Em vez disso, cursos de desenvolvimento seguro podem usar o MASVS, com um forte foco nos controles proativos documentados no MASVS, em vez de, por exemplo, os 10 principais problemas de segurança de desenvolvimento.
