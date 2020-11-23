# V7: Requisitos de Qualidade de Codigo e Distribuição

## Objetivo de Controlo

O objetivo deste controlo é garantir que as práticas básicas de segurança em programação são cumpridas ao longo do desenvolvimento da aplicação, e que os recursos de segurança “gratuitos” oferecidos pelo compilador são ativados.

## Verificação de Requisitos de Segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | A aplicação é fornecida e assinada com um certificado válido, do qual a chave privada se encontra devidamente protegida. | ✓ | ✓ |
| **7.2** | MSTG-CODE-2 | A aplicação é desenvolvida em modo de distribuição, com configurações apropriadas para a implementação de uma nova versão de produção (ex. não depurável). | ✓ | ✓ |
| **7.3** | MSTG-CODE-3 | Os símbolos de depuração são removidos dos binários nativos. | ✓ | ✓ |
| **7.4** | MSTG-CODE-4 | Código de depuração e código de assistência ao programador (ex. código de teste, conteúdo secreto, configurações ocultas) são removidos. A aplicação não regista mensagens de erro detalhadas ou de depuração. | ✓ | ✓ |
| **7.5** | MSTG-CODE-5 | Todos os componentes de terceiros usados pela aplicação móvel, como bibliotecas e frameworks, são identificados e analisados para deteção de vulnerabilidades conhecidas. | ✓ | ✓ |
| **7.6** | MSTG-CODE-6 | A aplicação identifica e trata possíveis exceções. | ✓ | ✓ |
| **7.7** | MSTG-CODE-7 | A lógica de tratamento de erros em controlos de segurança, nega o acesso por defeito. | ✓ | ✓ |
| **7.8** | MSTG-CODE-8 | Em código não administrado, a memória é alocada, libertada e usada de forma segura. | ✓ | ✓ |
| **7.9** | MSTG-CODE-9 | Recursos de segurança gratuitos oferecidos pelo conjunto de ferramentas de programação, como minificação de bytes de código, proteção da pilha (stack), suporte ao PIE e contagem automática de referência, são ativados. | ✓ | ✓ |

## Referências

O OWASP Mobile Security Testing Guide providencia instruções detalhadas para verificação dos requisitos acima listados.

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Para mais informação, consulte:

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
