# V8: Requisitos de Resiliência

## Objetivo de controlo

Esta secção cobre medidas recomendadas de defesa em profundidade para aplicações que processam ou dão acesso a informação ou funcionalidades sensíveis. A falta de algum destes controlos não causa uma vulnerabilidade - em vez disso, estes são considerados para aumentar a resiliência da aplicação contra ataques de engenharia reversa e ataques específicos do lado do cliente.

Os controlos nesta secção devem ser aplicados quando necessários, baseados na avaliação dos riscos causados por manipulação não autorizada da aplicação, e/ou engenharia reversa do código. Nós sugerimos consultar o documento da OWASP "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention" (ver referências em baixo) para uma lista de riscos de negócio assim como ameaças técnicas associadas.

Para que qualquer um dos controlos da lista em baixo seja efetivo, a aplicação deve cumprir pelo menos com todos os requisitos de MASVS-L1 (Ex: Fortes controlos de segurança devem ser implementados) assim como todos os requisitos numerados com um valor baixo em V8. Para exemplificar, os controlos listados em "Impedimento compreensão" devem ser combinados com "Impedimento analise dinâmica e manipulação" e Device Binding

**É de notar que proteções de software nunca devem de ser usadas como alternativa a controlos de segurança. Os controlos listados em MASVR-R são planeados para adicionar controlos de proteção adicionais, específicos para ameaças, que também preenchem os requisitos de segurança de MASVS.**

As seguintes considerações são aplicadas:

1. Um modelo de ameaças tem de ser definido de tal forma que claramente realce as ameaças do lado do cliente que não devem de ser defendidas. Adicionalmente o nível de proteção que o modelo deve providenciar deve de ser especificado. Por exemplo um objetivo definito pode ser de forçar os autores de malware direcionado à procura de instrumentar a aplicação de investir esforços de engenharia reversa significativos.

2. O modelo de ameaças deve ser credível e relevante. Por exemplo, esconder uma chave de criptografia numa implementação de caixa branca pode provar-se redundante se um atacante poder simplesmente obter o código da caixa branca como um todo.

3. A eficácia da proteção deve ser verificada sempre por um humano especialista com experiência em testar particulares tipos de prevenção de adulteração e ofuscação usados (ver também os capítulos "engenharia reversa" e "Avaliação de Proteções de Software" em MOBILE SECURITY TESTING GUIDE).

<!-- \pagebreak -->

### Impedimento de análise dinâmica e manipulação

| # | MSTG-ID | Descrição| R |
| -- | -------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | A aplicação deteta, e responde à presença de um dispositivo 'rooted' ou com 'jailbreak' alertando o utilizador ou por fechar a aplicação. | ✓ |
| **8.2** | MSTG-RESILIENCE-2 | A aplicação previne depuração e/ou deteta e responde a um depurador ligado à aplicação. Todos os protocolos de depuração devem de ser tidos em conta. | ✓ |
| **8.3** | MSTG-RESILIENCE-3 | A aplicação deteta e responde a manipulação de ficheiros executáveis e informação critica dentro da sua sandbox. | ✓ |
| **8.4** | MSTG-RESILIENCE-4 | A aplicação deteta e responde à presença de ferramentas ou frameworks de engenharia reversa amplamente usadas no dispositivo. | ✓ |
| **8.5** | MSTG-RESILIENCE-5 | A aplicação deteta e responde a ser corrida num emulador.  | ✓ |
| **8.6** | MSTG-RESILIENCE-6 | A aplicação deteta e responde a manipulação de código e informação no seu próprio espaço de memória. | ✓ |
| **8.7** | MSTG-RESILIENCE-7 | A aplicação implementa vários mecanismos em cada categoria de defesa(8.1 to 8.6). É de notar que a resiliência aumenta com o número, diversidade e originalidade dos sistemas usados. | ✓ |
| **8.8** | MSTG-RESILIENCE-8 | Os mecanismos de deteção desencadeiam respostas de diferentes tipos, incluindo respostas atrasadas e furtivas. | ✓ |
| **8.9** | MSTG-RESILIENCE-9 | Ofuscação é aplicada a defesas de programação que por sua vez impedem a desofuscação por via de análise dinâmica.  | ✓ |

### Device Binding

| # | MSTG-ID | Descrição| R |
| -- | -------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | A aplicação implementa uma funcionalidade de 'DEVICE BINDING' usando uma impressão digital do dispositivo derivada de várias propriedades únicas do mesmo. | ✓ |

<!-- \pagebreak -->

### Impedimento de Compreensão

| # | MSTG-ID | Descrição | R |
| -- | -------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | Todos os ficheiros executáveis e bibliotecas pertencentes à aplicação são ou cifrados ao nível do ficheiro, e/ou código importante ou segmentos de informação dentro dos executáveis são cifrados ou embalados. Analise estática básica não revela código ou informação importante. | ✓ |
| **8.12** | MSTG-RESILIENCE-12 | Se o objetivo da ofuscação é proteger contra computações sensíveis, um esquema de ofuscação é usado que seja tanto apropriado para a tarefa em particular como robusto contro métodos de desofuscação manuais e automáticos, considerando investigações publicadas. A efetividade do esquema de ofuscação deve ser verificada com testes manuais. É de notar que características de isolamento baseado em hardware são preferidas em relação a ofuscação sempre que possível. | ✓ |

### Impedimento de espionagem

| # | MSTG-ID | Descrição | R |
| -- | -------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | Como uma defesa em profundidade a seguir a ter uma comunicação entre as várias entidades bem protegida, encriptação a nível aplicacional pode ser usada para impedir ainda mais a espionagem. | ✓ |

<!-- \pagebreak -->

## Referências

A OWASP Mobile Security Testing Guide fornece instruções detalhadas para verificar os requisitos listados nesta secção:

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

Para mais informação, ver também:

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
