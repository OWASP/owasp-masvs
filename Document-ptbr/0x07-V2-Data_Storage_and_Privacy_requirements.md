# V2: Requisitos de Armazenamento de Dados e Privacidade

## Objetivo do Controle

A proteção de dados sensíveis, como credenciais de usuário e informações pessoais, é um foco chave na segurança de dispositivos móveis. Primeiramente, dados sensíveis podem ser expostos de forma não-intencional a outros aplicativos rodando no mesmo dispositivo se os mecanismos do sistema operacional como o IPC estiverem sendo usados de forma incorreta. Os dados também podem ser vazados não-intencionalmente no armazenamento em nuvem, *backups* ou no *cache* do teclado. Além disso, dispositivos móveis podem ser perdidos ou roubados de forma mais comum que outros tipos de dispositivos, então um atacante conseguindo acesso físico ao equipamento é um cenário mais possível. Nesse caso, proteções adicionais podem ser implementadas para tornar a recuperação de dados sensíveis mais difícil.

Note que, como o MASVS é centrado no aplicativo, ele não cobre políticas a nível de dispositivo, como aquelas aplicadas por soluções MDM. Nós encorajamos a utilização dessas políticas em contexto corporativo para melhorar ainda mais a segurança dos dados.

### Definição de Dados Sensíveis

Dados sensíveis no contexto do MASVS incluem tanto as credenciais do usuário quanto quaisquer outros dados considerados sensíveis em contextos particulares, por exemplo:

- Informação de Identificação Pessoal (*Personally Identifiable Information* - PII) que possa ser utilizada para roubo de identidade: números de seguro social, números de cartão de crédito, dados de conta bancária, informações de saúde;
- Dados altamente sensíveis que podem causar danos à reputação e/ou custos financeiros se comprometidos: informações de contrato, informações protegidas por acordos de não divulgação (NDA), informações gerenciais;
- Quaisquer dados que sejam protegidos por lei ou regulações de conformidade.

## Requerimentos de Verificação de Segurança

A ampla maioria dos problemas de vazamento de dados podem ser prevenidos seguindo regras simples. A maior parte dos controles listados neste capítulo são mandatórios para todos os níveis de verificação.

| # | MSTG-ID | Descrição | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | Recursos de armazenamento de credenciais do sistema devem ser utilizados para armazenar dados sensíveis, como dados pessoais (PII), credenciais de usuário ou chaves criptográficas. | ✓ | ✓ |
| **2.2** | MSTG-STORAGE-2 | Dados sensíveis não devem ser armazenados fora do contêiner do aplicativo ou de recursos de armazenamento de credenciais do sistema. | ✓ | ✓ |
| **2.3** | MSTG-STORAGE-3 | Dados sensíveis não podem aparecer nos *logs* de aplicação. | ✓ | ✓ |
| **2.4** | MSTG-STORAGE-4 | Dados sensíveis não devem ser compartilhados com terceiros exceto se for uma parte necessária da arquitetura. | ✓ | ✓ |
| **2.5** | MSTG-STORAGE-5 | O _cache_ do teclado deve estar desabilitado nas entradas de usuário que processam dados sensíveis. | ✓ | ✓ |
| **2.6** | MSTG-STORAGE-6 | Dados sensíveis não devem ser expostos através de mecanismos IPC. | ✓ | ✓ |
| **2.7** | MSTG-STORAGE-7 | Dados sensíveis, como senhas ou PINs, não devem ser expostos através da interface de usuário. | ✓ | ✓ |
| **2.8** | MSTG-STORAGE-8 | Dados sensíveis não devem ser incluídos nos _backups_ gerados pelo sistema operacional móvel. |   | ✓ |
| **2.9** | MSTG-STORAGE-9 | O aplicativo deve remover dados sensíveis da visualização quando ficar em segundo plano. |  | ✓ |
| **2.10** | MSTG-STORAGE-10 | O aplicativo não deve manter dados sensíveis em memória mais tempo do que o necessário, e a memória deve ser completamente limpa depois do uso. |  | ✓ |
| **2.11** | MSTG-STORAGE-11 | O aplicativo deve reforçar o uso de políticas mínimas de segurança no acesso ao dispositivo, como pedir que o usuário defina um código de acesso ao dispositivo. |  | ✓ |
| **2.12** | MSTG-STORAGE-12 | O aplicativo deve ensinar o usuário sobre os tipos de Informação de Identificação Pessoal (PII) que são processadas, assim como melhores práticas de segurança que o usuário deve seguir quando utilizar o aplicativo. |  | ✓ |
| **2.13** | MSTG-STORAGE-13 | Dados sensíveis não devem ser armazenados localmente no dispositivo móvel. Em vez disso, os dados devem ser recuperados de um _terminal_ remoto quando necessário e mantidos apenas em memória. |  | ✓ |
| **2.14** | MSTG-STORAGE-14 | Se ainda assim for necessário armazenar dados pessoais localmente, eles devem ser cifrados utilizando uma chave derivada do armazenamento suportado pelo _hardware_ que requeira autenticação. |  | ✓ |
| **2.15** | MSTG-STORAGE-15 | O armazenamento local do aplicativo deve ser completamente apagado (_wipe_) após um número excessivo de tentativas de autenticação sem sucesso. |  | ✓ |

## Referências

O Guia de Teste de Segurança de Aplicações Móveis da OWASP provê instruções detalhadas para verificar os requerimentos listados nesta seção (em inglês).

- Android: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

Para mais informações, veja também (em inglês):

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
