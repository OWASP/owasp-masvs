# V2: Armazenamento de Dados e Requisitos de Privacidade

## Objetivo de Controlo

A proteção de informação sensível, como por exemplo as credenciais do utilizador, e informação privada, é fulcral em segurança de dispositivos móveis. Informação sensível pode ser exposta de forma não intencional a outras aplicações em funcionamento no mesmo dispositivo se os mecanismos do sistema operativo, como o IPC, não são usados de forma apropriada.  A informação também pode de forma não intencional vazar para armazenamento na nuvem, cópias de segurança ou cache to teclado. Adicionalmente os dispositivos móveis podem serem perdidos ou roubados mais facilmente comparados a outros dispositivos, então um atacante ganhar acesso fisico ao sistema é um cenário mais provável. Para evitar estes casos proteções adicionais podem ser implementadas forma a tornar a obtenção de informação sensível mais difícil.

Repare que, a MASVS é focada na aplicação, e não cobre políticas a nível do dispositivo tais como as impostas por soluções MDM . Nós recomendamos o uso de tais políticas num contexto empresarial para melhorar a proteção da informação.

### Definição de Informação Sensível

Informação privada, no contexto da MASVS, diz respeito não só às credenciais do utilizador mas também a outros dados sensíveis, como por exemplo:

- Informação de Identificação Pessoal (PII) que pode ser abusada para roubo de identidade: números de segurança social, números de cartões de crédito, números de conta bancária, informação de saúde;
- Informação altamente sensível que pode pôr em causa a reputação do indivíduo, e/ou custos financeiros se comprometida: Informação contratual, Informação de não divulgação, informação de gestão;
- Quaisquer dados que devem ser protegidos por lei ou outras razões.

## Requisitos para Verificação de Segurança

A grande maioria de exposição de dados privados pode ser evitada através da aplicação de regras simples. A maioria das diretrizes listadas neste capítulo são obrigatórias para todos os níveis de verificação.

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | Para o armazenamento de dados privados, como por exemplo credenciais ou chaves criptográficas,  devem ser utilizados módulos de sistema dedicados ao armazenamento de credenciais. | ✓ | ✓ |
| **2.2** | MSTG-STORAGE-2 | Nunca guardar dados privados em sistemas fora da aplicação que não sejam módulos de sistema dedicados ao armazenamento de credenciais. | ✓ | ✓ |
| **2.3** | MSTG-STORAGE-3 | Nenhuma informação sensível é exposta nos registos de actividade (logs) da aplicação. | ✓ | ✓ |
| **2.4** | MSTG-STORAGE-4 | Nenhuma informação sensível é partilhada com aplicações externas excepto se extremamente necessário. | ✓ | ✓ |
| **2.5** | MSTG-STORAGE-5 | A memória do teclado (keyboard cache) está desabilitada nos controlos de entrada de texto relativos a dados privados. | ✓ | ✓ |
| **2.6** | MSTG-STORAGE-6 | Nenhuma informação sensível é exposta via comunicação inter-processos (IPC). | ✓ | ✓ |
| **2.7** | MSTG-STORAGE-7 | Nenhuma informação sensível, nomeadamente palavras-passe, é exposta na interface apresentada ao utilizador. | ✓ | ✓ |
| **2.8** | MSTG-STORAGE-8 | Nenhuma informação sensível é incluída nas cópias de segurança geradas pelo sistema operativo. |   | ✓ |
| **2.9** | MSTG-STORAGE-9 | A aplicação remove/esconde qualquer informação privada das vistas, quando a aplicação é enviada para segundo plano. |  | ✓ |
| **2.10** | MSTG-STORAGE-10 | A aplicação não guarda em memória informação sensível durante um período maior que o necessário, sendo que essa mesma informação é apagada findo o respectivo uso. |  | ✓ |
| **2.11** | MSTG-STORAGE-11 | A aplicação reforça uma política mínima de segurança no acesso ao dispositivo, como por exemplo a necessidade do utilizador para definir um código-passe. |  | ✓ |
| **2.12** | MSTG-STORAGE-12 | A aplicação indica ao utilizador os tipos de informação privada processada, assim como as boas práticas a seguir durante a utilização da mesma. |  | ✓ |
| **2.13** | MSTG-STORAGE-13 | Nenhuma informação sensível é guardada localmente no dispositivo móvel. Esses mesmos dados são obtidos através de um pedido a um servidor externo quando necessário, sendo mantidos em memória enquanto necessário. |  | ✓ |
| **2.14** | MSTG-STORAGE-14 | Caso seja necessário guardar localmente informação sensível, esta deve ser encriptada com uma chave proveniente de um dispositivo de armazenamento que exija autenticação para o acesso ao mesmo. |  | ✓ |
| **2.15** | MSTG-STORAGE-15 | O armazenamento local da aplicação deve ser limpo após uma excessiva quantidade de tentativas de autenticação. |  | ✓ |

## Referências

O OWASP Mobile Security Testing Guide providencia instruções detalhadas para verificação dos requisitos listados nesta secção.

- Android: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

Para mais informação:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M2 (Insecure Data Storage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage>
- CWE 117 (Improper Output Neutralization for Logs) - <https://cwe.mitre.org/data/definitions/117.html>
- CWE 200 (Information Exposure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 276 (Incorrect Default Permissions) - <https://cwe.mitre.org/data/definitions/276.html>
- CWE 311 (Missing Encryption of Sensitive Data) - <https://cwe.mitre.org/data/definitions/311.html>
- CWE 312 (Cleartext Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/312.html>
- CWE 316 (Cleartext Storage of Sensitive Information in Memory) - <https://cwe.mitre.org/data/definitions/316.html>
- CWE 359 (Exposure of Private Information ('Privacy Violation')) - <https://cwe.mitre.org/data/definitions/359.html>
- CWE 522 (Insufficiently Protected Credentials) - <https://cwe.mitre.org/data/definitions/522.html>
- CWE 524 (Information Exposure Through Caching) - <https://cwe.mitre.org/data/definitions/524.html>
- CWE 530 (Exposure of Backup File to an Unauthorized Control Sphere) - <https://cwe.mitre.org/data/definitions/530.html>
- CWE 532 (Information Exposure Through Log Files) - <https://cwe.mitre.org/data/definitions/532.html>
- CWE 534 (Information Exposure Through Debug Log Files) - <https://cwe.mitre.org/data/definitions/534.html>
- CWE 634 (Weaknesses that Affect System Processes) - <https://cwe.mitre.org/data/definitions/634.html>
- CWE 798 (Use of Hard-coded Credentials) - <https://cwe.mitre.org/data/definitions/798.html>
- CWE 921 (Storage of Sensitive Data in a Mechanism without Access Control) - <https://cwe.mitre.org/data/definitions/921.html>
- CWE 922 (Insecure Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/922.html>
