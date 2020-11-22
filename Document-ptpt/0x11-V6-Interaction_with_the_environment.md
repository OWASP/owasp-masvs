# V6: Requisitos de Interacção com a plataforma

## Objetivo de Controlo

Os controlos neste grupo asseguram que a aplicação utiliza Interfaces de Programação da Aplicação (APIs) e componentes padrão. Adicionalmente é também abordada a comunicação entre aplicações (ICP).

## Requisitos para Verificação de Segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |

| **6.1** | MSTG-PLATFORM-1 | A aplicação apenas requer o conjunto mínimo de permissões necessárias. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | Quaisquer dados obtidos por fonte externa (utilizador e outros) são validados e, se necessário, sanitizados. Aqui estão incluídos quaisquer dados obtidos através de interface visual (UI), via comunicação inter-processos (IPC), incorporados nos localizadores de instâncias (URL), assim como por recursos de rede.| ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | A aplicação não exporta qualquer informação sensível via esquemas de localizadores de instâncias (URL) customizados, excepto nos casos em que esses mecanismos estão devidamente protegidos. | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | A aplicação não exporta qualquer informação sensível via comunicação inter-processos (IPC), excepto nos casos em que esses mecanismos estão devidamente protegidos. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | JavaScript está inactivo nas vistas da aplicação excepto nos casos em que é estritamente necessário. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | As vistas da aplicação estão configuradas de forma a suportar o número mínimo de protocolos , idealmente só https deve ser suportado.  Potentially dangerous handlers, such as file, tel and app-id, are disabled. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | Se métodos nativos da aplicação estarem expostos na vista web, verificar que esta apenas renderiza o JavaScript contido na aplicação. | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | A deserialização de objectos, se necessária, é implementada através do uso de interfaces (APIs) de serialização seguras. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | A aplicação protege-se contra ataques de sobreposição de ecrãs. (Apenas em Android) |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | A cache da vista web, o armazenamento e os recursos utilizados (JavaScript, etc.) devem ser limpos antes da destruição da vista web. |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | Verificar que a aplicação previne o uso de teclados externos customizados, nos casos em que informação sensivel é inserida. | | ✓ |

## Referências

O OWASP Mobile Security Testing Guide providencia instruções detalhadas para verificação dos requisitos listados nesta secção.

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Para mais informação:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>
