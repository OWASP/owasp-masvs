<div dir="rtl" markdown="1">

# V6: نیازمندی‌های تعامل با پلتفرم

## هدف کنترل

کنترل‌های این گروه اطمینان حاصل می‌کنند که برنامه کاربردی از API مربوط به پلتفرم و مؤلفه‌های استاندارد به طورت امن استفاده می‌کند. علاوه بر این، این کنترل‌ها ارتباطات بین برنامه‌های کاربردی (IPC) را کنترل می‌نماید.

## نیازمندی‌های وارسی امنیت

| # | MSTG-ID | Description | L1 | L2 |
| -- | -------- | ---------------------- | - | - |
| **6.1** | MSTG-PLATFORM-1 | برنامه کاربردی نیازمند حداقل سطح دسترسی‌های ضروری است. | ✓ | ✓ |
| **6.2** | MSTG-PLATFORM-2 | تمام ورودی‌ها از منابع خارجی و کاربر اعتبارسنجی شده و اگر ضروری بود به خوبی بررسی شوند. این شامل داده‌های دریافت شده از رابط کاربری، مکانیزم‌های IPC از قبیل intent ها، URL  های اختصاصی و منابع شبکه می‌باشد. | ✓ | ✓ |
| **6.3** | MSTG-PLATFORM-3 | برنامه کاربردی عملکردهای حساس را از طریق طرح‌های URL اختصاصی صادر نمی‌کند مگر اینکه این مکانیزم‌ها به درستی محافظت شده باشند. | ✓ | ✓ |
| **6.4** | MSTG-PLATFORM-4 | برنامه کاربردی عملکرد حساس را از طریق امکانات IPC صادر نمی‌کند مگر اینکه این مکانیزم‌ها به درستی محافظت شده باشند. | ✓ | ✓ |
| **6.5** | MSTG-PLATFORM-5 | جاوا اسکریپت در WebView ها غیر فعال شده است مگر اینکه به صراحت مورد نیاز باشد. | ✓ | ✓ |
| **6.6** | MSTG-PLATFORM-6 | WebView ها طوری پیکربندی شده‌اند که مجموعه حداقلی از protocol handler های مورد نیاز را اجازه دهند (به طور ایده آل تنها HTTPS پشتیبانی شود). protocol handler های به طور بالقوه خطرناک از قبیل file ، tel و app-id غیر فعال باشند. | ✓ | ✓ |
| **6.7** | MSTG-PLATFORM-7 | اگر متدهای native برنامه در معرض یک WebView هستند، بررسی کنید که WebView تنها جاوا اسکریپت قرار داده شده در بسته برنامه کاربردی را render می‌کند. | ✓ | ✓ |
| **6.8** | MSTG-PLATFORM-8 | Object deserialization در صورت وجود داشتن توسط API های امن توالی سازی پیاده سازی شده باشد. | ✓ | ✓ |
| **6.9** | MSTG-PLATFORM-9 | اپلیکیشن از خود در برابر حملات screen overlay محافظت می‌کند. (فقط سیستم عامل اندروید) |  | ✓ |
| **6.10** | MSTG-PLATFORM-10 | حافظه نهان، حافظه ذخیره‌سازی و منابع لود شده (جاوا اسکریپت و غیره) باید قبل از نابود شدن WebView پاک شوند. |  | ✓ |
| **6.11** | MSTG-PLATFORM-11 | وارسی کنید که برنامه کاربردی موقع وارد کردن اطلاعات حساس از استفاده صفحه کلیدهای شخص ثالث جلوگیری می‌کند. | | ✓ |

## منابع

راهنمای وارسی امنیتی موبایل OWASP، دستورالعمل‌هایی مفصل برای تایید نیازمندی‌های لیست شده در این بخش، فراهم می کند.

- Android: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md>
- iOS: Testing Platform Interaction - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md>

برای اطلاعات بیشتر همچنین مشاهده کنید:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M7 (Poor Code Quality) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m7-client-code-quality>
- CWE 20 (Improper Input Validation) - <https://cwe.mitre.org/data/definitions/20.html>
- CWE 79 (Improper Neutralization of Input During Web Page Generation) - <https://cwe.mitre.org/data/definitions/79.html>
- CWE 200 (Information Leak / Disclosure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 250 (Execution with Unnecessary Privileges) - <https://cwe.mitre.org/data/definitions/250.html>
- CWE 672 (Operation on a Resource after Expiration or Release) - <https://cwe.mitre.org/data/definitions/672.html>
- CWE 749 (Exposed Dangerous Method or Function) - <https://cwe.mitre.org/data/definitions/749.html>
- CWE 772 (Missing Release of Resource after Effective Lifetime) - <https://cwe.mitre.org/data/definitions/772.html>
- CWE 920 (Improper Restriction of Power Consumption) - <https://cwe.mitre.org/data/definitions/920.html>
- CWE 925 (Improper Verification of Intent by Broadcast Receiver) - <https://cwe.mitre.org/data/definitions/925.html>
- CWE 926 (Improper Export of Android Application Components) - <https://cwe.mitre.org/data/definitions/926.html>
- CWE 927 (Use of Implicit Intent for Sensitive Communication) - <https://cwe.mitre.org/data/definitions/927.html>
- CWE 939 (Improper Authorization in Handler for Custom URL Scheme) - <https://cwe.mitre.org/data/definitions/939.html>

</div>
