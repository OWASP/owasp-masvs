# V3: Kriptografi Gereksinimleri

## Kontrol Hedefi

Kriptografi, bir mobil cihazda depolanan verilerin korunması söz konusu olduğunda önemli bir bileşendir. Aynı zamanda, özellikle standart kurallara uyulmadığında, işlerin korkunç şekilde ters gidebileceği bir kategoridir. Bu bölümdeki kontrollerin amacı, doğrulanmış uygulamanın, aşağıdakiler de dahil olmak üzere sektördeki en iyi uygulamalara göre kriptografi kullanmasını sağlamaktır:

- Kanıtlanmış kriptografik kütüphanelerin kullanımı;
- Kriptografik temellerin doğru seçimi ve konfigürasyonu;
- Rasgeleliğin gerekli olduğu her yerde uygun bir rasgele sayı üreteci.

## Güvenlik Doğrulama Gereksinimleri

| # | MSTG-ID | Description | L1 | L2 |
| -- | ---------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | Uygulama, tek şifreleme yöntemi olarak sabit kodlanmış anahtarlarla simetrik şifrelemeye dayanmaz. | x | x |
| **3.2** | MSTG-CRYPTO-2 | Uygulama, kriptografik temellerin, kanıtlanmış uygulamalarını kullanır. | x | x |
| **3.3** | MSTG-CRYPTO-3 | Uygulama, sektördeki en iyi uygulamalara uyan parametrelerle yapılandırılmış, belirli kullanım durumuna uygun kriptografik temel öğeleri kullanır. | x | x |
| **3.4** | MSTG-CRYPTO-4 | Uygulama, güvenlik nedeniyle yaygın olarak kullanımdan kaldırılan kriptografik protokolleri veya algoritmaları kullanmaz. | x | x |
| **3.5** | MSTG-CRYPTO-5 | Uygulama, aynı şifreleme anahtarını birden çok amaç için yeniden kullanmaz. | x | x |
| **3.6** | MSTG-CRYPTO-6 | Tüm rasgele değerler, yeterince güvenli bir rasgele sayı üreteci kullanılarak üretilir. | x | x |

## Referanslar

OWASP Mobile Security Testing Guide, bu bölümde listelenen gereksinimleri doğrulamak için ayrıntılı talimatlar sağlar.

- Android: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

Daha fazla bilgi için ayrıca bakınız:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>
