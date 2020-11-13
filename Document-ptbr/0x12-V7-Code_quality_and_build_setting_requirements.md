# V7: Requisitos de Qualidade de Código e Configuração do Compilador

## Objetivo do Controle

O objetivo deste controle é garantir que práticas básicas de codificação segura são seguidas no desenvolvimento do aplicativo móvel e que as funcionalidades de segurança "gratuitas" do compilador estão habilitadas.

## Requisitos de Verificação de Segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | O aplicativo é assinado e disponibilizado com um certificado válido e cuja chave privada está devidamente protegida. | ✓ | ✓ |
| **7.2** | MSTG-CODE-2 | O aplicativo foi criado em modo de _release_ e com as configurações apropriadas para ela (ex.: _non-debuggable_). | ✓ | ✓ |
| **7.3** | MSTG-CODE-3 | Os símbolos de depuração foram removidos dos binários nativos. | ✓ | ✓ |
| **7.4** | MSTG-CODE-4 | Todo código de depuração e de assistência ao desenvolvedor (ex.: código de teste, _backdoors_, configurações ocultas) deve ser eliminado. O aplicativo não tem logs detalhados de erros e nem mensagens de depuração. | ✓ | ✓ |
| **7.5** | MSTG-CODE-5 | Todos componentes de terceiros utilizados pelo aplicativo móvel, como blibliotecas e _frameworks_, são identificados e revisados quanto às vulnerabilidades conhecidas. | ✓ | ✓ |
| **7.6** | MSTG-CODE-6 | O aplicativo captura e trata devidamente as possíveis exceções. | ✓ | ✓ |
| **7.7** | MSTG-CODE-7 | Os controles de segurança não permitem acesso por padrão no tratamento de erros. | ✓ | ✓ |
| **7.8** | MSTG-CODE-8 | No código não gerenciado a memória é alocada, liberada e usada com segurança.  | ✓ | ✓ |
| **7.9** | MSTG-CODE-9 | As funcionalidades de segurança gratuitas das ferramentas, tais como minificação do _byte-code_, proteção de pilha, suporte PIE e contagem automática de referência, devem estar habilitadas. | ✓ | ✓ |

## Referências

O Guia de Teste de Segurança de Dispositivos Móveis do OWASP disponibiliza instruções detalhadas para verificar os requisitos listados nesta seção (em inglês).

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Para mais informações, veja também (em inglês):

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
