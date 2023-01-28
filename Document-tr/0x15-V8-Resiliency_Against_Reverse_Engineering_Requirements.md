# V8: Dayanıklılık Gereksinimleri

## Kontrol Hedefi

Bu bölüm, hassas verileri veya işlevleri işleyen veya bunlara erişim sağlayan uygulamalar için önerilen kapsamlı savunma önlemlerini kapsar. Bu denetimlerin herhangi birinin olmaması bir güvenlik açığına neden olmaz - bunun yerine, uygulamanın tersine mühendislik ve belirli istemci tarafı saldırılarına karşı direncini artırmayı amaçlar.

Bu bölümdeki kontroller, uygulamada yetkisiz kurcalamanın ve/veya kodun tersine mühendisliğinin neden olduğu risklerin değerlendirilmesine dayalı olarak gerektiği gibi uygulanmalıdır. İş risklerinin yanı sıra ilgili teknik tehditlerin bir listesi için "Technical Risks of Reverse Engineering and Unauthorized Code Modification Reverse Engineering and Code Modification Prevention" (aşağıdaki referanslara bakın) OWASP belgesine başvurmanızı öneririz.

Aşağıdaki listedeki kontrollerden herhangi birinin etkili olması için, uygulamanın en azından MASVS-L1'in tamamını (yani, sağlam güvenlik kontrolleri mevcut olmalıdır) ve V8'deki tüm düşük numaralı gereksinimleri karşılaması gerekir. Örneğin, "anlamayı engelleme" altında listelenen gizleme kontrolleri "dinamik analiz ve kurcalamayı engelleme" ve "cihaz bağlama" ile birleştirilmelidir.

**Yazılım korumalarının asla güvenlik kontrollerinin yerine kullanılmaması gerektiğini unutmayın. MASVR-R'de listelenen kontroller, MASVS güvenlik gereksinimlerini de karşılayan uygulamalara tehdide özgü, ek koruyucu kontroller eklemeyi amaçlamaktadır.**

Aşağıdaki hususlar geçerlidir:

1. Savunulması gereken istemci tarafı tehditlerini açıkça ortaya koyan bir tehdit modeli tanımlanmalıdır. Ek olarak, planın sağlaması amaçlanan koruma derecesi belirtilmelidir. Örneğin, belirtilen bir hedef, uygulamayı önemli ölçüde manuel tersine mühendislik çabasına yatırım yapmaya zorlamak isteyen hedeflenen kötü amaçlı yazılım yazarlarını zorlamak olabilir.

2. Tehdit modeli güvenilir ve ilgili olmalıdır. Örneğin, bir beyaz kutu uygulamasında bir şifreleme anahtarının gizlenmesi, bir saldırgan beyaz kutuyu bir bütün olarak basitçe kodla kaldırabiliyorsa gereksiz olabilir.

3. Korumanın etkinliği her zaman, kullanılan belirli kurcalamaya karşı koruma ve gizleme türlerini test etme konusunda deneyimli bir insan uzman tarafından doğrulanmalıdır (Mobile Security Testing Guide içerisindeki "tersine mühendislik" ve "yazılım korumalarını değerlendirme" bölümlerine de bakın).

<!-- \pagebreak -->

### Dinamik Analizi ve Kurcalamayı Engelleme

| # | MSTG-ID | Açıklama | R |
| -- | ----------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | Uygulama, kullanıcıyı uyararak veya uygulamayı sonlandırarak root veya jailbreak yapılmış bir cihazın varlığını algılar ve yanıt verir. | x |
| **8.2** | MSTG-RESILIENCE-2 | Uygulama, hata ayıklamayı önler ve/veya eklenen bir hata ayıklayıcıyı algılar ve yanıt verir. Mevcut tüm hata ayıklama protokolleri kapsanmalıdır. | x |
| **8.3** | MSTG-RESILIENCE-3 | Uygulama, kendi sanal alanı içindeki yürütülebilir dosyalar ve kritik verilerle kurcalamayı algılar ve bunlara yanıt verir. | x |
| **8.4** | MSTG-RESILIENCE-4 | Uygulama, cihazda yaygın olarak kullanılan tersine mühendislik araçlarının ve çerçevelerinin varlığını algılar ve yanıt verir. | x |
| **8.5** | MSTG-RESILIENCE-5 | Uygulama, bir emülatörde çalıştırılmakta olduğunu algılar ve yanıt verir.  | x |
| **8.6** | MSTG-RESILIENCE-6 | Uygulama, kodu ve verileri kendi bellek alanında kurcalamayı algılar ve yanıt verir. | x |
| **8.7** | MSTG-RESILIENCE-7 | Uygulama, her savunma kategorisinde (8.1 ila 8.6) birden fazla mekanizma uygular. Dayanıklılığın, kullanılan mekanizmaların özgünlüğünün miktarı ve çeşitliliği ile ölçeklendiğini unutmayın. | x |
| **8.8** | MSTG-RESILIENCE-8 | Algılama mekanizmaları, gecikmeli ve gizli yanıtlar dahil olmak üzere farklı türdeki yanıtları tetikler. | x |
| **8.9** | MSTG-RESILIENCE-9 | Gizleme (obfuscation), programatik savunmalara uygulanır ve bu da dinamik analiz yoluyla gizliliğin kaldırılmasını engeller.  | x |

### Cihaz Bağlama (Device Binding)

| # | MSTG-ID | Açıklama | R |
| -- | ----------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | Uygulama, cihaza özgü birden çok özellikten türetilen bir cihaz parmak izi kullanarak bir 'cihaz bağlama' işlevi uygular. | x |

<!-- \pagebreak -->

### Anlamayı Engelleme

| # | MSTG-ID | Açıklama | R |
| -- | ----------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 | Uygulamaya ait tüm yürütülebilir dosyalar ve kitaplıklar ya dosya düzeyinde şifrelenir ve/veya yürütülebilir dosyaların içindeki önemli kod ve veri bölümleri şifrelenir veya paketlenir. Statik analiz, önemli kodu veya verileri ortaya çıkarmamalıdır. | x |
| **8.12** | MSTG-RESILIENCE-12 | Gizlemenin amacı hassas hesaplamaları korumaksa, şu anda yayınlanmış araştırmalar dikkate alınarak hem belirli görev için uygun hem de manuel ve otomatik gizleme yöntemlerine karşı dayanıklı olan bir gizleme şeması kullanılır. Gizleme planının etkinliği manuel test yoluyla doğrulanmalıdır. Donanım tabanlı yalıtım özelliklerinin, mümkün olduğunda gizleme yerine tercih edildiğini unutmayın. | x |

### Dinlemeyi Engelleme

| # | MSTG-ID | Açıklama | R |
| -- | ----------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | Derinlemesine bir savunma olarak, iletişim kuran tarafların sağlam bir şekilde sağlamlaştırılmasının yanı sıra, gizli dinlemeyi daha fazla engellemek için uygulama düzeyinde veri yükü şifrelemesi uygulanabilir. | x |

<!-- \pagebreak -->

## Referanslar

OWASP Mobile Security Testing Guide, bu bölümde listelenen gereksinimleri doğrulamak için ayrıntılı talimatlar sağlar.

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

Daha fazla bilgi için ayrıca bakınız:

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>
