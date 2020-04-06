<div dir="rtl" markdown="1">
# V4: نیازمندی‌های تصدیق هویت و مدیریت نشست

## اهداف کنترل

در بیشتر موارد، ورود کاربران به یک سرویس از راه دور بخشی جدایی ناپذیر از معماری کلی برنامه موبایل است. حتی اگر بیشتر منطق در نقطه پایانی رخ دهد. MASVS برخی نیازمندی‌های پایه در مورد چگونگی مدیریت نشست‌ها و حساب‌های کاربری را تعریف می‌نماید.

## نیازمندی‌های تأیید امنیتی

| # | شناسه-آزمون امنیتی برنامۀ کاربردی موبایل | شرح | سطح یک | سطح دو |
| -- | -------- | ---------------------- | - | - |
| **4.1** | MSTG-AUTH-1 | اگر برنامه کاربردی برای کاربران دسترسی به یک سرویس از راه دور را فراهم می‌کند، نوعی تصدیق هویت همانند نام کاربری و کلمه عبور باید در نقطه پایانه راه دور انجام شود. | ✓ | ✓ |
| **4.2** | MSTG-AUTH-2 | اگر از مدیریت نشست stateful استفاده شده است، نقطه پایانی از راه دور باید بدون ارسال ابزارهای احراز هویت کاربر از شناسه‌های نشست تولید شده به طور تصادفی برای تصدیق هویت درخواست‌های کلاینت استفاده کند. | ✓ | ✓ |
| **4.3** | MSTG-AUTH-3 | اگر از تصدیق هویت مبتنی بر توکن stateless استفاده شده است، سرور باید توکنی را ارائه دهد که توسط یک الگوریتم امن امضا شده باشد. | ✓ | ✓ |
| **4.4** | MSTG-AUTH-4 | وقتی کاربر از سیستم خارج می‌شود، نقطه پایانی راه دور نشست فعلی را پایان می‌دهد. | ✓ | ✓ |
| **4.5** | MSTG-AUTH-5 | یک سیاست کلمه عبور وجود دارد و در سمت پایانی اعمال می‌شود. | ✓ | ✓ |
| **4.6** | MSTG-AUTH-6 | نقطه پایانی مکانیزمی را برای محافظت در برابر وارد کردن اطلاعات احراز هویت نادرست به دفعات زیاد پیاده سازی می‌کند. | ✓ | ✓ |
| **4.7** | MSTG-AUTH-7 | نشست‌ها پس از مدتی عدم فعالیت یا منقضی شدن توکن‌های دسترسی در سمت پایانی نامعتبر می‌شوند. | ✓ | ✓ |
| **4.8** | MSTG-AUTH-8 | تصدیق هویت بیومتریک نباید محدود به یک رویداد باشد (به عنوان نمونه استفاده از یک API که تنها True و False را باز می‌گرداند). به جای این، باید بر اساس گشودن keychain یا keystore باشد. | | ✓ |
| **4.9** | MSTG-AUTH-9 | مرحله دومی از تصدیق هویت در نقطه پایانی وجود داشته باشد و نیازمندی‌های تصدیق هویت دو مرحله‌ای همواره الزامی باشند.  | | ✓ |
| **4.10** | MSTG-AUTH-10 | تراکنش‌های حساس نیازمند تصدیق هویت مرحله به مرحله باشند. | | ✓ |
| **4.11** | MSTG-AUTH-11 | برنامه کاربردی کاربر را نسبت به تمام فعالیت‌های ورود به سیستم با حساب وی آگاه می‌سازد. کاربران قادرند لیستی از دستگاه‌هایی که از آن‌ها برای دسترسی به حساب استفاده شده است را مشاهده کنند و دستگاه‌های خاصی را مسدود نمایند. | | ✓ |
| **4.12** | MSTG-AUTH-12 | مدل‌های مجوز باید در سمت پایانی تعریف شده و اجباری شوند. | ✓ | ✓ |

## منابع

راهنمای آزمون امنیت موبایل ،OWASP دستورالعمل‌های دقیق برای تایید نیازمندی‌های لیست شده در بالا را ارائه می‌دهد.

- General: Authentication and Session Management - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x04e-Testing-Authentication-and-Session-Management.md>
- Android: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05f-Testing-Local-Authentication.md>
- iOS: Testing Local Authentication - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06f-Testing-Local-Authentication.md>

برای اطلاعات بیشتر همچنین مشاهده کنید:

- OWASP Mobile Top 10: M4 (Insecure Authentication) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m4-insecure-authentication>
- OWASP Mobile Top 10: M6 (Insecure Authorization) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m6-insecure-authorization>
- CWE 287 (Improper Authentication) - <https://cwe.mitre.org/data/definitions/287.html>
- CWE 307 (Improper Restriction of Excessive Authentication Attempts) - <https://cwe.mitre.org/data/definitions/307.html>
- CWE 308 (Use of Single-factor Authentication) - <https://cwe.mitre.org/data/definitions/308.html>
- CWE 521 (Weak Password Requirements) - <https://cwe.mitre.org/data/definitions/521.html>
- CWE 604 (Use of Client-Side Authentication) - <https://cwe.mitre.org/data/definitions/604.html>
- CWE 613 (Insufficient Session Expiration) - <https://cwe.mitre.org/data/definitions/613.html>

</div>
