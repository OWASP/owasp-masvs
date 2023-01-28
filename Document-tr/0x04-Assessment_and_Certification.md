# Değerlendirme ve Sertifikasyon

## OWASP'ın MASVS Sertifikaları ve Güven Markaları Konusundaki Duruşu

OWASP, satıcıdan bağımsız, kar amacı gütmeyen bir kuruluş olarak, herhangi bir satıcıyı, sağlayıcı veya yazılımı onaylamaz.

Tüm bu tür güvence onayları, güven markaları veya sertifikaları OWASP tarafından resmi olarak incelenmemiş, tescil edilmemiş veya onaylanmamıştır, bu nedenle böyle bir görüşe dayanan bir kuruluşun (M)ASVS sertifikasyonu iddiasında bulunan herhangi bir üçüncü şahsa veya güven markasına duyulan güven konusunda dikkatli olması gerekir.

Bu, resmi OWASP sertifikası talep etmedikleri sürece, kuruluşların bu tür güvence hizmetleri sunmasını engellememelidir.

## Mobil Uygulamaları Onaylama Rehberi

Bir mobil uygulamanın MASVS ile uyumluluğunu doğrulamanın önerilen yolu bir "açık kitap" incelemesi yapmaktır, yani test uzmanlarına uygulamanın mimarları ve geliştiricileri, proje dokümantasyonu, kaynak kodu ve her rol için en az bir kullanıcı hesabına erişim dahil olmak üzere uç noktalara kimlik doğrulaması ile erişim gibi temel kaynaklara erişim izni verilmelidir.

MASVS'nin yalnızca (istemci tarafı) mobil uygulamanın güvenliğini ve uygulama ile uzak uç noktaları arasındaki ağ iletişimini, ayrıca kullanıcı kimlik doğrulaması ve oturum yönetimi ile ilgili birkaç temel ve genel gereksinimi kapsadığına dikkat etmek önemlidir. Yetkilendirme, kimlik doğrulama, kontrol doğrulama ve oturum yönetimi ile ilgili konularda sınırlı genel gereksinimler kümesi dışında, uygulama ile ilişkili uzak servisler (ör. Web servisler) için özel gereksinimler içermez. Ancak MASVS V1, uzak servislerin genel tehdit modeli tarafından kapsanması ve OWASP ASVS gibi uygun standartlara göre doğrulanması gerektiğini belirtir.

Sertifikalandırma kuruluşu, herhangi bir rapora doğrulama kapsamını (özellikle bir anahtar bileşen kapsam dışındaysa), başarılı ve başarısız testler dahil olmak üzere doğrulama bulgularının bir özetini, başarısız testlerin nasıl çözüleceğine dair net göstergeler dahil etmelidir. Detaylı çalışma kağıtları, ekran görüntüleri ya da ekran videoları, bulguyu güvenilir ve tekrarlanabilir biçinde sömürebilecek betikler, vekil sunucu (proxy) kayıtları ve temizleme prosedürüne yönelik notlar gibi elektronik kayıtlar standart endüstri uygulaması olarak kabul edilir. Sadece bir aracı çalıştırmak ve bulguları raporlamak yeterli değildir; bu, sertifikalandırma düzeyindeki tüm konuların kapsamlı ve uygun bir şekilde test edildiğine dair yeterli kanıt sağlamaz. Anlaşmazlık durumunda, doğrulanan her gereksinimin gerçekten test edildiğini gösteren yeterli destekleyici kanıt olmalıdır.

<!-- \pagebreak -->

### OWASP Mobile Security Testing Guide (MSTG) Kullanma

OWASP MSTG, mobil uygulamaların güvenliğini test etmeye yönelik bir kılavuzdur. MASVS'de listelenen gereksinimleri doğrulamak için teknik süreçleri açıklar. MSTG, her biri MASVS'deki bir gereksinimle eşleşen test senaryolarının bir listesini içerir. MASVS gereksinimleri üstten ve genel olmakla birlikte, MSTG, mobil işletim sistemine göre derinlemesine öneriler ve test prosedürleri sağlar.

### Otomatize Güvenlik Test Araçlarının Rolü

Mümkün olduğunda verimliliği artırmak için kaynak kod tarayıcılarının ve kara kutu (black-box) test araçlarının kullanılması teşvik edilmektedir. Bununla birlikte, MASVS doğrulamasını yalnızca otomatik araçları kullanarak tamamlamak mümkün değildir: Her mobil uygulama farklıdır ve uygulamada kullanılan belirli teknolojilerin ve çerçevelerin genel mimarisini, iş mantığını ve kullanılan spesifik teknolojilerin teknik tuzaklarını anlamak, uygulama güvenliğini doğrulamak için zorunlu bir gerekliliktir.

## Diğer Kullanımlar

### Ayrıntılı Güvenlik Mimarisi Rehberi olarak

MASVS'nin en yaygın kullanımlarından biri, güvenlik mimarları için bir kaynak olarak kullanımıdır. İki ana güvenlik mimarisi çerçevesi, SABSA veya TOGAF, mobil uygulama güvenlik mimarisi incelemelerini tamamlamak için gerekli olan çok fazla bilgiden yoksundur. MASVS, güvenlik mimarlarının mobil uygulamalarda ortak olan sorunlar için daha iyi kontroller seçmesine izin vererek bu boşlukları doldurmak için kullanılabilir.

### Kullanıma Hazır Güvenli Kodlama Kontrol Listelerinin Değiştirilmesi Olarak

Birçok kuruluş, MASVS'nin iki düzeyinden birini seçerek veya MASVS'yi klonlayarak ve her uygulamanın risk düzeyi için gerekenleri etki alanına özgü bir şekilde değiştirerek fayda sağlayabilir. İzlenebilirlik korunduğu sürece bu tür klonlamaları teşvik ederiz, böylece bir uygulama 4.1 gereksinimini geçerse, bu, standart geliştikçe klonlanan kopyalar için de aynı anlama gelir.

### Güvenlik Testi Metodolojilerinin Temeli Olarak

İyi bir mobil uygulama güvenlik testi metodolojisi, MASVS'de listelenen tüm gereksinimleri kapsamalıdır. OWASP Mobile Security Testing Guide (MSTG) her doğrulama gereksinimi için kara kutu (black-box) ve beyaz kutu (white-box) test durumlarını açıklar.

### Otomatik Birim ve Entegrasyon Testleri için Kılavuz Olarak

MASVS, mimari gereksinimler dışında, yüksek düzeyde test edilebilir olacak şekilde tasarlanmıştır. MASVS gereksinimlerine dayalı otomatik birim, entegrasyon ve kabul testi, sürekli geliştirme yaşam döngüsüne entegre edilebilir. Bu yalnızca geliştirici güvenlik farkındalığını artırmakla kalmaz, aynı zamanda ortaya çıkan uygulamaların genel kalitesini iyileştirir ve devreye alım öncesi aşamada güvenlik testi sırasında bulguların miktarını azaltır.

### Güvenli Geliştirme Eğitimi İçin

MASVS, güvenli mobil uygulamaların özelliklerini tanımlamak için de kullanılabilir. Çoğu "güvenli kodlama" kursu, üstünkörü bir şekilde kodlama ipuçlarına değinerek basitçe etik bilgisayar korsanlığı kurslarıdır. Bu, geliştiricilere yardımcı olmaz. Bunun yerine, güvenli geliştirme kursları örneğin en sık karşılaşılan 10 kod güvenlik bulgusuna odaklanmak yerine MASVS'de belgelenen proaktif kontrollere güçlü bir odaklanma ile MASVS'yi kullanabilir.
