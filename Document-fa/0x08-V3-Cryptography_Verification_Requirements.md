<div dir="rtl" markdown="1">
# V3: نیازمندی های رمزنگاری

## هدف کنترل

رمزنگاری یک جزء ضروری در حفاظت از داده ذخیره شده در گوشی موبایل می باشد. همینطور بخش ایست که احتمال رخ دادن اشتباهات بزرگ در آن بسیار است، به خصوص هنگامی که از قرداد های استاندارد تبعیت نشود. هدف کنترل ها در این بخش این است که اطمینان حاصل کنند برنامه تایید شده، از رمزنگاری طبق بهترین روش های صنعتی استفاده می کند، که شامل موارد زیر می شود:
-	استفاده از کتابخانه های رمزنگاری ثابت شده؛
-	انتخاب و پیکربندی مناسب بدوی های رمزنگاری؛
-	تولید یک عدد تصادفی مناسب هر گاه که تصادفی بودن مورد نیاز است؛


## Security Verification Requirements

| # | شناسه-آزمون امنیتی برنامۀ کاربردی موبایل | شرح | سطح یک | سطح دو |
| -- | -------- | ---------------------- | - | - |
| **3.1** | MSTG-CRYPTO-1 | برنامه بر رمزنگاری متقارن با کلید های hardcoded، به عنوان تنها روش رمزگذاری، تکیه نمی کند.| ✓ | ✓ |
| **3.2** | MSTG-CRYPTO-2 | برنامه از پیاده سازی های ثابت شده ی بدوی های رمزنگاری استفاده می کند. | ✓ | ✓ |
| **3.3** | MSTG-CRYPTO-3 | برنامه از بدوی های رمزنگاری استفاده می کند که برای مورد استفاده خاص مناسب هستند، که با پارامتر هایی که به بهترین روش های صنعتی پایبند هستند، پیکربندی شده اند.  | ✓ | ✓ |
| **3.4** | MSTG-CRYPTO-4 | برنامه از پروتکل ها یا الگوریتم های رمزنگاری که به دلایل امنیتی به آن ها بها داده نمی شود و مورد استفاده قرار نمی گیرند، استفاده نمی کند. | ✓ | ✓ |
| **3.5** | MSTG-CRYPTO-5 | برنامه از کلید رمزنگاری یکسان برای چندین عمل، استفاده دوباره نمی کند. | ✓ | ✓ |
| **3.6** | MSTG-CRYPTO-6 | تمام مقدار های تصادفی با استفاده از عدد های تصادفی که به اندازه کافی امن هستند، ایجاد شده اند. | ✓ | ✓ |

## منابع

راهنمای تست امنیتی موبایل OWASP، دستورالعمل هایی مفصل برای تایید نیازمندی های لیست شده در این بخش، فراهم می کند.

- Android: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05e-Testing-Cryptography.md>
- iOS: Testing Cryptography - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06e-Testing-Cryptography.md>

For more information, see also:

- OWASP Mobile Top 10: M5 (Insufficient Cryptography) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m5-insufficient-cryptography>
- CWE 310 (Cryptographic Issues) - <https://cwe.mitre.org/data/definitions/310.html>
- CWE 321 (Use of Hard-coded Cryptographic Key) - <https://cwe.mitre.org/data/definitions/321.html>
- CWE 326 (Inadequate Encryption Strength) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (Use of a Broken or Risky Cryptographic Algorithm) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 329 (Not Using a Random IV with CBC Mode) - <https://cwe.mitre.org/data/definitions/329.html>
- CWE 330 (Use of Insufficiently Random Values) - <https://cwe.mitre.org/data/definitions/330.html>
- CWE 337 (Predictable Seed in PRNG) - <https://cwe.mitre.org/data/definitions/337.html>
- CWE 338 (Use of Cryptographically Weak Pseudo Random Number Generator (PRNG)) - <https://cwe.mitre.org/data/definitions/338.html>

</div>
