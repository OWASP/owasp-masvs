# V5: Ağ İletişim Gereksinimleri

## Kontrol Hedefi

Bu bölümde listelenen kontrollerin amacı, mobil uygulama ile uzak servis uç noktaları arasında aktarılan bilgilerin gizliliğini ve bütünlüğünü sağlamaktır. En azından bir mobil uygulama, uygun ayarlarla TLS protokolünü kullanarak ağ iletişimi için güvenli, şifreli bir kanal kurmalıdır. Seviye 2, SSL sabitleme gibi ek derinlemesine savunma önlemlerini listeler.

## Güvenlik Doğrulama Gereksinimleri

| # | MSTG-ID | Açıklama | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | Veriler ağda TLS kullanılarak şifrelenir. Güvenli kanal, uygulama boyunca tutarlı bir şekilde kullanılır. | x | x |
| **5.2** | MSTG-NETWORK-2 | TLS ayarları, mevcut en iyi uygulamalarla uyumludur veya mobil işletim sistemi önerilen standartları desteklemiyorsa mümkün olduğunca yakındır. | x | x |
| **5.3** | MSTG-NETWORK-3 | Uygulama, güvenli kanal kurulduğunda uzak uç noktanın X.509 sertifikasını doğrular. Yalnızca güvenilir bir CA tarafından imzalanmış sertifikalar kabul edilir. | x | x |
| **5.4** | MSTG-NETWORK-4 | Uygulama ya kendi sertifika deposunu kullanır ya da uç nokta sertifikasını veya genel anahtarı sabitler ve ardından güvenilir bir CA tarafından imzalanmış olsa bile farklı bir sertifika veya anahtar sunan uç noktalarla bağlantı kurmaz. |   | x |
| **5.5** | MSTG-NETWORK-5 | Uygulama, kayıtlar ve hesap kurtarma gibi kritik işlemler için tek bir güvenli olmayan iletişim kanalına (e-posta veya SMS) güvenmez. |  | x |
| **5.6** | MSTG-NETWORK-6 | Uygulama yalnızca güncel bağlantı ve güvenlik kütüphanelerine bağlıdır. |  | x |

## Referanslar

OWASP Mobile Security Testing Guide, bu bölümde listelenen gereksinimleri doğrulamak için ayrıntılı talimatlar sağlar.

- General: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: Testing Network Communication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

Daha fazla bilgi için ayrıca bakınız:

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
