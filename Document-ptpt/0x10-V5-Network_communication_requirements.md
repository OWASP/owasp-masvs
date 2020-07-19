
# V5: Requisitos de comunicação em Rede

## Objetivo de Controlo

O objetivo dos controlos detalhados nesta secção é de garantir a confidencialidade e integridade da informaçao trocada entre a aplicaçao movel e os pontos de acesso do serviço remoto. No minimo, a aplicação movel deve de usar um canal seguro e encriptado para as comunicaçoes em rede, usando o protocolo TlS com configuraçoes apropriadas. o Nivel 2 (L2) lista medidas de defesas em profundidade como 'SSL pinnning'

## Requisitos de verificaçao de segurança
| # | MSTG-ID | Description | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Os dados sao encriptados na rede usando TLS. Este canal seguro é usado com consistencia ao longo d aplicaçao. | ✓ | ✓ |
| **5.2** | MSTG-NETWORK-2 | As configuraçoes de TLS estao de acordo com as melhores praticas atuaism, ou o mais proximo possivel caso o sistema operativo movel nao suporte os padroes recomendados. | ✓ | ✓ |
| **5.3** | MSTG-NETWORK-3 | A aplicação verifica o certificado X.509 do ponto de acesso remoto quando o canal seguro é estabelecido. Apenas certificados assinados por uma autoridade certificadora de confiança sao aceites. | ✓ | ✓ |
| **5.4** | MSTG-NETWORK-4 | **MISSING TRANSLATION HERE The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.** |   | ✓ |
| **5.5** | MSTG-NETWORK-5 | A app nao depende apenas de um unico canel de comunica;ao inseguro (email ou SMS) para operaçoes criticas, tais como inscriçoes e recuperaçao de contas. |  | ✓ |
| **5.6** | MSTG-NETWORK-6 | A aplicaçao depende apenas de conetividade atualizada e bibliotecas seguras. |  | ✓ |

## References

O OWASP Mobile Security Testing Guide fornece instruçoes detalhadas de como verificar os requisitos identificados nesta secção.

- General: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Para mais informaçoes ver tambem:

- OWASP Mobile Top 10: M3 (Insecure Communication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Improper Certificate Validation) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Improper Following of a Certificate's Chain of Trust) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Improper Validation of Certificate with Host Mismatch) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Improper Validation of Certificate Expiration) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Cleartext Transmission of Sensitive Information) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Use of RSA Algorithm without OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Improper Verification of Source of a Communication Channel) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Incorrectly Specified Destination in a Communication Channel) - <https://cwe.mitre.org/data/definitions/941.html>
