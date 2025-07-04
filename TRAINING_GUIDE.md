# دليل تدريبي لأدوات تحليل وفحص أمان المواقع

**المطور:** Saudi Crackers  
**البريد الإلكتروني:** SaudiLinux7@gmail.com

هذا الدليل التدريبي مصمم لمساعدة المستخدمين الجدد على تعلم كيفية استخدام أدوات تحليل المواقع واستغلال الثغرات بشكل فعال وآمن. يتضمن الدليل شرحًا مفصلاً للمفاهيم الأساسية، وخطوات التثبيت، وتدريبات عملية متدرجة في الصعوبة.

## تذكير بإخلاء المسؤولية

**تنبيه هام**: استخدم هذه الأدوات فقط على المواقع التي لديك إذن قانوني لفحصها. الاستخدام غير المصرح به قد يعتبر انتهاكًا للقوانين المحلية والدولية.

## المتطلبات الأساسية

### المعرفة المطلوبة

- معرفة أساسية بلغة Python
- فهم أساسي لبروتوكولات الويب (HTTP/HTTPS)
- معرفة أساسية بأمان الويب والثغرات الشائعة

### المتطلبات التقنية

- Python 3.6 أو أحدث
- المكتبات المطلوبة (يمكن تثبيتها باستخدام `pip install -r requirements.txt`)
- اتصال إنترنت مستقر

## الجزء الأول: التثبيت والإعداد

### تثبيت الأدوات

1. قم بتنزيل الأدوات من المستودع:

```bash
git clone https://github.com/SaudiCrackers/site-analyzer.git
cd site-analyzer
```

2. قم بتثبيت المكتبات المطلوبة:

```bash
pip install -r requirements.txt
```

3. تأكد من صلاحيات التنفيذ للملفات:

```bash
chmod +x site_analyzer.py vulnerability_exploiter.py
```

### التحقق من التثبيت

قم بتشغيل الأمر التالي للتحقق من تثبيت الأدوات بشكل صحيح:

```bash
python site_analyzer.py -h
python vulnerability_exploiter.py -h
```

يجب أن تظهر قائمة بالخيارات المتاحة لكل أداة.

## الجزء الثاني: مفاهيم أساسية

### فهم تحليل المواقع

تحليل المواقع هو عملية جمع معلومات عن موقع ويب لفهم بنيته وتكوينه وتحديد نقاط الضعف المحتملة. تتضمن هذه العملية:

1. **جمع البيانات الوصفية**: استخراج معلومات مثل العنوان والوصف والكلمات المفتاحية والتقنيات المستخدمة.

2. **استخراج الروابط**: تحديد الروابط الداخلية والخارجية والموارد المرتبطة بالموقع.

3. **فحص التكوين**: التحقق من إعدادات الأمان وترويسات HTTP والشهادات الرقمية.

4. **اكتشاف الثغرات**: تحديد نقاط الضعف المحتملة مثل XSS وSQL Injection وغيرها.

### فهم استغلال الثغرات

aستغلال الثغرات هو عملية استخدام نقاط الضعف المكتشفة لاختبار مدى تأثيرها على أمان الموقع. تتضمن هذه العملية:

1. **التحقق من الثغرات**: التأكد من وجود الثغرة وقابليتها للاستغلال.

2. **تطوير طرق الاستغلال**: إنشاء حمولات (payloads) مخصصة لاستغلال الثغرات المكتشفة.

3. **تقييم التأثير**: تحديد مدى تأثير الثغرة على أمان الموقع والبيانات.

4. **توثيق النتائج**: توثيق الثغرات المكتشفة وطرق استغلالها والتوصيات للإصلاح.

## الجزء الثالث: تدريبات عملية

### تدريب 1: تحليل أساسي لموقع

#### الهدف
إجراء تحليل أساسي لموقع للحصول على معلومات عامة عن بنيته وتكوينه.

#### الخطوات

1. قم بتشغيل أداة تحليل المواقع مع الخيارات الأساسية:

```bash
python site_analyzer.py -t example.com -o reports
```

2. افتح التقرير الناتج وقم بتحليل المعلومات التالية:
   - البيانات الوصفية للموقع
   - التقنيات المستخدمة
   - الروابط الداخلية والخارجية
   - معلومات WHOIS وDNS

#### أسئلة للتفكير
- ما هي التقنيات الرئيسية المستخدمة في الموقع؟
- ما هي أنواع الروابط الأكثر شيوعًا في الموقع؟
- هل هناك أي معلومات حساسة في البيانات الوصفية؟

### تدريب 2: تحليل عميق مع زحف الروابط

#### الهدف
إجراء تحليل عميق للموقع مع زحف الروابط الداخلية لاكتشاف المزيد من الصفحات والمحتوى.

#### الخطوات

1. قم بتشغيل أداة تحليل المواقع مع تحديد عمق الزحف:

```bash
python site_analyzer.py -t example.com -o reports -d 2 --threads 5 -v
```

2. افتح التقرير الناتج وقم بتحليل المعلومات التالية:
   - عدد الصفحات التي تم اكتشافها
   - بنية الموقع وتنظيم الصفحات
   - الملفات والموارد المكتشفة
   - الثغرات المحتملة في جميع الصفحات

#### أسئلة للتفكير
- كيف يؤثر عمق الزحف على كمية المعلومات المكتشفة؟
- ما هي أنماط تنظيم الصفحات في الموقع؟
- هل هناك أي صفحات أو ملفات حساسة تم اكتشافها؟

### تدريب 3: فحص الثغرات الأمنية

#### الهدف
فحص الموقع للكشف عن الثغرات الأمنية الشائعة.

#### الخطوات

1. قم بتشغيل أداة تحليل المواقع مع التركيز على فحص الثغرات:

```bash
python site_analyzer.py -t example.com -o reports -d 1 -v
```

2. افتح التقرير الناتج وركز على قسم الثغرات والتكوينات الخاطئة.

3. قم بتشغيل أداة استغلال الثغرات للتحقق من الثغرات المكتشفة:

```bash
python vulnerability_exploiter.py -t example.com -i reports/example.com_*.json --all
```

4. قم بتحليل التقرير الناتج وحدد الثغرات الأكثر خطورة.

#### أسئلة للتفكير
- ما هي أنواع الثغرات الأكثر شيوعًا في الموقع؟
- ما هي درجة خطورة كل ثغرة؟
- ما هي التوصيات المقترحة لإصلاح هذه الثغرات؟

### تدريب 4: فحص ثغرات XSS

#### الهدف
فحص الموقع للكشف عن ثغرات XSS (Cross-Site Scripting) واختبار استغلالها.

#### الخطوات

1. قم بتشغيل أداة تحليل المواقع للكشف عن نماذج الإدخال والصفحات التفاعلية:

```bash
python site_analyzer.py -t example.com -o reports -d 2 -v
```

2. قم بتشغيل أداة استغلال الثغرات للتركيز على ثغرات XSS:

```bash
python vulnerability_exploiter.py -t example.com --xss -v
```

3. قم بتحليل التقرير الناتج وحدد نقاط الإدخال المعرضة لثغرات XSS.

4. قم بتجربة الحمولات المقترحة على نقاط الإدخال المعرضة للثغرات.

#### أسئلة للتفكير
- ما هي أنواع ثغرات XSS التي تم اكتشافها (Reflected, Stored, DOM)؟
- ما هي نقاط الإدخال الأكثر عرضة لثغرات XSS؟
- كيف يمكن تعديل الحمولات لتجاوز آليات الحماية؟

### تدريب 5: فحص ثغرات SQL Injection

#### الهدف
فحص الموقع للكشف عن ثغرات SQL Injection واختبار استغلالها.

#### الخطوات

1. قم بتشغيل أداة تحليل المواقع للكشف عن نماذج الإدخال والصفحات التفاعلية:

```bash
python site_analyzer.py -t example.com -o reports -d 2 -v
```

2. قم بتشغيل أداة استغلال الثغرات للتركيز على ثغرات SQL Injection:

```bash
python vulnerability_exploiter.py -t example.com --sqli -v
```

3. قم بتحليل التقرير الناتج وحدد نقاط الإدخال المعرضة لثغرات SQL Injection.

4. قم بتجربة الحمولات المقترحة على نقاط الإدخال المعرضة للثغرات.

#### أسئلة للتفكير
- ما هي أنواع قواعد البيانات المستخدمة في الموقع؟
- ما هي نقاط الإدخال الأكثر عرضة لثغرات SQL Injection؟
- كيف يمكن تعديل الحمولات لاستخراج معلومات من قاعدة البيانات؟

## الجزء الرابع: مشروع نهائي

### مشروع: تقييم أمان موقع كامل

#### الهدف
إجراء تقييم أمان شامل لموقع ويب وإعداد تقرير مفصل عن النتائج والتوصيات.

#### المتطلبات

1. اختر موقعًا ويب لديك إذن قانوني لفحصه.

2. قم بإجراء تحليل شامل للموقع باستخدام أداة تحليل المواقع:

```bash
python site_analyzer.py -t target.com -o reports -d 3 --threads 10 -v
```

3. قم بفحص الثغرات المكتشفة باستخدام أداة استغلال الثغرات:

```bash
python vulnerability_exploiter.py -t target.com -i reports/target.com_*.json --all -v
```

4. قم بإعداد تقرير مفصل يتضمن:
   - ملخص تنفيذي
   - نطاق التقييم ومنهجيته
   - النتائج المكتشفة مصنفة حسب درجة الخطورة
   - تفاصيل كل ثغرة وطريقة استغلالها
   - التوصيات للإصلاح
   - الملاحق (نتائج الفحص الخام، الأدلة، الصور)

#### معايير التقييم
- شمولية التحليل
- دقة اكتشاف الثغرات
- جودة التوصيات للإصلاح
- تنظيم وتنسيق التقرير
- الالتزام بالمعايير الأخلاقية والقانونية

## الجزء الخامس: موارد إضافية

### مراجع للتعلم

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Web Application Hacker's Handbook](https://www.wiley.com/en-us/The+Web+Application+Hacker%27s+Handbook%3A+Finding+and+Exploiting+Security+Flaws%2C+2nd+Edition-p-9781118026472)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)

### أدوات مساعدة

- [Burp Suite](https://portswigger.net/burp)
- [OWASP ZAP](https://www.zaproxy.org/)
- [Metasploit](https://www.metasploit.com/)

### مجتمعات للدعم

- [OWASP Community](https://owasp.org/)
- [HackerOne](https://www.hackerone.com/)
- [Bugcrowd](https://www.bugcrowd.com/)

---

## نصائح للمتدربين

1. **ابدأ بالأساسيات**: تأكد من فهمك للمفاهيم الأساسية قبل الانتقال إلى المواضيع المتقدمة.

2. **التدرب على بيئات آمنة**: استخدم بيئات التدريب المخصصة مثل DVWA أو WebGoat للتدرب على اكتشاف واستغلال الثغرات.

3. **التوثيق المستمر**: وثق جميع خطواتك ونتائجك أثناء التدريب لتحسين فهمك وتطوير مهاراتك.

4. **التعلم المستمر**: تابع أحدث التطورات في مجال أمان الويب والثغرات الجديدة.

5. **الالتزام بالأخلاقيات**: احترم دائمًا القوانين والأخلاقيات المهنية عند استخدام أدوات الاختبار الأمني.

---

© 2023 Saudi Crackers. جميع الحقوق محفوظة.