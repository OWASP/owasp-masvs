# Önsöz

Teknolojik devrimler hızlı bir şekilde gerçekleşebilir. On yıldan daha kısa bir süre önce, akıllı telefonlar küçük klavyeleri olan hantal cihazlardı - teknoloji meraklısı iş insanları için pahalı oyuncaklardı. Günümüzde ise akıllı telefonlar hayatımızın önemli bir parçası. Bilgi, navigasyon ve iletişim için onlara güvenmeye başladık ve hem iş hayatımızda hem de sosyal hayatımızda her yerde bulunuyorlar.

Her yeni teknoloji, yeni güvenlik riskleri ortaya çıkarır ve bu değişikliklere ayak uydurmak, güvenlik endüstrisinin karşı karşıya kaldığı ana zorluklardan biridir. Savunma tarafı her zaman birkaç adım geride kalıyor. Örneğin, birçoğu için varsayılan refleks, işleri yapmanın eski yöntemlerini uygulamaktı: "Akıllı telefonlar küçük bilgisayarlar gibi ve mobil uygulamalar da tıpkı klasik yazılımlar gibidir - dolayısıyla aynı güvenlik gereksinimleri geçerlidir." Fakat bu böyle işlemiyor. Akıllı telefon işletim sistemleri masaüstü işletim sistemlerinden farklıdır ve mobil uygulamalar da web uygulamalarından farklıdır. Örneğin, klasik imza tabanlı virüs taraması yöntemi, modern mobil işletim sistemi ortamlarında bir anlam ifade etmez: Yalnızca mobil uygulama dağıtım modeliyle uyumsuz olmakla kalmaz, aynı zamanda korumalı alan kısıtlamaları nedeniyle teknik olarak imkansızdır. Ayrıca, arabellek taşmaları ve XSS gibi bazı güvenlik zafiyetleri istisnaları olsa da masaüstü ve web uygulamalarından ziyade mobil uygulamalar bağlamında daha az görülür.

Zamanla, sektörümüz mobil tehdit ortamını daha iyi kavradı. Görününen o ki mobil güvenliği tamamen veri korumayla ilgilidir: Uygulamalar kişisel bilgilerimizi, resimlerimizi, kayıtlarımızı, notlarımızı, hesap verilerimizi, iş bilgilerimizi, konumumuzu ve daha fazlasını depolar. Bizi günlük kullandığımız hizmetlere bağlayan istemciler ve başkalarıyla paylaştığımız her mesajı işleyen iletişim merkezleri olarak davranırlar. Bir kişinin akıllı telefonunu ele geçirirseniz, o kişinin hayatına kısıtlama olmaksızın erişim sağlarsınız. Mobil cihazların daha kolay kaybolduğunu veya çalındığını düşündüğümüzde ve mobil kötü amaçlı yazılımların artışıyla birlikte veri koruma ihtiyacı daha da belirgin hale geliyor.

Bu nedenle, mobil uygulamalar için bir güvenlik standardı, mobil uygulamaların hassas bilgileri nasıl işlediğine, depoladığına ve koruduğuna odaklanmalıdır. iOS ve Android gibi modern mobil işletim sistemleri, güvenli veri depolama ve iletişim için iyi API'ler sunsa da, bunların etkili olabilmeleri için doğru şekilde uygulanması ve kullanılması gerekir. Veri depolama, uygulamalar arası iletişim, kriptografik API'lerin uygun kullanımı ve güvenli ağ haberleşmesi, dikkatlice düşünülmesi gereken durumlardan yalnızca bazılarıdır.

Sektörde fikir birliğine ihtiyaç duyan önemli bir soru, verilerin gizliliğini ve bütünlüğünü korumak için tam olarak ne kadar ileri gidilmesi gerektiğidir. Örneğin, çoğumuz bir mobil uygulamanın TLS değişiminde sunucu sertifikasını doğrulaması gerektiğini kabul ederiz. Peki ya SSL sertifikası sabitleme? Bunu yapmamak bir güvenlik açığıyla sonuçlanmaz mı? Eğer bir uygulama hassas verileri işliyorsa bu bir gereklilik olmalı mı, yoksa ters etki yaratabilir mi? İşletim sistemi uygulamayı korumalı alana alsa bile SQLite veritabanlarında depolanan verileri şifrelememiz gerekiyor mu? Bir uygulama için uygun olan şey bir başkası için gerçekçi olmayabilir. MASVS, farklı tehdit senaryolarına uyan doğrulama seviyelerini kullanarak bu gereksinimleri standartlaştırma girişimidir.

Dahası, kök (root) zararlı yazılımlarının ve uzaktan yönetim araçlarının ortaya çıkması, mobil işletim sistemlerinin kendilerinin istismar edilebilir kusurları olduğu gerçeğine dair farkındalık yaratmıştır, bu nedenle, hassas verilere ek koruma sağlamak ve istemci tarafındaki müdahaleyi önlemek için konteynerleştirme stratejileri giderek daha fazla kullanılmaktadır. İşlerin karmaşıklaştığı yer de burasıdır. "Android for Work" ve "Samsung Knox" gibi donanım destekli güvenlik özellikleri ve işletim sistemi düzeyinde konteynerleştirme çözümleri mevcuttur, ancak bunlar farklı cihazlarda tutarlı bir şekilde kullanılamaz. Bir yara bandı olarak, yazılım tabanlı koruma önlemleri uygulamak mümkündür - ancak ne yazık ki, bu tür korumaları doğrulamak için standartlar veya test süreçleri yoktur.

Sonuç olarak, mobil uygulama güvenlik testi raporları her yerde: Örneğin, bazı test uzmanları bir Android uygulamasında kod karmaşıklaştırma veya root algılama eksikliğini "güvenlik açığı" olarak bildiriyor. Öte yandan, dizgi şifreleme, hata ayıklayıcı tespiti veya kontrol akışının gizlenmesi gibi önlemler zorunlu olarak düşünülmez. Bununla birlikte, bu iki taraflı bakış açısı mantıklı değildir çünkü "dayanıklık" iki taraftan da bir öneri değildir: Savunmayı amaçladığı belirli istemci taraflı tehditlere bağlıdır. Yazılım korumaları işe yaramaz değildir, ancak eninde sonunda atlanabilirler, bu nedenle asla güvenlik kontrollerinin yerine kullanılmamalıdır.

MASVS genel olarak, mobil uygulama güvenliği için bir temel sunmak (MASVS-L1), aynı zamanda derinlemesine savunma önlemlerinin (MASVS-L2) ve istemci taraflı tehditlere (MASVS-R) karşı korumaların dahil edilmesini hedefler. MASVS, aşağıdakileri gerçekleştirmeyi amaçlar:

- Güvenli mobil uygulamalar geliştirmek isteyen geliştiriciler ve yazılım mimarları için gereksinimleri sağlamak;
- Mobil uygulama güvenlik incelemelerinde test edilebilecek bir endüstri standardı sunmak;
- Yazılım koruma mekanizmalarının mobil güvenlikteki rolünü netleştirmek ve etkinliklerini doğrulamak için gereksinimleri sağlamak;
- Farklı kullanım durumları için hangi güvenlik seviyesinin tavsiye edildiğine dair spesifik öneriler sunmak.

%100 endüstri mutabakatına ulaşmanın imkansız olduğunun farkındayız. Yine de, MASVS'nin mobil uygulama geliştirme ve testlerinin tüm aşamalarında rehberlik sağlamada yararlı olacağını umuyoruz. Açık kaynak standardı olarak MASVS zamanla gelişecek ve her türlü katkı ve öneriyi memnuniyetle karşılıyoruz.

Bernhard Mueller tarafından