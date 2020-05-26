# V5: Requerimentos de Comunicação de Rede

## Objetivo do Controle

O propósito dos controles listados nessa seção é garantir a confidencialidade e integridade das informações trocadas entre o aplicativo móvel e os *endpoints* de serviço remoto. Um aplicativo móvel deve, pelo menos, criar um canal seguro e criptografado para comunicação de rede utilizando o protocolo TLS com as configurações apropriadas. O Nível 2 lista medidas adicionais de defesa em profundidade, como fixação de SSL (*SSL Pinning*).

## Requerimentos de Verificação de Segurança

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Os dados são criptografados na rede utilizando TLS. O canal seguro é utilizado de forma consistente através do aplicativo. | ✓ | ✓ |
| **5.2** | MSTG-NETWORK-2 | As configurações do TLS estão alinhadas com as melhores práticas atuais, ou o mais próximas possível se o sistema operacional móvel não oferece suporte aos padrões recomendados. | ✓ | ✓ |
| **5.3** | MSTG-NETWORK-3 | O aplicativo verifica o certificado X.509 do *endpoint* remoto quando o canal seguro é estabelecido. Apenas certificados assinados por uma CA confiável são aceitos. | ✓ | ✓ |
| **5.4** | MSTG-NETWORK-4 | O aplicativo utiliza seu próprio armazenamento de certificados, ou define um certificado ou chave pública do *endpoint* e, posteriormente, não estabelece conexões com *endpoints* que ofereçam um certificado ou chave diferente, mesmo que assinados por uma CA confiável. |   | ✓ |
| **5.5** | MSTG-NETWORK-5 | O aplicativo não confia em um único canal de comunicações inseguro (email ou SMS) para operações críticas, como registros/cadastros ou recuperação de conta. |  | ✓ |
| **5.6** | MSTG-NETWORK-6 | O aplicativo depende de conectividade e bibliotecas de segurança atualizadas. |  | ✓ |

## Referências

O Guia de Teste de Segurança de Aplicações Móveis da OWASP provê instruções detalhadas para verificar os requerimentos listados nessa seção.

- Geral: Testando Comunicações de Rede (em inglês) - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Testando Comunicações de Rede (em inglês) - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Testando Comunicações de Rede (em inglês) - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Para mais informações, veja também (em inglês):

- OWASP Mobile Top 10: M3 (Communicação Insegura) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (Validação Inadequada de Certificados) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (Seguindo uma Cadeia de Confiança de Certificado Incorretamente) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (Validação Inadequada de Certificado com Incompatibilidade de *Host*) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (Validação Inadequada de Expiração de Certificado) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (Uso de Autenticação de Fator Único) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (Transmissão em Texto Claro de Informações Sensíveis) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (Encriptação com Força Inadequada) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Uso de Algoritmos Criptográficos Quebrados ou de Risco) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (Uso de Algoritmo RSA sem OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (Verificação Inadequada de Origem em um Canal de Comunicação) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (Especificação Incorreta de Destino em um Canal de Comunicação) - <https://cwe.mitre.org/data/definitions/941.html>
