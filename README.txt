# أدوات تحليل وفحص أمان المواقع

تم تطوير هذه الأدوات بواسطة: Saudi Crackers
البريد الإلكتروني: SaudiLinux7@gmail.com

## المحتويات
1. نبذة عن الأدوات
2. متطلبات النظام
3. طريقة التثبيت
4. طريقة استخدام أداة تحليل المواقع (Site Analyzer)
5. طريقة استخدام أداة استغلال الثغرات (Vulnerability Exploiter)
6. سير العمل النموذجي
7. ملاحظات أمنية

## 1. نبذة عن الأدوات

### أداة تحليل المواقع (Site Analyzer)
أداة قوية مكتوبة بلغة Python تقوم بسحب بيانات المواقع المستهدفة وتحليلها بشكل شامل. تقوم الأداة باستخراج البيانات الوصفية، وملفات الموقع، وروابطه، واستكشاف الثغرات الأمنية المحتملة.

### أداة استغلال الثغرات (Vulnerability Exploiter)
أداة متقدمة مكتوبة بلغة Python تعمل على اختبار واستغلال الثغرات الأمنية المكتشفة في المواقع المستهدفة. تم تصميم هذه الأداة لتكون مكملة لأداة تحليل المواقع وتوفر طرق عملية لاختبار الثغرات وتوليد أدلة إثبات المفهوم (PoC).

## 2. متطلبات النظام

- Python 3.6 أو أحدث
- المكتبات التالية:
  - requests>=2.28.1
  - beautifulsoup4>=4.11.1
  - python-whois>=0.7.3
  - dnspython>=2.2.1
  - colorama>=0.4.5
  - argparse>=1.4.0
  - urllib3>=1.26.12
  - fake-useragent>=0.1.11
  - tqdm>=4.64.1
  - pyopenssl>=22.1.0
  - cryptography>=38.0.1
  - scapy>=2.4.5
  - sockspy>=1.7.1

## 3. طريقة التثبيت

1. قم بتنزيل المشروع أو استنساخه:

```
git clone https://github.com/SaudiCrackers/site-analyzer.git
cd site-analyzer
```

2. قم بتثبيت المتطلبات:

```
pip install -r requirements.txt
```

3. طريقة بديلة للتثبيت باستخدام setup.py:

```
python setup.py install
```

## 4. طريقة استخدام أداة تحليل المواقع (Site Analyzer)

### الأوامر الأساسية

```
python site_analyzer.py -t example.com
```

### خيارات متقدمة

```
python site_analyzer.py -t example.com -o custom_reports -d 2 -v --threads 10
```

### الخيارات المتاحة

- `-t, --target`: عنوان URL المستهدف أو اسم النطاق (مطلوب)
- `-o, --output`: مجلد الإخراج للتقارير (الافتراضي: reports)
- `-d, --depth`: عمق الزحف (الافتراضي: 1)
- `-v, --verbose`: تمكين الإخراج المفصل
- `--no-color`: تعطيل الإخراج الملون
- `--timeout`: مهلة الطلب بالثواني (الافتراضي: 10)
- `--threads`: عدد مسارات التنفيذ للعمليات المتزامنة (الافتراضي: 5)

### أمثلة

#### فحص موقع بسيط
```
python site_analyzer.py -t example.com
```

#### فحص موقع مع زحف عميق
```
python site_analyzer.py -t example.com -d 3 --threads 10
```

#### حفظ التقرير في مجلد مخصص
```
python site_analyzer.py -t example.com -o my_reports
```

## 5. طريقة استخدام أداة استغلال الثغرات (Vulnerability Exploiter)

### الأوامر الأساسية

```
python vulnerability_exploiter.py -t example.com --all
```

### استخدام نتائج تحليل الموقع

```
python vulnerability_exploiter.py -t example.com -i reports/example.com_20230101_120000.json --all
```

### الخيارات المتاحة

- `-t, --target`: عنوان URL المستهدف أو اسم النطاق (مطلوب)
- `-i, --input`: ملف الإدخال مع الثغرات (من site_analyzer)
- `-o, --output`: ملف الإخراج لنتائج الاستغلال
- `--xss`: اختبار ثغرات XSS
- `--sqli`: اختبار ثغرات SQL Injection
- `--csrf`: اختبار ثغرات CSRF
- `--lfi`: اختبار ثغرات LFI/RFI
- `--cmdi`: اختبار ثغرات Command Injection
- `--all`: اختبار جميع الثغرات
- `--cookies`: ملفات تعريف الارتباط المراد استخدامها (الصيغة: name1=value1; name2=value2)
- `--proxy`: البروكسي المراد استخدامه (الصيغة: http://127.0.0.1:8080)
- `--timeout`: مهلة الطلب بالثواني (الافتراضي: 10)
- `--no-color`: تعطيل الإخراج الملون
- `--verbose`: تمكين الإخراج المفصل

### أمثلة

#### اختبار جميع الثغرات
```
python vulnerability_exploiter.py -t example.com --all
```

#### اختبار ثغرات XSS فقط
```
python vulnerability_exploiter.py -t example.com --xss
```

#### استخدام بروكسي واختبار ثغرات SQL Injection
```
python vulnerability_exploiter.py -t example.com --sqli --proxy http://127.0.0.1:8080
```

## 6. سير العمل النموذجي

1. قم أولاً بتحليل الموقع المستهدف باستخدام أداة تحليل المواقع:

```
python site_analyzer.py -t example.com -o reports
```

2. استخدم نتائج التحليل كمدخل لأداة استغلال الثغرات:

```
python vulnerability_exploiter.py -t example.com -i reports/example.com_20230101_120000.json --all
```

3. راجع تقارير النتائج للحصول على معلومات مفصلة حول الثغرات المكتشفة وطرق استغلالها.

## 7. ملاحظات أمنية

- استخدم هذه الأدوات فقط على المواقع التي لديك إذن قانوني لفحصها
- قد يؤدي استخدام هذه الأدوات على مواقع بدون إذن إلى انتهاك القوانين المحلية
- المطور غير مسؤول عن أي استخدام غير قانوني لهذه الأدوات
- بعض طرق الاستغلال قد تسبب ضررًا للأنظمة المستهدفة، استخدمها بحذر

## الترخيص

هذا المشروع مرخص بموجب ترخيص MIT. راجع ملف LICENSE للحصول على التفاصيل.