
# V5: Requisitos de comunicação em Rede

## Objetivo de Controlo

O objetivo dos controlos detalhados nesta secção é de garantir a confidencialidade e integridade da informação trocada entre a aplicação móvel e os pontos de acesso do serviço remoto. No mínimo, a aplicação móvel deve de usar um canal seguro e cifrados para as comunicações em rede, usando o protocolo TLS com configurações apropriadas. o Nível 2 (L2) lista medidas de defesas em profundidade como 'SSL pinnning'

## Requisitos de verificação de segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Os dados são cifrados na rede usando TLS. Este canal seguro é usado com consistência ao longo da aplicação. | ✓ | ✓ |
| **5.2** | MSTG-NETWORK-2 | As configurações de TLS estão de acordo com as melhores praticas atuais, ou o mais próximo possível caso o sistema operativo movel não suporte os padrões recomendados. | ✓ | ✓ |
| **5.3** | MSTG-NETWORK-3 | A aplicação verifica o certificado X.509 do ponto de acesso remoto quando o canal seguro é estabelecido. Apenas certificados assinados por uma autoridade certificadora de confiança são aceites. | ✓ | ✓ |
| **5.4** | MSTG-NETWORK-4 | A aplicação ou usa a sua própria loja de certificados ou fixa o certificado da ou chave pública do ponto de acesso, e subsequentemente não estabelece ligações a pontos de acesso que ofereçam um certificado ou chave diferentes, mesmo que assinados por uma Autoridade de Certificação de confiança |   | ✓ |
| **5.5** | MSTG-NETWORK-5 | A aplicação não depende apenas de um único canal de comunicação inseguro (email ou SMS) para operações críticas, tais como inscrições e recuperação de contas. |  | ✓ |
| **5.6** | MSTG-NETWORK-6 | A aplicação depende apenas de conetividade atualizada e bibliotecas seguras. |  | ✓ |

## Referencias

O OWASP Mobile Security Testing Guide fornece instruções detalhadas de como verificar os requisitos identificados nesta secção.

- General: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Para mais informações ver também:

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
