<div dir="rtl" markdown="1">

# V5: الزامات ارتباطات شبکه

## هدف کنترل

هدف کنترل‌های فهرست شده در این بخش، این است که از محرمانگی و یکپارچگی اطلاعات مبادله شده میان برنامه موبایل و پایانه‌های سرویس از راه دور، اطمینان حاصل گردد. در حداقل شرایط، یک برنامه موبایل باید کانالی امن و رمزنگاری شده برای ارتباطات شبکه با استفاده از پروتکل TLS با تنظیمات مناسب، ایجاد کند. سطح دو، اقدامات اضافی دفاع عمیق، مانند SSL pinning را لیست می‌کند.

## الزامات وارسی امنیت

| # | MSTG-ID | شرح | سطح یک | سطح دو |
| -- | -------- | ---------------------- | - | - |
| **5.1** | MSTG-NETWORK-1 | داده با استفاده از TLS روی شبکه رمزگذاری می‌شود. کانال امن در طول برنامه، همواره استفاده می‌شود. | ✓ | ✓ |
| **5.2** | MSTG-NETWORK-2 | تنظیمات TLS با بهترین روش‌های حال حاضر مطابقت دارند، و یا اگر سیستم عامل موبایل از استانداردهای پیشنهادی پشتیبانی نمی‌کند، تنظیمات TLS تا جای ممکن با آنها مشابهت داشته باشد. | ✓ | ✓ |
| **5.3** | MSTG-NETWORK-3 | برنامه، گواهینامه X.509 پایانه‌ از راه‌دور را هنگامی که کانال امن ایجاد شود، وارسی می‌کند. تنها گواهینامه‌های امضا شده توسط CA مطمئن قابل قبول می‌باشند. | ✓ | ✓ |
| **5.4** | MSTG-NETWORK-4 | برنامه یا از Certificate Store خودش استفاده می‌کند، یا گواهینامه‌ی پایانه یا کلید عمومی را پین می‌کند، و متعاقبا اتصالات به پایانه‌هایی که گواهینامه یا کلید متفاوتی دارند را ایجاد نمی‌کند، حتی اگر آن گواهینامه توسط CA مطمئن امضا شده باشد. |   | ✓ |
| **5.5** | MSTG-NETWORK-5 | برنامه تنها بر یک کانال ناامن ارتباطی (ایمیل یا پیامک) برای عملیات‌های بسیار مهم مانند ثبت نام‌ها و بازگردانی حساب، تکیه نمی‌کند. |  | ✓ |
| **5.6** | MSTG-NETWORK-6 | برنامه تنها بر کتابخانه‌های امنیت و اتصال که به روز می‌باشند، متکی می‌باشد. |  | ✓ |

## منابع

راهنمای وارسی امنیتی موبایل OWASP، دستورالعمل‌هایی مفصل برای تایید الزامات لیست شده در این بخش، فراهم می‌کند.

- عمومی: تست ارتباطات شبکه - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04f-Testing-Network-Communication.md>
- Android: تست ارتباطات شبکه - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md>
- iOS: تست ارتباطات شبکه - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md>

برای اطلاعات بیشتر، مشاهده کنید:

- OWASP Mobile Top 10: M3 (ارتباطات نا امن) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m3-insecure-communication>
- CWE 295 (اعتبار سنجی نادرست گواهی نامه) - <https://cwe.mitre.org/data/definitions/295.html>
- CWE 296 (پیروی ناصحیح از زنجیره‌ی اطمینان گواهی نامه) - <https://cwe.mitre.org/data/definitions/296.html>
- CWE 297 (صحت سنجی نادرست گواهینامه با میزبان اشتباه) - <https://cwe.mitre.org/data/definitions/297.html>
- CWE 298 (اشتباه در اعتبار سنجی انقضاء گواهی نامه) - <https://cwe.mitre.org/data/definitions/298.html>
- CWE 308 (استفاده از احراز هویت یک مرحله‌ای) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 319 (انتقال اطلاعات مهم به صورت متنی واضح) - <https://cwe.mitre.org/data/definitions/319.html>
- CWE 326 (استحکام ناکافی در رمزنگاری) - <https://cwe.mitre.org/data/definitions/326.html>
- CWE 327 (استفاده از الگوی رمزنگاری منقضی شده یا پرخطر) - <https://cwe.mitre.org/data/definitions/327.html>
- CWE 780 (استفاده از الگوی RSA بدون OAEP) - <https://cwe.mitre.org/data/definitions/780.html>
- CWE 940 (اشتباه در صحت سنجی منبع کانال ارتباطی) - <https://cwe.mitre.org/data/definitions/940.html>
- CWE 941 (مشخص سازی اشتباه منبع در یک کانال ارتباطی) - <https://cwe.mitre.org/data/definitions/941.html>

</div>
