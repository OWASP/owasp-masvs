# V1: Mimari, Tasarım ve Tehdit Modelleme Gereksinimleri

## Kontrol Hedefi

Kusursuz bir dünyada, güvenlik, geliştirmenin tüm aşamalarında dikkate alınmalıdır. Gerçekte ise, güvenlik genellikle sadece SDLC'nin son aşamasında ele alınan bir konudur. MASVS, teknik kontrollerin yanı sıra, mobil uygulamanın mimarisini planlarken güvenliğin açıkça ele alınmasını, tüm bileşenlerin işlevsel ve güvenlik rollerinin bilinmesini sağlayan süreçlerin yürürlükte olmasını gerektirir. Çoğu mobil uygulama, uzak servislerin istemcisi olarak hareket ettiğinden, bu servislerin de uygun güvenlik standartlarının uygulandığından emin olunmalıdır - mobil uygulamayı tek başına test etmek yeterli değildir.

"V1" kategorisi, uygulamanın mimarisi ve tasarımıyla ilgili gereksinimleri listeler. Bu nedenle, OWASP Mobile Testing Guide içerisindeki teknik test durumlarıyla eşleşmeyen tek kategori budur. Tehdit modellemesi, güvenli SDLC veya anahtar yönetimi gibi konuları kapsamak için MASVS kullanıcıları, ilgili OWASP projelerine ve/veya aşağıda bağlantılı olanlar gibi diğer standartlara başvurmalıdır.

## Güvenlik Doğrulama Gereksinimleri

MASVS-L1 ve MASVS-L2 gereksinimleri aşağıda listelenmiştir.

| # | MSTG-ID | Açıklama | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **1.1** | MSTG-ARCH-1 | Tüm uygulama bileşenleri tanımlanır ve ihtiyaç duyulduğu bilinir. | x | x |
| **1.2** | MSTG-ARCH-2 | Güvenlik denetimleri yalnızca istemci tarafında değil, ilgili uzak uç noktalarda da zorlanır. | x | x |
| **1.3** | MSTG-ARCH-3 | Mobil uygulama ve tüm bağlı uzak hizmetler için yüksek seviyeli bir mimari tanımlanır ve bu mimaride güvenlik ele alınır. | x | x |
| **1.4** | MSTG-ARCH-4 | Mobil uygulama bağlamında hassas olduğu düşünülen veriler açıkça tanımlanır. | x | x |
| **1.5** | MSTG-ARCH-5 | Tüm uygulama bileşenleri, sağladıkları iş işlevleri ve/veya güvenlik işlevleri açısından tanımlanır.  |  | x |
| **1.6** | MSTG-ARCH-6 | Potansiyel tehditleri ve karşı önlemleri belirleyen mobil uygulama ve ilişkili uzak servisler için bir tehdit modeli oluşturuldu. |  | x |
| **1.7** | MSTG-ARCH-7 | Tüm güvenlik kontrolleri merkezi bir entegrasyona sahiptir.  |  | x |
| **1.8** | MSTG-ARCH-8 | Şifreleme anahtarlarının (eğer varsa) nasıl yönetildiğine ve şifreleme anahtarlarının yaşam döngüsünün zorunlu kılınmasına ilişkin açık bir politika vardır. İdeal olarak, NIST SP 800-57 gibi bir temel yönetim standardını izleyin. |  | x |
| **1.9** | MSTG-ARCH-9 | Mobil uygulamanın güncellemelerini zorunlu kılmak için bir mekanizma mevcuttur. |  | x |
| **1.10** | MSTG-ARCH-10 | Güvenlik, yazılım geliştirme yaşam döngüsünün tüm bölümlerinde ele alınmaktadır. |  | x |
| **1.11** | MSTG-ARCH-11 | Sorumlu bir bilgilendirme politikası mevcuttur ve etkin bir şekilde uygulanmaktadır. |  | x |
| **1.12** | MSTG-ARCH-12 | Uygulama, gizlilik yasalarına ve düzenlemelerine uymalıdır. | x | x |

## Referanslar

Daha fazla bilgi için ayrıca bakınız:

- OWASP Mobile Top 10: M10 (Extraneous Functionality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m10-extraneous-functionality>
- OWASP Threat modelling - <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet - <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL - <https://www.microsoft.com/en-us/sdl/>
- NIST SP 800-57 - <https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final>
- security.txt - <https://securitytxt.org/>

