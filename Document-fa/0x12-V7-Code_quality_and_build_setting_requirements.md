<div dir="rtl" markdown="1">
# V7: نیازمندی های کیفیت کد و تنظیمات ساخت

## هدف کنترل

هدف از این کنترل این است که اطمینان حاصل کند شیوه های کد زنی امنیتی پایه در توسعه برنامه رعایت می شوند، و امکانات امنیتی "رایگان" که توسط کامپایلر ارائه می شوند، فعال می باشند.  

## نیازمندی‌های وارسی امنیت

| # | MSTG-ID | شرح  | سطح یک | سطح دو |
| -- | -------- | ---------------------- | - | - |
| **7.1** | MSTG-CODE-1 | برنامه توسط گواهینامه معتبر امضا و تامین شده است، که در آن از کلید خصوصی به درستی محافظت شده است. | ✓ | ✓ |
| **7.2** | MSTG-CODE-2 |  برنامه در حالت انتشار ساخته شده است، همراه با تنظیمات مناسب برای یک ساخت انتشار | ✓ | ✓ |
| **7.3** | MSTG-CODE-3 | علائم اشکال زدایی از باینری های بومی حذف شده اند. | ✓ | ✓ |
| **7.4** | MSTG-CODE-4 | کد اشکال زدایی و کد دستیار توسعه دهنده حذف شده باشد(به عنوان نمونه کد آزمایشی، درب‌های پشتی، تنظیمات مخفی)، و برنامه خطاها یا پیغام های اشکال زدایی طولانی را ثبت نمی کند. | ✓ | ✓ |
| **7.5** | MSTG-CODE-5 | تمامی مؤلفه‌های شخص ثالث مورد استفاده برنامه موبایل، همچون کتابخانه‌ها و چارچوب‌ها، شناسایی شده‌اند، و برای داشتن آسیب پذیری ها شناخته شده بررسی می شوند. | ✓ | ✓ |
| **7.6** | MSTG-CODE-6 | برنامه استثنائات احتمالی را رسیدگی کرده و آنها را مدیریت می‌کند.| ✓ | ✓ |
| **7.7** | MSTG-CODE-7 | منطق مدیریت خطا در کنترل‌های امنیتی، به صورت پیش‌فرض، دسترسی را منع می‌کند. | ✓ | ✓ |
| **7.8** | MSTG-CODE-8 | در کد مدیریت نشده، حافظه، به صورت ایمن اختصاص داده شده، آزاد و استفاده می شود.  | ✓ | ✓ |
| **7.9** | MSTG-CODE-9 | امکانات امنیتی رایگان ارائه شده توسط زنجیره ابزار، همچون کوچک سازی byte-code، محافظت از پشته، پشتیبانی از PIE و شمارنده ارجاع خودکار، فعال می باشند. | ✓ | ✓ |

## منابع

راهنمای وارسی امنیتی موبایل OWASP، دستورالعمل هایی مفصل برای تایید نیازمندی های لیست شده در این بخش، فراهم می کند.

- Android: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05i-Testing-Code-Quality-and-Build-Settings.md>
- iOS: Testing Code Quality and Build Settings - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06i-Testing-Code-Quality-and-Build-Settings.md>

برای اطلاعات بیشتر، مشاهده کنید:

- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 89 (Improper Neutralization of Special Elements used in an SQL Command) - <https://cwe.mitre.org/data/definitions/89.html>
- CWE 95 (Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')) - <https://cwe.mitre.org/data/definitions/95.html>
- CWE 119 (Improper Restriction of Operations within the Bounds of a Memory Buffer) - <https://cwe.mitre.org/data/definitions/119.html>
- CWE 215 (Information Exposure through Debug Information) - <https://cwe.mitre.org/data/definitions/215.html>
- CWE 388 (7PK - Errors) - <https://cwe.mitre.org/data/definitions/388.html>
- CWE 489 (Leftover Debug Code) - <https://cwe.mitre.org/data/definitions/489.html>
- CWE 502 (Deserialization of Untrusted Data) - <https://cwe.mitre.org/data/definitions/502.html>
- CWE 511 (Logic/Time Bomb) - <https://cwe.mitre.org/data/definitions/511.html>
- CWE 656 (Reliance on Security through Obscurity) - <https://cwe.mitre.org/data/definitions/656.html>
- CWE 676 (Use of Potentially Dangerous Function)  - <https://cwe.mitre.org/data/definitions/676.html>
- CWE 937 (OWASP Top Ten 2013 Category A9 - Using Components with Known Vulnerabilities) - <https://cwe.mitre.org/data/definitions/937.html>

</div>
