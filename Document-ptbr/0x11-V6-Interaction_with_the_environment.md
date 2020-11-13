# V6: Requisitos de Interação com a Plataforma

## Objetivo de Controle

Os controles deste grupo garantem que o aplicativo use APIs da plataforma e componentes padrão de forma segura. Além disso, os controles cobrem a comunicação entre aplicativos (IPC).

## Requisitos de Verificação de Segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | O aplicativo só solicita o conjunto mínimo de permissões necessárias. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | Todas as entradas de fontes externas e do usuário são validadas e, se necessário, sanitizadas. Isso inclui dados recebidos através da UI, mecanismos de IPC como intenções, URLs personalizados e origens pela rede.| ✓ | ✓ |
| **6.3** | MSTG-PLATAFORMA-3 | O aplicativo não exporta funcionalidades sensíveis através de esquemas de URL personalizado, a menos que esses mecanismos estejam devidamente protegidos. | ✓  |  ✓  |
| **6.4** | MSTG-PLATAFORMA-4 | O aplicativo não exporta funcionalidades sensíveis através do IPC, a menos que esses mecanismos estejam devidamente protegidos. | ✓  |  ✓  |
| **6.5** | MSTG-PLATAFORMA-5 | Código JavaScript é desativado nos _WebViews_, a menos que explicitamente necessário. | ✓  |  ✓  |
| **6.6** | MSTG-PLATAFORMA-6 | O _WebViews_ está configurado para permitir apenas o conjunto mínimo de manipuladores de protocolo necessários (preferencialmente, apenas https). Manipuladores potencialmente perigosos, como um arquivo, tel e app-id estão desabilitados. | ✓  |  ✓  |
| **6.7** | MSTG-PLATAFORMA-7 | Se os métodos nativos do aplicativo forem expostos a um _WebView_, verifique se o _WebView_ só renderiza o código JavaScript contido no pacote do aplicativo. | ✓  |  ✓  |
| **6.8** | MSTG-PLATAFORMA-8 | A desserialização de objetos, se houver, é implementada usando APIs de serialização seguras. | ✓  |  ✓  |
| **6.9** | MSTG-PLATAFORMA-9 | O aplicativo se protege contra ataques de sobreposição de tela. (somente para Android) |  | ✓  |
| **6.10** | MSTG-PLATAFORMA-10 | O _cache_, o armazenamento e os recursos carregados (JavaScript, etc.) devem ser eliminados antes que o _WebView_ seja destruído. |  | ✓  |
| **6.11** | MSTG-PLATAFORMA-11 | Verifique se o aplicativo impede o uso de teclados de terceiros personalizados sempre que dados confidenciais são inseridos. (somente para iOS) | | ✓  |

## References

O Guia de Teste de Segurança Móvel da OWASP fornece instruções detalhadas para verificar os requisitos listados nesta seção (em inglês).

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Para mais informações, veja (em inglês):

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
