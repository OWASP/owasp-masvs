# V7: Kod Kalitesi ve Derleme Ayar Gereksinimleri

## Kontrol Hedefi

Bu kontrolün amacı, uygulamanın geliştirilmesinde temel güvenlik kodlama uygulamalarının takip edilmesini ve derleyici tarafından sunulan "ücretsiz" güvenlik özelliklerinin etkinleştirilmesini sağlamaktır.

## Güvenlik Doğrulama Gereksinimleri

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | Uygulama, özel anahtarın uygun şekilde korunduğu geçerli bir sertifika ile imzalanır ve sağlanır. | x | x |
| **7.2** | MSTG-CODE-2 | Uygulama, yayına uygun ayarlarla (ör. hata ayıklanamaz) yayın modunda oluşturulmuştur. | x | x |
| **7.3** | MSTG-CODE-3 | Hata ayıklama sembolleri  native binary dosyalardan kaldırıldı. | x | x |
| **7.4** | MSTG-CODE-4 | Hata ayıklama kodu ve geliştirici yardım kodu (ör. test kodu, arka kapılar, gizli ayarlar) kaldırıldı. Uygulama, ayrıntılı hataları veya hata ayıklama mesajlarını günlüğe kaydetmez. | x | x |
| **7.5** | MSTG-CODE-5 | Kitaplıklar ve çerçeveler gibi mobil uygulama tarafından kullanılan tüm üçüncü taraf bileşenleri tanımlanır ve bilinen güvenlik açıkları açısından kontrol edilir. | x | x |
| **7.6** | MSTG-CODE-6 | Uygulama, olası hataları yakalar ve işler. | x | x |
| **7.7** | MSTG-CODE-7 | Güvenlik kontrollerinde hata işleme mantığı, varsayılan olarak erişimi reddeder. | x | x |
| **7.8** | MSTG-CODE-8 | Yönetilmeyen kodda bellek tahsis edilir, serbest bırakılır ve güvenli bir şekilde kullanılır. | x | x |
| **7.9** | MSTG-CODE-9 | Bayt kodu küçültme, yığın koruması, PIE desteği ve otomatik referans sayımı gibi araç zinciri tarafından sunulan ücretsiz güvenlik özellikleri etkinleştirilir. | x | x |

## Referanslar

OWASP Mobile Security Testing Guide, bu bölümde listelenen gereksinimleri doğrulamak için ayrıntılı talimatlar sağlar.

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

Daha fazla bilgi için ayrıca bakınız:

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>
