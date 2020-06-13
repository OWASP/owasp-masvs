# V8: Requisitos de Resiliência

## Objetivo do Controle

Esta seção cobre as medidas de proteção recomendadas para aplicativos móveis que processam, ou dão acesso para, dados ou funcionalidades sensíveis. A falta de qualquer um desses controles não causa uma vulnerabilidade. Em vez disso, eles destinam-se a aumentar a resiliência do aplicativo móvel contra engenharia reversa e ataques específicos do lado do cliente.

Os controles desta seção devem ser aplicados conforme necessário, com base em uma avaliação dos riscos causados por manipulação não autorizada do aplicativo móvel e/ou engenharia reversa do código. Sugerimos que seja consultado os documentos "_Technical Risks of Reverse Engineering and Unauthorized Code Modification_" e "_Reverse Engineering and Code Modification Prevention_" do OWASP (veja referência abaixo) para uma lista dos riscos de negócio, assim como as ameaças técnicas associadas.

Para que qualquer controle da lista abaixo ser efetivo, o aplicativo móvel deve cumprir pelo menos todas as MASVS-L1 (ou seja, devem existir controles sólidos de segurança), assim como todos os requisitos de número inferior no V8. Por exemplo, os controles de ofuscação listados em "impedir a compreensão" devem ser combinados com "impedir a análise dinâmica e a manipulação" e "vinculação ao dispositivo".

**Perceba que as proteções de software nunca devem ser usadas como substitutas dos controles de segurança. Os controles listados no MASVR-R buscam adicionar controles específicos contra ameaças aos aplicativos móveis que também atendem aos requisitos de segurança do MASVS.

As seguintes considerações se aplicam:

1. Um modelo de ameaça deve ser definido para descrever de forma clara as ameaças que devem ser defendidas no lado do cliente. Além disso, deve ser especificado o grau de proteção que o esquema deve fornecer. Por exemplo, um objetivo poderia ser obrigar os autores do _malware_ que querem se utilizar do aplicativo móvel a terem que se esforçar bastante para realizar a engenharia reversa.

2. O modelo de ameaça deve ser crível e relevante. Por exemplo, esconder a chave criptográfica em uma implementação caixa branca pode ser redundante se um atacante puder simplesmente utilizar a aplicação móvel como um todo.

3. A efetividade da proteção deve sempre ser verificada por um especialista com experiência em testar tipos particulares de prevenção de manipulação e ofuscação usados (veja também os capítulos "_reverse engineering_" e "_assessing software protections_" no Guia de Teste de Segurança de Dispositivos Móveis).

<!-- \pagebreak -->

### Impedir Análise Dinâmica e Manipulação

| # | MSTG-ID | Descrição | R |
| -- | -------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | O aplicativo detecta e responde para a presença de um dispositivo com _root_ ou _jailbreak_ alertando o usuário ou fechando o aplicativo. | ✓ |
| **8.2** | MSTG-RESILIENCE-2 | O aplicativo previne a depuração e/ou detecta e reponde a ela. Todos os protocolos de depuração disponíveis devem ser cobertos. | ✓ |
| **8.3** | MSTG-RESILIENCE-3 | O aplicativo detecta e responde para a manipulação de executáveis e dados críticos do próprio aplicativo. | ✓ |
| **8.4** | MSTG-RESILIENCE-4 | O aplicativo detecta e responde para a presença no dispositivo de ferramentas de engenharia reversa e _frameworks_ amplamente utilizados. | ✓ |
| **8.5** | MSTG-RESILIENCE-5 | O aplicativo detecta e responde para quando executada em um emulador.  | ✓ |
| **8.6** | MSTG-RESILIENCE-6 | O aplicativo detecta e responde para manipulação de código e dados em seu espaço de memória. | ✓ |
| **8.7** | MSTG-RESILIENCE-7 | O aplicativo implementa múltiplos mecanismos em cada categoria de defesa (8.1 a 8.6). Observe que quanto maior a quantidade e diversidade de mecanismos usados, maior será a resiliência. | ✓ |
| **8.8** | MSTG-RESILIENCE-8 | Os mecanismos de detecção provocam diferentes tipos de respostas, inclusive respostas tardias e silenciosas. | ✓ |
| **8.9** | MSTG-RESILIENCE-9 | A ofuscação é aplicada às defesas do programa que, por sua vez, impede a desofuscação por meio de análise dinâmica. | ✓ |

### Vinculação ao Dispositivo

| # | MSTG-ID | Descrição | R |
| -- | -------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | O aplicativo implementa uma funcionalidade de 'vinculação ao dispositivo' usando um identificador único derivado de múltiplas propriedades únicas do dispositivo. | ✓ |

<!-- \pagebreak -->

### Impedir a Compreensão

| # | MSTG-ID | Descrição | R |
| -- | -------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | Todos os arquivos executáveis e bibliotecas pertencentes ao aplicativo devem ser cifrados e/ou códigos importantes e segmentos de dados dentro dos executáveis devem ser cifrados ou empacotados. Assim, uma análise estática trivial não revelará importantes trechos de código e dados. | ✓ |
| **8.12** | MSTG-RESILIENCE-12 | Se o objetivo da ofuscação é proteger códigos relevantes, deverá ser utilizado um esquema de ofuscação apropriado para essa tarefa particular e robusto para contra métodos de desofuscação manual e automatizada, considerando as pesquisas atualmente publicadas. A efetividade do esquema de ofuscação deve ser verificada com testes manuais. Observe que, sempre que possível, as funcionalidades de isolamento baseadas em hardware são preferíveis à ofuscação. | ✓ |

### Impedir o _Eavesdropping_

| # | MSTG-ID | Descrição | R |
| -- | -------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | Como defesa mais forte, além de ter um sólido fortalecimento das partes que se comunicam, pode ser implementada a criptografia de dados em nível de aplicativo como uma medida adicional contra ataques _eavesdropping_. | ✓ |

<!-- \pagebreak -->

## Referências

O Guia de Teste de Segurança de Dispositivos Móveis do OWASP disponibiliza instruções detalhadas para verificar os requisitos listados nesta seção (em inglês).

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

Para mais informação, veja também (em inglês):

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
