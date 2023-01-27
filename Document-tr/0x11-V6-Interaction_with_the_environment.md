# V6: Platform Etkileşim Gereksinimleri

## Kontrol Hedefi

Bu gruptaki kontroller, uygulamanın platform API'lerini ve standart bileşenleri güvenli bir şekilde kullanmasını sağlar. Ek olarak, kontroller uygulamalar arasındaki iletişimi (IPC) kapsar.

## Güvenlik Doğrulama Gereksinimleri

| # | MSTG-ID | Açıklama | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | Uygulama, yalnızca gerekli olan minimum izin grubunu ister. | x | x |
| **6.2** | MSTG-PLATFORM-2 | Harici kaynaklardan ve kullanıcıdan gelen tüm girdiler doğrulanır ve gerekirse sterilize edilir. Bu, kullanıcı arayüzü aracılığıyla alınan verileri, amaçlar, özel URL'ler ve ağ kaynakları gibi IPC mekanizmalarını içerir. | x | x |
| **6.3** | MSTG-PLATFORM-3 | Bu mekanizmalar uygun şekilde korunmadıkça, uygulama özel URL şemaları aracılığıyla hassas işlevleri dışa aktarmaz. | x | x |
| **6.4** | MSTG-PLATFORM-4 | Uygulama, bu mekanizmalar uygun şekilde korunmadıkça, IPC aracılığıyla hassas işlevleri dışa aktarmaz. | x | x |
| **6.5** | MSTG-PLATFORM-5 | JavaScript, açıkça gerekmedikçe webview yapılarında devre dışı bırakılır. | x | x |
| **6.6** | MSTG-PLATFORM-6 | Webview yapıları, yalnızca gereken minimum protokol işleyici kümesine izin verecek şekilde yapılandırılır (ideal olarak yalnızca https desteklenir). File, tel ve app-id gibi potansiyel olarak tehlikeli işleyiciler devre dışı bırakılır. | x | x |
| **6.7** | MSTG-PLATFORM-7 | Uygulamanın native metodları bir webview yapısına maruz bırakılırsa, webview yapısının yalnızca uygulama paketinde bulunan JavaScript'i oluşturduğunu doğrulayın. | x | x |
| **6.8** | MSTG-PLATFORM-8 | Nesne seriden çıkarma işlemi varsa güvenli serileştirme API'leri uygulanır. | x | x |
| **6.9** | MSTG-PLATFORM-9 | Uygulama, screen overlay saldırılarına karşı kendini korur. (Yalnızca Android) |  | x |
| **6.10** | MSTG-PLATFORM-10 | WebView yok edilmeden önce WebView önbelleği, deposu ve yüklenen kaynaklar (JavaScript, vb.) temizlenir. |  | x |
| **6.11** | MSTG-PLATFORM-11 | Hassas veriler girildiğinde uygulamanın özel üçüncü taraf klavyelerin kullanımını engellediğini doğrulayın (yalnızca iOS). | | x |

## Referanslar

OWASP Mobile Security Testing Guide, bu bölümde listelenen gereksinimleri doğrulamak için ayrıntılı talimatlar sağlar.

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

Daha fazla bilgi için ayrıca bakınız:

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

