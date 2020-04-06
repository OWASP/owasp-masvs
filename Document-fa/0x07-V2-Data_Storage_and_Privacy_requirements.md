<div dir="rtl" markdown="1">

# V2: نیازمندی‌های ذخیره داده و حریم خصوصی

## هدف کنترل

حفاظت از داده‌های حساس، از قبیل ابزارهای احراز هویت و اطلاعات خصوصی، یک نقطه تمرکز کلیدی در امنیت موبایل است.  در مرحله اول اگر مکانیزم‌های سیستم عامل همانند IPC به طور نامناسب استفاده شوند، ممکن است اطلاعات حساس به طور سهوی در معرض دسترسی سایر اپلیکیشن‌های موجود بر روی همان دستگاه قرار گیرند. همچنین ممکن است که داده‌ها به طور اشتباه بر روی حافظه ابری، پشتیبان یا حافظه کش صفحه کلید نشت کنند. علاوه بر این، دستگاه‌های موبایل در مقایسه با سایر انواع دستگاه‌ها می‌توانند راحت‌تر مفقود شده یا مورد سرقت قرار بگیرند، بنابراین سناریوی دسترسی فیزیکی یک شخص متخاصم محتمل‌تر است. در این صورت یک سری محافظت‌های اضافی می‌توانند پیاده‌سازی شوند تا دسترسی به داده‌ها دشوارتر گردد.
توجه داشته باشید که از آنجایی که MASVS بر اپلیکیشن متمرکز می‌باشد، این استاندارد سیاست‌های الزام شده سطح دستگاه توسط MDM را تحت پوشش قرار نمی‌دهد.


### تعریف داده حساس

داده حساس در چارچوب MASVS هم مربوط به ابزارهای احراز هویت کاربر است و هم هرگونه داده دیگر که در یک چارچوب خاص حساس در نظر گرفته می‌شود از قبیل:
-	اطلاعات قابل شناسایی خصوصی  (PII) که می‌توانند توسط دزدی هویت مورد سوء استفاده قرار بگیرند: شماره‌های تأمین اجتماعی، شماره‌های کارت اعتباری، شماره‌های حساب بانکی و اطلاعات بهداشتی.
-	اطلاعات بسیار حساس که در صورت به خطر افتادن می‌توانند منجر به آسیب به سابقه شخصی یا خسارت‌های مالی شوند.
-	هرگونه داده‌ای که باید توسط قانون و یا به دلایل انطباق محافظت شود.


## نیازمندی‌های وارسی امنیت

اکثریت قریب به اتفاق مسائل افشای اطلاعات می‌توانند با پیروی از قوانین ساده زیر پیشگیری شوند. بیشتر کنترل‌های فهرست شده در این فصل برای تمام سطوح تایید الزامی هستند.

| # | MSTG-ID | شرح | سطح یک | سطح دو |
| -- | -------- | ---------------------- | - | - |
| **2.1** | MSTG-STORAGE-1 | امکانات ذخیره‌سازی ابزارهای احراز هویت سیستم برای ذخیره‌سازی اطلاعات حساس از قبیل PII، ابزارهای تصدیق هویت کاربر یا کلید‌های رمزنگاری به طور مناسب استفاده شده باشند. | ✓ | ✓ |
| **2.2** | MSTG-STORAGE-2 | هیچ اطلاعات حساسی نباید خارج از کانتینر برنامه یا امکانات ذخیره‌سازی ابزارهای احراز هویت سیستم ذخیره شود. | ✓ | ✓ |
| **2.3** | MSTG-STORAGE-3 | هیچ اطلاعات حساسی نباید در لاگ‌های برنامه‌ها نوشته شود. | ✓ | ✓ |
| **2.4** | MSTG-STORAGE-4 | هیچ اطلاعات حساسی نباید با اشخاص ثالث به اشتراک گذاشته شود مگر اینکه بخشی ضروری از معماری باشد. | ✓ | ✓ |
| **2.5** | MSTG-STORAGE-5 | حافظه کش صفحه کلید برای ورودی‌های متنی که شامل اطلاعات حساس است غیر فعال شده باشد. | ✓ | ✓ |
| **2.6** | MSTG-STORAGE-6 | هیچ اطلاعات حساسی توسط مکانیزم IPC فاش نشود. | ✓ | ✓ |
| **2.7** | MSTG-STORAGE-7 | هیچ اطلاعات حساسی از قبیل کلمات عبور یا پین‌ها توسط رابط کاربری فاش نشوند. | ✓ | ✓ |
| **2.8** | MSTG-STORAGE-8 | هیچ اطلاعات حساسی در فایل‌های پشتیبان تولید شده توسط سیستم عامل موبایل وجود نداشته باشد. |   | ✓ |
| **2.9** | MSTG-STORAGE-9 | وقتی برنامه کاربردی وارد پس‌ضمینه می‌شود باید  اطلاعات حساس را از view ها پاک کند. |  | ✓ |
| **2.10** | MSTG-STORAGE-10 | اپلیکیشن اطلاعات حساس را بیش از میزان ضروری در حافظه نگهداری نکند و حافظه پس از استفاده صریحاً پاک شود. |  | ✓ |
| **2.11** | MSTG-STORAGE-11 | اپلیکیشن یک سیاست device-access-security حداقلی را الزامی نماید از جمله الزام کاربر به تنظیم یک کد عبور دستگاه. |  | ✓ |
| **2.12** | MSTG-STORAGE-12 | اپلیکیشن کاربر را در مورد انواع اطلاعات شخصی قابل شناسایی پردازش شده و همچنین بهترین شیوه‌های امنیتی که کاربر باید در استفاده از برنامه دنبال نماید آموزش دهد. |  | ✓ |
| **2.13** | MSTG-STORAGE-13 | هیچ داده حساسی نباید به طور محلی بر روی دستگاه موبایل ذخیره شود. بلکه داده در موقع نیاز باید از یک نقطه پایانی راه دور دریافت شده و فقط در حافظه غیر دائم ذخیره شود. |  | ✓ |
| **2.14** | MSTG-STORAGE-14 | اگر هنوز لازم است که داده حساس به طور محلی ذخیره شود، باید توسط یک کلید مشتق شده از حافظه ذخیره سازی پشتیبانی شده به صورت سخت‌افزاری رمزنگاری شده که نیازمند تصدیق هویت است. |  | ✓ |
| **2.15** | MSTG-STORAGE-15 | حافظه ذخیره‌سازی محلی اپلیکیشن باید بعد از تعداد زیادی تلاش ناموفق برای تصدیق هویت پاکسازی شود. |  | ✓ |

## منابع

راهنمای وارسی امنیتی موبایل OWASP، دستورالعمل‌هایی مفصل برای تایید نیازمندی‌های لیست شده در این بخش، فراهم می کند.

- Android: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md>
- iOS: Testing Data Storage - <https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md>


برای اطلاعات بیشتر همچنین مشاهده کنید:

- OWASP Mobile Top 10: M1 (Improper Platform Usage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m1-improper-platform-usage>
- OWASP Mobile Top 10: M2 (Insecure Data Storage) - <https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage>
- CWE 117 (Improper Output Neutralization for Logs) - <https://cwe.mitre.org/data/definitions/117.html>
- CWE 200 (Information Exposure) - <https://cwe.mitre.org/data/definitions/200.html>
- CWE 276 (Incorrect Default Permissions) - <https://cwe.mitre.org/data/definitions/276.html>
- CWE 311 (Missing Encryption of Sensitive Data) - <https://cwe.mitre.org/data/definitions/311.html>
- CWE 312 (Cleartext Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/312.html>
- CWE 316 (Cleartext Storage of Sensitive Information in Memory) - <https://cwe.mitre.org/data/definitions/316.html>
- CWE 359 (Exposure of Private Information ('Privacy Violation')) - <https://cwe.mitre.org/data/definitions/359.html>
- CWE 522 (Insufficiently Protected Credentials) - <https://cwe.mitre.org/data/definitions/522.html>
- CWE 524 (Information Exposure Through Caching) - <https://cwe.mitre.org/data/definitions/524.html>
- CWE 530 (Exposure of Backup File to an Unauthorized Control Sphere) - <https://cwe.mitre.org/data/definitions/530.html>
- CWE 532 (Information Exposure Through Log Files) - <https://cwe.mitre.org/data/definitions/532.html>
- CWE 534 (Information Exposure Through Debug Log Files) - <https://cwe.mitre.org/data/definitions/534.html>
- CWE 634 (Weaknesses that Affect System Processes) - <https://cwe.mitre.org/data/definitions/634.html>
- CWE 798 (Use of Hard-coded Credentials) - <https://cwe.mitre.org/data/definitions/798.html>
- CWE 921 (Storage of Sensitive Data in a Mechanism without Access Control) - <https://cwe.mitre.org/data/definitions/921.html>
- CWE 922 (Insecure Storage of Sensitive Information) - <https://cwe.mitre.org/data/definitions/922.html>

</div>
