# V2: Veri Depolama ve Gizlilik Gereksinimleri

## Kontrol Hedefi

Kullanıcı kimlik bilgileri ve özel bilgiler gibi hassas verilerin korunması, mobil güvenliğin temel odak noktasıdır. İlk olarak, hassas veriler, IPC gibi işletim sistemi mekanizmaları tarafından uygunsuz bir şekilde kullanılırsa, aynı cihazda çalışan diğer uygulamalara istenmeden ifşa edilebilir. Ayrıca veriler istemeden bulut depolamaya, yedeklemelere veya klavye önbelleğine sızabilir. Ek olarak, mobil cihazlar diğer cihaz türlerine kıyasla daha kolay kaybolabilir veya çalınabilir, bu nedenle fiziksel erişim elde eden bir düşman daha olası bir senaryodur. Bu durumda, hassas verilerin alınmasını daha zor hale getirmek için ek korumalar uygulanabilir.

MASVS uygulama merkezli olduğundan, MDM çözümleri tarafından zorunlu kılınan cihaz düzeyinde politikaları kapsamamaktadır. Veri güvenliğini daha da artırmak için bu tür politikaların kurumsal bağlamda kullanılmasını destekliyoruz.

### Hassas Verilerin Tanımı

MASVS bağlamındaki hassas veriler, hem kullanıcı kimlik bilgileriyle hem de belirli bağlamda hassas olduğu düşünülen diğer verilerle ilgilidir, örneğin:

- Kimlik hırsızlığı için kötüye kullanılabilecek kişisel tanımlanabilir bilgiler (PII): Sosyal güvenlik numaraları, kredi kartı numaraları, banka hesap numaraları, sağlık bilgileri;
- Açığa çıkması durumunda itibarın zarar görmesine ve/veya finansal maliyetlere yol açabilecek son derece hassas veriler: Sözleşme bilgileri, gizlilik anlaşmalarının kapsadığı bilgiler, yönetim bilgileri;
- Yasa tarafından veya uygunluk nedenleriyle korunması gereken herhangi bir veri.

## Güvenlik Doğrulama Gereksinimleri

Veri ifşa sorunlarının büyük çoğunluğu basit kurallara uyarak önlenebilir. Bu bölümde listelenen kontrollerin çoğu tüm doğrulama seviyeleri için zorunludur.

| # | MSTG-ID | Açıklama | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | Kişisel tanımlanabilir bilgiler (PII), kullanıcı kimlik bilgileri veya kriptografik anahtarlar gibi hassas verileri depolamak için sistem kimlik bilgileri depolama tesislerinin kullanılması gerekir. | x | x |
| **2.2** | MSTG-STORAGE-2 | Hassas veriler, uygulama alanı veya sistem kimlik depolama alanları dışındaki alanlarda saklanmamalıdır. | x | x |
| **2.3** | MSTG-STORAGE-3 | Uygulama günlüklerine hassas veriler yazılmaz. | x | x |
| **2.4** | MSTG-STORAGE-4 | Mimarinin gerekli bir parçası olmadığı sürece hiçbir hassas veri üçüncü taraflarla paylaşılmaz. | x | x |
| **2.5** | MSTG-STORAGE-5 | Hassas verileri işleyen metin girişlerinde klavye önbellek özelliği devre dışı bırakılır. | x | x |
| **2.6** | MSTG-STORAGE-6 | IPC mekanizmaları aracılığıyla hiçbir hassas veri açığa çıkarılmaz. | x | x |
| **2.7** | MSTG-STORAGE-7 | Parola veya pin gibi hassas veriler, kullanıcı arabirimi aracılığıyla açığa çıkarılmaz. | x | x |
| **2.8** | MSTG-STORAGE-8 | Mobil işletim sistemi tarafından oluşturulan yedeklemelere hiçbir hassas veri dahil edilmez. |   | x |
| **2.9** | MSTG-STORAGE-9 | Uygulama, arka plana taşındığında hassas verileri görünümlerden kaldırır. |  | x |
| **2.10** | MSTG-STORAGE-10 | Uygulama hassas verileri hafızada gerekenden daha uzun süre tutmaz ve kullanımdan sonra hafıza açıkça temizlenir. |  | x |
| **2.11** | MSTG-STORAGE-11 | Uygulama, kullanıcının bir cihaz parolası belirlemesini istemek gibi minimum bir cihaz erişim güvenliği politikası uygular. |  | x |
| **2.12** | MSTG-STORAGE-12 | Uygulama, kullanıcıyı, işlenen kişisel olarak tanımlanabilir bilgi türleri ve ayrıca kullanıcının uygulamayı kullanırken izlemesi gereken en iyi güvenlik uygulamaları hakkında eğitir. |  | x |
| **2.13** | MSTG-STORAGE-13 | Mobil cihazda yerel olarak hiçbir hassas veri saklanmamalıdır. Bunun yerine, veriler gerektiğinde uzak bir uç noktadan alınmalı ve yalnızca bellekte tutulmalıdır. |  | x |
| **2.14** | MSTG-STORAGE-14 | Hassas verilerin hala yerel olarak depolanması gerekiyorsa, donanım destekli depolamadan türetilen ve kimlik doğrulama gerektiren bir anahtar kullanılarak şifrelenmelidir. |  | x |
| **2.15** | MSTG-STORAGE-15 | Uygulamanın yerel depolaması, aşırı sayıda başarısız kimlik doğrulama girişiminden sonra silinmelidir. |  | x |

## Referanslar

OWASP Mobile Security Testing Guide, bu bölümde listelenen gereksinimleri doğrulamak için ayrıntılı talimatlar sağlar.

- Android: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>

Daha fazla bilgi için ayrıca bakınız:

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
