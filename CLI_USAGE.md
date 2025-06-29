# دليل استخدام واجهة سطر الأوامر لأداة Site Analyzer

## نظرة عامة

توفر أداة Site Analyzer واجهة سطر أوامر قوية تتيح لك تحليل المواقع واستخراج البيانات الوصفية والروابط واكتشاف الثغرات الأمنية المحتملة. يشرح هذا الدليل كيفية استخدام جميع الخيارات المتاحة في واجهة سطر الأوامر.

## الاستخدام الأساسي

الصيغة الأساسية لاستخدام الأداة هي:

```bash
python site_analyzer.py -t TARGET [OPTIONS]
```

حيث `TARGET` هو عنوان URL المستهدف أو اسم النطاق الذي تريد فحصه.

## الخيارات المتاحة

### الخيارات الأساسية

| الخيار | الوصف | القيمة الافتراضية |
|--------|--------|----------------|
| `-t, --target` | عنوان URL المستهدف أو اسم النطاق (مطلوب) | - |
| `-o, --output` | مجلد الإخراج للتقارير | reports |
| `-d, --depth` | عمق الزحف | 1 |
| `-v, --verbose` | تمكين الإخراج المفصل | غير مفعل |
| `--no-color` | تعطيل الإخراج الملون | غير مفعل |
| `-h, --help` | عرض رسالة المساعدة وإنهاء البرنامج | - |

### خيارات متقدمة

| الخيار | الوصف | القيمة الافتراضية |
|--------|--------|----------------|
| `--timeout` | مهلة الطلب بالثواني | 10 |
| `--threads` | عدد مسارات التنفيذ للعمليات المتزامنة | 5 |
| `--user-agent` | تحديد User-Agent مخصص | عشوائي |
| `--cookies` | ملف الكوكيز للمصادقة (بتنسيق Netscape) | - |
| `--proxy` | استخدام وكيل HTTP/SOCKS (بتنسيق http://host:port أو socks5://host:port) | - |
| `--exclude` | أنماط URL للاستبعاد (يمكن تكرار هذا الخيار) | - |
| `--include` | أنماط URL للتضمين فقط (يمكن تكرار هذا الخيار) | - |
| `--max-size` | الحد الأقصى لحجم الاستجابة بالميجابايت | 10 |
| `--delay` | التأخير بين الطلبات بالثواني | 0 |

### خيارات الفحص

| الخيار | الوصف | القيمة الافتراضية |
|--------|--------|----------------|
| `--disable-ssl` | تعطيل فحص SSL/TLS | غير مفعل |
| `--disable-headers` | تعطيل فحص رؤوس الأمان | غير مفعل |
| `--disable-dns` | تعطيل فحص DNS | غير مفعل |
| `--disable-whois` | تعطيل فحص WHOIS | غير مفعل |
| `--disable-files` | تعطيل فحص الملفات الحساسة | غير مفعل |
| `--disable-links` | تعطيل استخراج الروابط | غير مفعل |
| `--disable-metadata` | تعطيل استخراج البيانات الوصفية | غير مفعل |

## أمثلة على الاستخدام

### فحص أساسي لموقع

```bash
python site_analyzer.py -t example.com
```

### فحص موقع مع عمق زحف أكبر

```bash
python site_analyzer.py -t example.com -d 3
```

### فحص موقع مع إخراج مفصل وحفظ التقرير في مجلد مخصص

```bash
python site_analyzer.py -t example.com -v -o my_reports
```

### فحص موقع باستخدام وكيل

```bash
python site_analyzer.py -t example.com --proxy http://127.0.0.1:8080
```

### فحص موقع مع تعطيل بعض الفحوصات

```bash
python site_analyzer.py -t example.com --disable-whois --disable-dns
```

### فحص موقع مع تأخير بين الطلبات

```bash
python site_analyzer.py -t example.com --delay 2
```

### فحص موقع مع استبعاد بعض المسارات

```bash
python site_analyzer.py -t example.com --exclude "/admin/" --exclude "/login/"
```

### فحص موقع مع زيادة عدد مسارات التنفيذ المتزامنة

```bash
python site_analyzer.py -t example.com --threads 10
```

## تنسيق الإخراج

عند تشغيل الأداة، سترى إخراجاً مشابهاً لما يلي:

```
[+] Starting Site Analyzer v1.0.0 by Saudi Crackers
[+] Target: example.com
[+] Scan started at: 2023-07-01 12:00:00

[*] Normalizing URL: example.com -> https://example.com/
[*] Checking connection to target...
[+] Connection successful!

[*] Extracting metadata...
[+] Title: Example Domain
[+] Description: This domain is for use in illustrative examples in documents.
[+] Keywords: example, domain

[*] Checking DNS information...
[+] IP Address: 93.184.216.34
[+] DNS Records: A, AAAA, MX, NS, SOA, TXT

[*] Checking WHOIS information...
[+] Registrar: ICANN
[+] Creation Date: 1995-08-14
[+] Expiration Date: 2023-08-13

[*] Checking security headers...
[-] Missing security header: X-Frame-Options
[-] Missing security header: Content-Security-Policy

[*] Checking for common vulnerabilities...
[-] [Medium] Server information disclosure in headers

[*] Crawling links (depth: 1)...
[+] Found 5 unique links

[+] Scan completed in 3.5 seconds
[+] Report saved to: reports/example.com_20230701_120000.json
```

## تنسيق التقرير

يتم حفظ التقرير بتنسيق JSON ويحتوي على الأقسام التالية:

- `scan_info`: معلومات عامة عن الفحص (التاريخ، الوقت، الإصدار، إلخ)
- `target`: معلومات عن الهدف (URL، IP، إلخ)
- `metadata`: البيانات الوصفية المستخرجة من الموقع
- `dns_info`: معلومات DNS
- `whois_info`: معلومات WHOIS
- `security_headers`: تحليل رؤوس الأمان
- `vulnerabilities`: الثغرات والأخطاء في الإعدادات المكتشفة
- `links`: الروابط المكتشفة في الموقع
- `files`: الملفات الحساسة المكتشفة
- `statistics`: إحصائيات عن الفحص (الوقت المستغرق، عدد الطلبات، إلخ)

## ملاحظات هامة

- استخدم الأداة فقط على المواقع التي لديك إذن قانوني لفحصها.
- قد تؤدي عمليات الفحص المكثفة إلى حظر عنوان IP الخاص بك من قبل الموقع المستهدف.
- استخدم خيار `--delay` لإضافة تأخير بين الطلبات لتقليل الحمل على الخادم المستهدف.
- استخدم خيار `--threads` بحذر، حيث قد يؤدي استخدام عدد كبير من مسارات التنفيذ المتزامنة إلى زيادة الحمل على الخادم المستهدف.
- تحقق دائماً من النتائج يدوياً قبل اتخاذ أي إجراء، حيث قد تعطي الأداة بعض النتائج الإيجابية الكاذبة.

## استكشاف الأخطاء وإصلاحها

### الأداة تعطي خطأ "Connection Error"

تأكد من أن الموقع المستهدف متاح وأن لديك اتصالاً بالإنترنت. قد تحتاج أيضاً إلى زيادة قيمة `--timeout`.

### الأداة تعطي خطأ "SSL Certificate Verification Failed"

قد تواجه هذا الخطأ مع المواقع التي تستخدم شهادات SSL غير صالحة أو موقعة ذاتياً. الأداة تتجاهل التحقق من شهادات SSL بشكل افتراضي.

### الأداة تستغرق وقتاً طويلاً للغاية

حاول تقليل عمق الزحف باستخدام الخيار `-d` أو زيادة عدد مسارات التنفيذ المتزامنة باستخدام الخيار `--threads`.

### الأداة تستهلك الكثير من الذاكرة

قد تستهلك الأداة كمية كبيرة من الذاكرة عند فحص مواقع كبيرة مع عمق زحف عالٍ. حاول تقليل عمق الزحف أو استخدام خيار `--max-size` لتحديد الحد الأقصى لحجم الاستجابة.