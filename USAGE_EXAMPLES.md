# أمثلة استخدام أدوات تحليل وفحص أمان المواقع

**المطور:** Saudi Crackers  
**البريد الإلكتروني:** SaudiLinux7@gmail.com

هذا الملف يقدم أمثلة عملية لاستخدام أدوات تحليل المواقع واستغلال الثغرات في سيناريوهات مختلفة. الهدف هو مساعدة المستخدمين على فهم كيفية استخدام الأدوات بشكل فعال في مهام الاختبار الأمني المختلفة.

## تذكير بإخلاء المسؤولية

**تنبيه هام**: استخدم هذه الأدوات فقط على المواقع التي لديك إذن قانوني لفحصها. الاستخدام غير المصرح به قد يعتبر انتهاكًا للقوانين المحلية والدولية.

## سيناريو 1: تحليل أساسي لموقع

### الهدف
إجراء تحليل أساسي لموقع للحصول على معلومات عامة عن بنيته وتكوينه.

### الخطوات

1. تشغيل أداة تحليل المواقع مع الخيارات الأساسية:

```bash
python site_analyzer.py -t example.com -o reports
```

2. مراجعة التقرير الناتج للحصول على معلومات حول:
   - البيانات الوصفية للموقع
   - التقنيات المستخدمة
   - الروابط الداخلية والخارجية
   - معلومات WHOIS وDNS

### النتائج المتوقعة
تقرير شامل يحتوي على معلومات أساسية عن الموقع، مما يوفر نظرة عامة على بنيته وتكوينه.

## سيناريو 2: تحليل عميق مع زحف الروابط

### الهدف
إجراء تحليل عميق للموقع مع زحف الروابط الداخلية لاكتشاف المزيد من الصفحات والمحتوى.

### الخطوات

1. تشغيل أداة تحليل المواقع مع تحديد عمق الزحف:

```bash
python site_analyzer.py -t example.com -o reports -d 3 --threads 10 -v
```

2. مراجعة التقرير الناتج للحصول على معلومات مفصلة عن:
   - جميع الصفحات التي تم اكتشافها
   - الروابط الداخلية والخارجية لكل صفحة
   - الملفات والموارد المكتشفة
   - الثغرات المحتملة في جميع الصفحات

### النتائج المتوقعة
تقرير شامل يحتوي على معلومات مفصلة عن بنية الموقع وصفحاته وملفاته وروابطه، بالإضافة إلى الثغرات المحتملة.

## سيناريو 3: فحص الثغرات الأمنية

### الهدف
فحص الموقع للكشف عن الثغرات الأمنية الشائعة.

### الخطوات

1. تشغيل أداة تحليل المواقع مع التركيز على فحص الثغرات:

```bash
python site_analyzer.py -t example.com -o reports -d 1 -v
```

2. مراجعة التقرير الناتج للتركيز على قسم الثغرات والتكوينات الخاطئة.

3. استخدام أداة استغلال الثغرات للتحقق من الثغرات المكتشفة:

```bash
python vulnerability_exploiter.py -t example.com -i reports/example.com_20230101_120000.json --all
```

### النتائج المتوقعة
تقارير مفصلة عن الثغرات المكتشفة في الموقع، مع معلومات عن كيفية استغلالها وتوصيات للإصلاح.

## سيناريو 4: فحص ثغرات XSS

### الهدف
فحص الموقع للكشف عن ثغرات XSS (Cross-Site Scripting) واختبار استغلالها.

### الخطوات

1. تشغيل أداة تحليل المواقع للكشف عن نماذج الإدخال والصفحات التفاعلية:

```bash
python site_analyzer.py -t example.com -o reports -d 2 -v
```

2. استخدام أداة استغلال الثغرات للتركيز على ثغرات XSS:

```bash
python vulnerability_exploiter.py -t example.com --xss -v
```

3. مراجعة التقرير الناتج للحصول على معلومات مفصلة عن ثغرات XSS المكتشفة وكيفية استغلالها.

### النتائج المتوقعة
تقرير مفصل عن ثغرات XSS المكتشفة في الموقع، مع أمثلة على الحمولات (payloads) التي يمكن استخدامها لاستغلال هذه الثغرات.

## سيناريو 5: فحص ثغرات SQL Injection

### الهدف
فحص الموقع للكشف عن ثغرات SQL Injection واختبار استغلالها.

### الخطوات

1. تشغيل أداة تحليل المواقع للكشف عن نماذج الإدخال والصفحات التفاعلية:

```bash
python site_analyzer.py -t example.com -o reports -d 2 -v
```

2. استخدام أداة استغلال الثغرات للتركيز على ثغرات SQL Injection:

```bash
python vulnerability_exploiter.py -t example.com --sqli -v
```

3. مراجعة التقرير الناتج للحصول على معلومات مفصلة عن ثغرات SQL Injection المكتشفة وكيفية استغلالها.

### النتائج المتوقعة
تقرير مفصل عن ثغرات SQL Injection المكتشفة في الموقع، مع أمثلة على الحمولات (payloads) التي يمكن استخدامها لاستغلال هذه الثغرات.

## سيناريو 6: فحص ثغرات CSRF

### الهدف
فحص الموقع للكشف عن ثغرات CSRF (Cross-Site Request Forgery) واختبار استغلالها.

### الخطوات

1. تشغيل أداة تحليل المواقع للكشف عن نماذج الإدخال والصفحات التفاعلية:

```bash
python site_analyzer.py -t example.com -o reports -d 2 -v
```

2. استخدام أداة استغلال الثغرات للتركيز على ثغرات CSRF:

```bash
python vulnerability_exploiter.py -t example.com --csrf -v
```

3. مراجعة التقرير الناتج للحصول على معلومات مفصلة عن ثغرات CSRF المكتشفة وكيفية استغلالها.

### النتائج المتوقعة
تقرير مفصل عن ثغرات CSRF المكتشفة في الموقع، مع أمثلة على كيفية إنشاء صفحات HTML لاستغلال هذه الثغرات.

## سيناريو 7: فحص ثغرات File Inclusion

### الهدف
فحص الموقع للكشف عن ثغرات LFI/RFI (Local/Remote File Inclusion) واختبار استغلالها.

### الخطوات

1. تشغيل أداة تحليل المواقع للكشف عن المعلمات المشبوهة في عناوين URL:

```bash
python site_analyzer.py -t example.com -o reports -d 2 -v
```

2. استخدام أداة استغلال الثغرات للتركيز على ثغرات File Inclusion:

```bash
python vulnerability_exploiter.py -t example.com --lfi -v
```

3. مراجعة التقرير الناتج للحصول على معلومات مفصلة عن ثغرات File Inclusion المكتشفة وكيفية استغلالها.

### النتائج المتوقعة
تقرير مفصل عن ثغرات File Inclusion المكتشفة في الموقع، مع أمثلة على المسارات والحمولات التي يمكن استخدامها لاستغلال هذه الثغرات.

## سيناريو 8: فحص ثغرات Command Injection

### الهدف
فحص الموقع للكشف عن ثغرات Command Injection واختبار استغلالها.

### الخطوات

1. تشغيل أداة تحليل المواقع للكشف عن المعلمات المشبوهة في عناوين URL ونماذج الإدخال:

```bash
python site_analyzer.py -t example.com -o reports -d 2 -v
```

2. استخدام أداة استغلال الثغرات للتركيز على ثغرات Command Injection:

```bash
python vulnerability_exploiter.py -t example.com --cmdi -v
```

3. مراجعة التقرير الناتج للحصول على معلومات مفصلة عن ثغرات Command Injection المكتشفة وكيفية استغلالها.

### النتائج المتوقعة
تقرير مفصل عن ثغرات Command Injection المكتشفة في الموقع، مع أمثلة على الحمولات التي يمكن استخدامها لاستغلال هذه الثغرات.

## سيناريو 9: استخدام بروكسي للفحص

### الهدف
استخدام بروكسي لإخفاء هوية المستخدم أثناء فحص الموقع.

### الخطوات

1. إعداد بروكسي (مثل Tor أو بروكسي HTTP).

2. تشغيل أداة تحليل المواقع مع تحديد البروكسي:

```bash
python site_analyzer.py -t example.com -o reports --proxy http://127.0.0.1:8080
```

3. استخدام أداة استغلال الثغرات مع نفس البروكسي:

```bash
python vulnerability_exploiter.py -t example.com --all --proxy http://127.0.0.1:8080
```

### النتائج المتوقعة
تقارير مفصلة عن الموقع والثغرات المكتشفة، مع إخفاء هوية المستخدم أثناء الفحص.

## سيناريو 10: فحص شامل مع تقرير مفصل

### الهدف
إجراء فحص شامل للموقع واستخراج تقرير مفصل عن جميع الجوانب.

### الخطوات

1. تشغيل أداة تحليل المواقع مع خيارات شاملة:

```bash
python site_analyzer.py -t example.com -o reports -d 3 --threads 10 -v
```

2. استخدام أداة استغلال الثغرات لفحص جميع أنواع الثغرات:

```bash
python vulnerability_exploiter.py -t example.com -i reports/example.com_20230101_120000.json --all -v
```

3. دمج نتائج التقارير وإعداد تقرير شامل يتضمن:
   - معلومات عامة عن الموقع
   - البنية والتكوين
   - الثغرات المكتشفة
   - طرق الاستغلال
   - التوصيات للإصلاح

### النتائج المتوقعة
تقرير شامل ومفصل عن جميع جوانب الموقع، بما في ذلك البنية والتكوين والثغرات وطرق الاستغلال والتوصيات للإصلاح.

---

## نصائح عامة

1. **ابدأ دائمًا بالفحص الأساسي**: قبل إجراء فحص مفصل، ابدأ بفحص أساسي للحصول على نظرة عامة عن الموقع.

2. **استخدم الخيار `-v` للحصول على معلومات مفصلة**: يوفر وضع الإخراج المفصل معلومات إضافية مفيدة أثناء الفحص.

3. **ضبط عدد مسارات التنفيذ**: استخدم الخيار `--threads` لضبط عدد مسارات التنفيذ وفقًا لقدرة جهازك وسرعة اتصالك بالإنترنت.

4. **استخدام ملفات تعريف الارتباط للمواقع التي تتطلب تسجيل الدخول**: استخدم الخيار `--cookies` لتوفير ملفات تعريف الارتباط للوصول إلى المحتوى المحمي.

5. **تعديل مهلة الطلب**: استخدم الخيار `--timeout` لزيادة مهلة الطلب إذا كان الموقع بطيئًا.

6. **استخدام البروكسي**: استخدم الخيار `--proxy` لإخفاء هويتك أثناء الفحص.

---

© 2023 Saudi Crackers. جميع الحقوق محفوظة.