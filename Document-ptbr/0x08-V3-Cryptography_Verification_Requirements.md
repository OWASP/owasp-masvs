# V3: Requisitos de Criptografia

## Objetivo do Controle

A criptografia é um componente essencial quando se trata da proteção dos dados armazenados em dispositivos móveis. É também uma categoria em que as coisas podem dar muito errado, especialmente quando as convenções e padrões não são seguidos. O objetivo dos controles neste capítulo é garantir que o aplicativo verificado use a criptografia de acordo com as melhores práticas do setor, incluindo:

- Uso de bibliotecas criptográficas comprovadas;
- Escolha e configuração adequada das primitivas criptográficas;
- Uso de um gerador de números aleatórios adequado sempre que a aleatoriedade for necessária.

## Requisitos de Verificação de Segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | O aplicativo não se baseia em criptografia simétrica com chaves fixas no código fonte como único método de criptografia. | ✓ | ✓ |
| **3.2** | MSTG-CRYPTO-2 | O aplicativo usa implementações comprovadas de primitivas criptográficas. | ✓ | ✓ |
| **3.3** | MSTG-CRYPTO-3 | O aplicativo usa primitivas criptográficas que são apropriadas para o caso de uso em questão, configurado com parâmetros que são aderentes às melhores práticas da indústria. | ✓ | ✓ |
| **3.4** | MSTG-CRYPTO-4 | O aplicativo não utiliza protocolos criptográficos ou algoritmos que são considerados amplamente obsoletos para uso em segurança. | ✓ | ✓ |
| **3.5** | MSTG-CRYPTO-5 | O aplicativo não reutiliza a mesma chave criptográfica para vários fins. | ✓ | ✓ |
| **3.6** | MSTG-CRYPTO-6 | Todos os valores aleatórios são gerados usando um gerador de números aleatórios suficientemente seguro. | ✓ | ✓ |

## Referências

O Guia de Teste de Segurança de Aplicações Móveis da OWASP fornece instruções detalhadas para verificar os requisitos listados nesta seção (em inglês).

- Android: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Para mais informações, consulte também (em inglês):

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
