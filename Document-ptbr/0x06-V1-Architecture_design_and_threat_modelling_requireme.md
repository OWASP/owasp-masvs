# V1: Requisitos de Arquitetura, Design e Modelagem de Ameaças

## Objetivo do Controle

Em um mundo perfeito, a segurança seria considerada em todas as fases do desenvolvimento. Na realidade, porém, a segurança geralmente é apenas uma consideração em uma fase tardia no SDLC. Além dos controles técnicos, o MASVS exige que os processos estejam em um local que garanta que a segurança tenha sido explicitamente abordada ao planejar a arquitetura do aplicativo móvel e que as funções funcionais e de segurança, de todos os componentes, sejam conhecidas. Como a maioria dos aplicativos móveis atua como clientes de serviços remotos, deve-se assegurar que os padrões de segurança adequados também são aplicadas a esses serviços, não bastando testar o aplicativo móvel isoladamente.

A categoria "V1" lista os requisitos referentes à arquitetura e _design_ do aplicativo. Como tal, esta é a única categoria que não é mapeada para casos de teste técnicos no _OWASP Mobile Testing Guide_. Para cobrir tópicos como modelagem de ameaças, SDLC seguro ou gerenciamento de chaves; os usuários do MASVS devem consultar os respectivos projetos da OWASP e/ou outros padrões, como os relacionados abaixo.

## Requisitos de Verificação de Segurança

Os requisitos para MASVS-L1 e MASVS-L2 estão listados abaixo.

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **1.1** | MSTG-ARCH-1 | Todos os componentes do aplicativo são identificados e conhecidos como necessários. | ✓ | ✓ |
| **1.2** | MSTG-ARCH-2 | Os controles de segurança nunca são aplicados apenas no lado do cliente, mas nos respectivos terminais remotos. | ✓ | ✓ |
| **1.3** | MSTG-ARCH-3 | Uma arquitetura de alto nível para o aplicativo móvel e todos os serviços remotos conectados foi definida e a segurança foi abordada nessa arquitetura. | ✓ | ✓ |
| **1.4** | MSTG-ARCH-4 | Os dados considerados confidenciais no contexto do aplicativo móvel são claramente identificados. | ✓ | ✓ |
| **1.5** | MSTG-ARCH-5 | Todos os componentes do aplicativo são definidos em termos das funções de negócios e/ou funções de segurança que eles fornecem. |   | ✓ |
| **1.6** | MSTG-ARCH-6 | Foram produzidos um modelo de ameaça para o aplicativo móvel e os serviços remotos associados, que identificam possíveis ameaças e contramedidas. |   | ✓ |
| **1.7** | MSTG-ARCH-7 | Todos os controles de segurança têm uma implementação centralizada. |   | ✓ |
| **1.8** | MSTG-ARCH-8 | Há uma política explícita sobre como as chaves criptográficas (se houver) são gerenciadas e como o ciclo de vida das chaves criptográficas é imposto. Idealmente, segue um padrão de gerenciamento de chaves como o NIST SP 800-57. |   | ✓ |
| **1.9** | MSTG-ARCH-9 | Existe um mecanismo para aplicar atualizações do aplicativo móvel. |   | ✓ |
| **1.10** | MSTG-ARCH-10 | A segurança é abordada em todas as partes do ciclo de vida de desenvolvimento de software. |   | ✓ |
| **1.11** | MSTG-ARCH-11 | Uma responsável política de divulgação está em vigor e é efetivamente aplicada. |   | ✓ |
| **1.12** | MSTG-ARCH-12 | O aplicativo deve estar em conformidade com as leis e regulamentos de privacidade. | ✓ | ✓ |

## Referências

Para mais informações, consulte também (em inglês):

- OWASP Mobile Top 10: M10 (Extraneous Functionality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m10-extraneous-functionality>
- OWASP Security Architecture cheat sheet - <https://www.owasp.org/index.php/Application_Security_Architecture_Cheat_Sheet>
- OWASP Threat modelling - <https://www.owasp.org/index.php/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet - <https://www.owasp.org/index.php/Secure_SDLC_Cheat_Sheet>
- Microsoft SDL - <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57 - <http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf>
- security.txt - <https://securitytxt.org/>
