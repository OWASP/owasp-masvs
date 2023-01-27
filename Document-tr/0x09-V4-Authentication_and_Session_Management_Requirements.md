# V4: Kimlik Doğrulama ve Oturum Yönetimi Gereksinimleri

## Kontrol Hedefi

Çoğu durumda, bir uzak serviste oturum açan kullanıcılar, genel mobil uygulama mimarisinin ayrılmaz bir parçasıdır. Mantığın çoğu uç noktada gerçekleşse de MASVS, kullanıcı hesaplarının ve oturumlarının nasıl yönetileceğine ilişkin bazı temel gereksinimleri tanımlar.

## Güvenlik Doğrulama Gereksinimleri

| # | MSTG-ID | Açıklama | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | Uygulama, kullanıcılara uzak bir servise erişim sağlıyorsa, uzak uç noktada kullanıcı adı/parola kimlik doğrulaması gibi bir tür kimlik doğrulama gerçekleştirilir. | x | x |
| **4.2** | MSTG-AUTH-2 | Durum bilgisi olan (stateful) oturum yönetimi kullanılıyorsa, uzak uç nokta, kullanıcının kimlik bilgilerini göndermeden istemci isteklerinin kimliğini doğrulamak için rastgele oluşturulmuş oturum tanımlayıcılarını kullanır. | x | x |
| **4.3** | MSTG-AUTH-3 | Durum bilgisi olmayan (stateless) token tabanlı kimlik doğrulama kullanılıyorsa, sunucu güvenli bir algoritma kullanılarak imzalanmış bir token sağlar. | x | x |
| **4.4** | MSTG-AUTH-4 | Uzak uç nokta, kullanıcı oturumu kapattığında mevcut oturumu sonlandırır. | x | x |
| **4.5** | MSTG-AUTH-5 | Uzak uç noktada bir parola politikası vardır ve uzak uç noktada uygulanır. | x | x |
| **4.6** | MSTG-AUTH-6 | Uzak uç nokta, kimlik bilgilerinin aşırı sayıda gönderilmesine karşı koruma sağlayan bir mekanizma uygular. | x | x |
| **4.7** | MSTG-AUTH-7 | Oturumlar, önceden tanımlanmış bir hareketsiz kalma süresi ve erişim tokenı süresi dolduktan sonra uzak uç noktada geçersiz kılınır. | x | x |
| **4.8** | MSTG-AUTH-8 | Eğer biyometrik kimlik doğrulama varsa, olaya bağlı değildir (yani, yalnızca "true" veya "false" döndüren bir API). Bunun yerine, keychain/keystore kilidini açmaya dayanır. | | x |
| **4.9** | MSTG-AUTH-9 | Uzak uç noktada ikinci bir kimlik doğrulama faktörü vardır ve 2FA gereksinimi tutarlı bir şekilde uygulanır.  | | x |
| **4.10** | MSTG-AUTH-10 | Hassas işlemler, aşamalı kimlik doğrulaması gerektirir. | | x |
| **4.11** | MSTG-AUTH-11 | Uygulama, kullanıcıyı hesabıyla ilgili tüm hassas etkinlikler konusunda bilgilendirir. Kullanıcılar, cihazların listesini görüntüleyebilir, bağlamsal bilgileri (IP adresi, konum vb.) görüntüleyebilir ve belirli cihazları engelleyebilir. | | x |
| **4.12** | MSTG-AUTH-12 | Yetkilendirme modelleri uzak uç noktada tanımlanır ve uygulanır. | x | x |

## Referanslar

OWASP Mobile Security Testing Guide, bu bölümde listelenen gereksinimleri doğrulamak için ayrıntılı talimatlar sağlar.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

Daha fazla bilgi için ayrıca bakınız:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>

