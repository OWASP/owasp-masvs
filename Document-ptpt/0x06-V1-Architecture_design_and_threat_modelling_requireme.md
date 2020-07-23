
# V1: Requisitos de Arquitetura, Desenho e Modelação de Ameaças

## Objetivo de controlo

Num mundo perfeito, a segurança deveria ser considerada em todas as fases de desenvolvimento. Mas na realidade a segurança é apenas considerada muitas vezes num estado tardio do SDLC. Para além dos controlos técnicos a MASVS requer que existam processos que garantam que a segurança foi tida em consideração na fase de planeamento da arquitetura da aplicação móvel e que os papéis de segurança de todos os componentes sejam conhecidos. Uma vez que a maioria das aplicações móveis funcionam como um cliente para serviços remotos, deve ser garantido que padrões de segurança são aplicados a esses serviços. Testar a aplicação de forma isolada não é suficiente.

A categoria "V1" lista requisitos pertencentes à arquitetura e desenho da aplicação. Como tal, esta é a única categoria que não tem correspondência com os casos de teste em OWASP Mobile Testing Guide. Para cobrir tópicos como modelação de ameaças, SDLC seguro ou gestão de chaves, os utilizadores da MASVS devem consultar os respetivos projetos e/ou padrões da OWASP, como os listados em baixo.

## Requisitos para verificações de segurança

Os requisitos para MASVS-L1 e MASVS-L2 estão listados em baixo.

| # | MSTG-ID | Descrição| L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **1.1** | MSTG-ARCH-1 | Todos os componentes da aplicação estão identificados e são necessários. | ✓ | ✓ |
| **1.2** | MSTG-ARCH-2 | Controlos de segurança nunca são forçados apenas no lado do cliente, mas também no respetivo ponto de acesso remoto. | ✓ | ✓ |
| **1.3** | MSTG-ARCH-3 | Uma arquitetura de alto nível para a aplicação móvel e todos os serviços remotos foi definida e a segurança foi endereçada nessa arquitetura. | ✓ | ✓ |
| **1.4** | MSTG-ARCH-4 | Informação considerada sensível no contexto da aplicação móvel está claramente identificada. | ✓ | ✓ |
| **1.5** | MSTG-ARCH-5 | Todos os componentes da aplicação estão definidos em termos de funções negócio e/ou funções de segurança que os mesmos providenciam. |  | ✓ |
| **1.6** | MSTG-ARCH-6 | Modelação de ameaças para a aplicação móvel e os serviços remotos associados que identifica potenciais ameaças e contramedidas foi produzido. |  | ✓ |
| **1.7** | MSTG-ARCH-7 | Todos os controlos de segurança têm uma implementação centralizada. |  | ✓ |
| **1.8** | MSTG-ARCH-8 | Existe uma política explicita de como chaves de criptografia (caso existam) são geridas, e o ciclo de vida das chaves de criptografia é imposto. O ideal é seguir um padrão para gestão de chaves, como o NIST SP 800-57. |  | ✓ |
| **1.9** | MSTG-ARCH-9 | Existe um mecanismo para impor atualizações da aplicação móvel. |  | ✓ |
| **1.10** | MSTG-ARCH-10 | Segurança é endereçada em todas as partes do ciclo de vida do software. |  | ✓ |
| **1.11** | MSTG-ARCH-11 | Uma política de divulgação responsável é usada e aplicada de forma efetiva. |  | ✓ |
| **1.12** | MSTG-ARCH-12 | A aplicação deverá ser compatível com leis de privacidade e regulações. | ✓ | ✓ |

## Referências

Para mais informação, ver também:

- OWASP Mobile Top 10: M10 (Extraneous Functionality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m10-extraneous-functionality>
- OWASP Threat modelling - <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet - <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL - <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57 - <http://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf>
- security.txt - <https://securitytxt.org/>
