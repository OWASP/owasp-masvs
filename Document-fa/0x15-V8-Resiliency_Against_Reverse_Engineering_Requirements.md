<div dir="rtl" markdown="1">
# V8: نیازمندی‌های انعطاف‌پذیری

## هدف کنترل

این بخش معیارهای دفاع در عمق توصیه شده برای اپلیکیشن‌هایی که اطلاعات حساس را پردازش کرده یا دسترسی به عملکرد یا اطلاعات حساس را فراهم می‌کنند را پوشش می‌دهد. نبود این کنترل‌ها باعث ایجاد آسیب‌پذیری نمی‌شود بلکه این کنترل‌ها به منظور افزایش انعطاف‌پذیری برنامه کاربردی در مقابل مهندسی معکوس و حملات خاص سمت کلاینت در نظر گرفته شده‌اند.

کنترل‌های این بخش باید بنا به نیاز و بر اساس ارزیابی مخاطرات به وجود آمده توسط دستکاری غیرمجاز برنامه و یا مهندسی معکوس کد اعمال شوند. برای مشاهده لیستی از مخاطرات کسب و کار و همچنین تهدیدات فنی مربوطه، پیشنهاد می‌کنیم که به سند OWASP با عنوان "مخاطرات فنی مهندسی معکوس و مهندسی معکوس تغییر غیر مجاز کد و جلوگیری از تغییر کد" مراجعه شود. (مراجع پایین را مشاهده کنید) 

برای اینکه هر یک از کنترل‌های فهرست شده در لیست زیر مؤثر واقع شوند، اپلیکیشن باید حداقل تمام سطح یک MASVS  (یعنی کنترل‌های مستهکم امنیتی باید در سر جای خود باشند) و همچنین تمام نیازمندی‌های شماره‌گذاری شده با عدد پایین‌تر در V8 را برآورده سازد. به عنوان مثال، کنترل‌های obfuscation فهرست شده در زیر قسمت "منع درک مطلب" باید همراه با "منع تجزیه و تحلیل پویا و دستکاری" و "انقیاد دستگاه" ترکیب شوند.

**توجه کنید که محافظت‌های نرم‌افزاری نباید هرگز به عنوان جایگزینی برای کنترل‌های امنیتی استفاده شوند. کنترل‌های فهرست شده در MASVR-R به منظور اضافه کردن کنترل‌های محافظتی اضافی و مربوط به تهدیدات خاص به برنامه‌هایی که نیازمندی‌های امنیتی MASVS را برآورده می‌کنند قرار داده شده‌اند. **

ملاحظات زیر قابل اجرا هستند:

1. یک مدل تهدید باید تعریف شود  که به طور روشن طرح کلی تهدیدات سمت کاربر که قرار است تعریف شوند را مشخص می‌کند. علاوه بر این، درجه محافظتی که طرح قرار است ارائه دهد باید مشخص شود. به عنوان مثال، یک هدف ذکر شده می‌تواند این باشد که سازندگان بدافزار هدف که به دنبال سوء استفاده از اپلیکیشن هستند را مجبور کنیم که برای مهندسی معکوس تلاش زیادی را متحمل شوند.

2. مدل تهدید باید معتبر و مناسب باشد. به عنوان مثال اگر یک مهاجم بتواند به راحتی کل جعبه سفید را سرقت کند، مخفی کردن یک کلید رمزنگاری در یک پیاده سازی جعبه سفید ممکن است کاری زائد باشد.

3. اثربخشی محافظت باید همیشه توسط یک متخصص انسانی دارای که داری تجربه در زمینه راه‌های جلوگیری از دستکاری برنامه و obfuscation است وارسی و تأیید شود (همچنین به بخش‌های "مهندسی معکوس" و "ارزیابی محافظت‌های نرم‌افزاری" از راهنمای آزمون امنیت موبایل مراجعه کنید).

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

### منع تجزیه و تحلیل پویا و دستکاری برنامه

| # | MSTG-ID | شرح | R |
| -- | -------- | ---------------------- | - |
| **8.1** | MSTG-RESILIENCE-1 | The app detects, and responds to, the presence of a rooted or jailbroken device either by alerting the user or terminating the app. | ✓ |
| **8.2** | MSTG-RESILIENCE-2 | The app prevents debugging and/or detects, and responds to, a debugger being attached. All available debugging protocols must be covered. | ✓ |
| **8.3** | MSTG-RESILIENCE-3 | The app detects, and responds to, tampering with executable files and critical data within its own sandbox. | ✓ |
| **8.4** | MSTG-RESILIENCE-4 | The app detects, and responds to, the presence of widely used reverse engineering tools and frameworks on the device.| ✓ |
| **8.5** | MSTG-RESILIENCE-5 | The app detects, and responds to, being run in an emulator.  | ✓ |
| **8.6** | MSTG-RESILIENCE-6 | The app detects, and responds to, tampering the code and data in its own memory space. | ✓ |
| **8.7** | MSTG-RESILIENCE-7 | The app implements multiple mechanisms in each defense category (8.1 to 8.6). Note that resiliency scales with the amount, diversity of the originality of the mechanisms used. | ✓ |
| **8.8** | MSTG-RESILIENCE-8 | The detection mechanisms trigger responses of different types, including delayed and stealthy responses. | ✓ |
| **8.9** | MSTG-RESILIENCE-9 | Obfuscation is applied to programmatic defenses, which in turn impede de-obfuscation via dynamic analysis.  | ✓ |

### Device Binding

| # | MSTG-ID | Description | R |
| -- | -------- | ---------------------- | - |
| **8.10** | MSTG-RESILIENCE-10 | The app implements a 'device binding' functionality using a device fingerprint derived from multiple properties unique to the device. | ✓ |

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

### Impede Comprehension

| # | MSTG-ID | Description | R |
| -- | -------- | ---------------------- | - |
| **8.11** | MSTG-RESILIENCE-11 |All executable files and libraries belonging to the app are either encrypted on the file level and/or important code and data segments inside the executables are encrypted or packed. Trivial static analysis does not reveal important code or data. | ✓ |
| **8.12** | MSTG-RESILIENCE-12 | If the goal of obfuscation is to protect sensitive computations, an obfuscation scheme is used that is both appropriate for the particular task and robust against manual and automated de-obfuscation methods, considering currently published research. The effectiveness of the obfuscation scheme must be verified through manual testing. Note that hardware-based isolation features are preferred over obfuscation whenever possible. | ✓ |

### Impede Eavesdropping

| # | MSTG-ID | Description | R |
| -- | -------- | ---------------------- | - |
| **8.13** | MSTG-RESILIENCE-13 | As a defense in depth, next to having solid hardening of the communicating parties, application level payload encryption can be applied to further impede eavesdropping. | ✓ |

<div style="page-break-after: always; visibility: hidden">
\pagebreak
</div>

## References

The OWASP Mobile Security Testing Guide provides detailed instructions for verifying the requirements listed in this section.

- Android: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md>
- iOS: Testing Resiliency Against Reverse Engineering - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md>

For more information, see also:

- OWASP Mobile Top 10: M8 (Code Tampering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m8-code-tampering>
- OWASP Mobile Top 10: M9 (Reverse Engineering) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m9-reverse-engineering>
- OWASP Reverse Engineering Threats - <https://wiki.owasp.org/index.php/Technical_Risks_of_Reverse_Engineering_and_Unauthorized_Code_Modification>
- OWASP Reverse Engineering and Code Modification Prevention - <https://wiki.owasp.org/index.php/OWASP_Reverse_Engineering_and_Code_Modification_Prevention_Project>

</div>
