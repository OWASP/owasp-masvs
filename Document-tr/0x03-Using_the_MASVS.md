# Mobil Uygulama Güvenlik Gereksinim Standardı

MASVS, mobil uygulamaların güvenliğine yönelik bir güven düzeyi oluşturmak için kullanılabilir. Gereksinimler, aşağıdaki hedefler göz önünde bulundurularak geliştirilmiştir:

- Metrik olarak kullanım - Mevcut mobil uygulamaların geliştiriciler ve uygulama sahipleri tarafından karşılaştırılabileceği bir güvenlik standardı sağlamak için;
- Kılavuz olarak kullanım - mobil uygulama geliştirme ve test sürecinin tüm fazlarında rehberlik sağlamak için;
- Tedarik sırasında kullanım - Mobil uygulama güvenlik doğrulaması için bir ana hat sağlamak için.

## Mobil AppSec Modeli

MASVS, iki güvenlik doğrulama düzeyini (MASVS-L1 ve MASVS-L2) ve bir dizi tersine mühendislik dayanıklılık gereksinimini (MASVS-R) tanımlar. MASVS-L1, tüm mobil uygulamalar için önerilen genel güvenlik gereksinimlerini içerirken, MASVS-L2 son derece hassas verileri işleyen uygulamalar için uygulanmalıdır. MASVS-R, istemci tarafındaki tehditleri önlemek bir tasarım hedefi ise uygulanabilecek ek koruyucu kontrolleri kapsar.

MASVS-L1'deki gereksinimleri karşılamak, en iyi güvenlik uygulamalarını izleyen ve yaygın güvenlik açıklarından etkilenmeyen güvenli bir uygulama ile sonuçlanır. MASVS-L2, mobil işletim sisteminin güvenlik kontrollerinin sağlam olduğunu ve son kullanıcının potansiyel bir düşman olarak görülmediğini varsayarak, daha karmaşık saldırılara karşı dirençli bir uygulama ile sonuçlanan SSL sabitleme gibi ek derinlemesine savunma kontrolleri ekler. MASVS-R'deki yazılım koruma gereksinimlerinin tamamını veya alt kümelerini karşılamak, son kullanıcının kötü niyetli olduğu ve/veya mobil işletim sisteminin tehlikeye düştüğü durumlarda belirli istemci tarafı tehditlerinin engellenmesine yardımcı olur.

**I: Her uygulamada MASVS-L1 kontrollerinin uygulanmasını önermemize rağmen, bir kontrolün uygulanması veya uygulanmaması, sonuçta iş sahipleriyle alınan/iletilen risk temelli bir karar olmalıdır.**

**II: MASVS-R'de listelenen ve OWASP Mobil Güvenlik Test Kılavuzunda açıklanan yazılım koruma kontrollerinin nihayetinde atlanabileceğini ve asla güvenlik kontrollerinin yerine kullanılmaması gerektiğini unutmayın. Bunun yerine, MASVS-L1 veya MASVS-L2'deki MASVS gereksinimlerini de karşılayan uygulamalara ek olarak belirli tehditlere yönelik, koruyucu denetimler eklemeyi amaçlamaktadır.**

![Verification Levels](images/masvs-levels-new.jpg)

### Doküman Yapısı

MASVS'nin ilk bölümü, güvenlik modelinin ve mevcut doğrulama seviyelerinin açıklamasını ve ardından standardın pratikte nasıl kullanılacağına dair tavsiyeleri içerir. Ayrıntılı güvenlik gereksinimleri, doğrulama seviyelerinin eşleştirilmesiyle birlikte ikinci bölümde listelenmiştir. Gereksinimler, teknik hedef/kapsama göre sekiz kategoriye (V1'den V8'e) gruplandırılmıştır. Aşağıdaki isimlendirme MASVS ve MSTG'de kullanılmaktadır:

- *Gereksinim kategorisi:* MASVS-Vx, ör. MASVS-V2: Veri Depolama ve Gizlilik
- *Gereksinim:* MASVS-Vx.y, ör. MASVS-V2.2: "Uygulama günlüklerine hassas veri yazılmaz."

### Doğrulama Düzeylerinin Detayları

#### MASVS-L1: Standard Güvenlik

MASVS-L1'e ulaşan bir mobil uygulama, mobil uygulama güvenliği için en iyi güvenlik pratiklerine bağlıdır. Kod kalitesi, hassas verilerin işlenmesi ve mobil ortamla etkileşim açısından temel gereksinimleri karşılar. Güvenlik kontrollerini doğrulamak için bir test süreci yürürlükte olmalıdır. Bu seviye tüm mobil uygulamalar için uygundur.

#### MASVS-L2: Derinlemesine Savunma

MASVS-L2, standart gereksinimlerin ötesinde gelişmiş güvenlik kontrolleri sunar. MASVS-L2'yi gerçekleştirmek için bir tehdit modeli mevcut olmalı ve güvenlik, uygulamanın mimarisinin ve tasarımının ayrılmaz bir parçası olmalıdır. Tehdit modeline göre, doğru MASVS-L2 kontrolleri seçilmeli ve başarıyla uygulanmalıdır. Bu seviye, mobil bankacılık uygulamaları gibi oldukça hassas verileri işleyen uygulamalar için uygundur.

#### MASVS-R: Tersine Mühendislik ve Kurcalamaya Karşı Dayanıklılık

Bu gereksinimlerde uygulama son teknoloji güvenliğe sahiptir ve ayrıca hassas kod veya verileri çıkarmak için kurcalama, modlama veya tersine mühendislik gibi belirli, açıkça tanımlanmış istemci tarafı saldırılarına karşı dayanıklıdır. Böyle bir uygulama ya donanım güvenlik özelliklerinden ya da yeterince güçlü ve doğrulanabilir yazılım koruma tekniklerinden yararlanır. MASVS-R, son derece hassas verileri işleyen ve fikri mülkiyeti korumayı veya kurcalamaya karşı koruma gerektiren uygulamalar için uygundur.

### Önerilen Kullanım

Uygulamalar, önceki risk değerlendirmesine ve gerekli genel güvenlik düzeyine dayalı olarak MASVS L1 veya L2'ye göre doğrulanabilir. L1, tüm mobil uygulamalar için geçerliyken, L2 genellikle daha hassas verileri ve / veya işlevselliği işleyen uygulamalar için önerilir. MASVS-R (veya bir kısmı), uygun güvenlik doğrulamasına *ek olarak* hassas verilerin yeniden paketlenmesi veya çıkarılması gibi belirli tehditlere karşı dayanıklılığı doğrulamak için uygulanabilir.

Özet olarak, aşağıdaki doğrulama türleri kullanılabilir:

- MASVS-L1
- MASVS-L1+R
- MASVS-L2
- MASVS-L2+R

Farklı kombinasyonlar, farklı güvenlik ve esneklik derecelerini yansıtır. Amaç esnekliğe izin vermektir: Örneğin, bir mobil oyun, kullanılabilirlik nedenleriyle 2 faktörlü kimlik doğrulama gibi MASVS-L2 güvenlik kontrolleri eklemeye ihtiyaç duymayabilir, ancak istemci tarafında kurcalamayı önleme konusunda güçlü bir iş gereksinimine sahip olabilir.

#### Hangi Doğrulama Türü Seçilmeli

MASVS L2 gereksinimlerinin uygulanması güvenliği artırırken aynı zamanda geliştirme maliyetini artırır ve son kullanıcı deneyimini potansiyel olarak kötüleştirir. Genel olarak L2, risk ve maliyet açısından anlamlı olduğunda (yani, gizlilik veya bütünlükten ödün vermenin neden olduğu potansiyel kayıp, ek güvenlik kontrollerinin neden olduğu maliyetten daha yüksek olduğunda) uygulamalar için kullanılmalıdır. MASVS'yi uygulamadan önce ilk adım bir risk değerlendirmesi olmalıdır.

##### Örnekler

###### MASVS-L1

- Tüm mobil uygulamalarda uygulanabilir. MASVS-L1, geliştirme maliyeti ve kullanıcı deneyimi üzerinde makul bir etkiyle izlenebilecek en iyi güvenlik uygulamalarını listeler. Daha yüksek seviyelerden birine uygun olmayan herhangi bir uygulama için MASVS-L1'deki gereksinimleri uygulayın.

<!-- \pagebreak -->

###### MASVS-L2

- Sağlık Endüstrisi: Kimlik hırsızlığı, dolandırıcılık ödemeleri veya çeşitli dolandırıcılık planları için kullanılabilen kişisel olarak tanımlanabilir bilgileri depolayan mobil uygulamaların uygulaması önerilir. ABD sağlık hizmetleri sektörü için uyumluluk konuları arasında Sağlık Sigortası Taşınabilirlik ve Sorumluluk Yasası (HIPAA) Gizlilik, Güvenlik, İhlal Bildirim Kuralları ve Hasta Güvenliği Kuralı bulunmaktadır.

- Finansal Endüstri: Kredi kartı numaraları, kişisel bilgiler gibi son derece hassas bilgilere erişim sağlayan veya kullanıcının para aktarmasına izin veren uygulamaların uygulaması önerilir. Bu uygulamalar, sahtekarlığı önlemek için ek güvenlik kontrollerini garanti eder. Finansal uygulamaların Payment Card Industry Data Security Standard (PCI DSS), Gramm Leech Bliley Yasası ve Sarbanes-Oxley Yasası (SOX) ile uyumluluğu sağlaması gerekir.

###### MASVS L1+R

- Fikri Mülkiyet (IP) korumasının bir iş hedefi olduğu mobil uygulamaların uygulaması önerilir. MASVS-R'de listelenen dayanıklılık kontrolleri, orijinal kaynak kodunu elde etmek ve kurcalama/kırılmayı engellemek için gereken çabayı artırmak için kullanılabilir.

- Oyun Endüstrisi: Rekabetçi çevrimiçi oyunlar gibi modlama ve hile yapmayı engelleme ihtiyacı olan oyunların uygulaması önerilir. Hile, çevrimiçi oyunlarda önemli bir sorundur, çünkü çok sayıda hileci hoşnutsuz bir oyuncu tabanına yol açar ve sonuçta bir oyunun başarısız olmasına neden olabilir. MASVS-R, dolandırıcıların çabasını artırmak için temel kurcalamaya karşı önleyici kontroller sağlar.

###### MASVS L2+R

- Finansal Endüstri: Ele geçirilen cihazlarda kod enjeksiyonu ve enstrümantasyon gibi tekniklerin risk oluşturduğu, para transferleri yapılabilen çevrimiçi bankacılık uygulamalarının uygulaması önerilir. Bu durumda, MASVS-R kontrolleri, kurcalanmayı engellemek için kullanılabilir ve kötü amaçlı yazılım sahipleri için çıtayı yükseltir.

- Tasarım gereği hassas verileri mobil cihazda depolaması gereken ve aynı zamanda çok çeşitli cihazları ve işletim sistemi sürümlerini desteklemesi gereken tüm mobil uygulamalarının uygulaması önerilir. Bu durumda dayanıklılık kontrolleri, hassas verileri çıkarmayı amaçlayan saldırganların çabalarını artırmak için kapsamlı bir savunma önlemi olarak kullanılabilir.

- Uygulama içi satın alımları olan uygulamalar, ücretli içeriği korumak için ideal olarak sunucu tarafı ve MASVS-L2 kontrollerini kullanmalıdır. Ancak, sunucu tarafı korumasını kullanma olanağının olmadığı durumlar olabilir. Bu durumlarda, tersine mühendislik ve/veya kurcalama çabasını artırmak için MASVS-R kontrolleri ek olarak uygulanmalıdır.
