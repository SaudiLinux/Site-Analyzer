# التوثيق الفني لأداة Site Analyzer

هذا المستند يوفر توثيقاً فنياً مفصلاً لأداة Site Analyzer، ويشرح بنية الكود والوظائف الرئيسية والتصميم الفني للأداة.

## نظرة عامة على البنية

تتكون أداة Site Analyzer من عدة وحدات وظيفية رئيسية:

1. **وحدة الطلبات والاتصال**: مسؤولة عن إجراء طلبات HTTP وإدارة الاتصال بالمواقع المستهدفة
2. **وحدة استخراج البيانات**: مسؤولة عن استخراج البيانات الوصفية والروابط من المواقع
3. **وحدة فحص DNS وWHOIS**: مسؤولة عن جمع معلومات DNS وWHOIS للنطاقات
4. **وحدة فحص الأمان**: مسؤولة عن فحص رؤوس الأمان والثغرات والأخطاء في الإعدادات
5. **وحدة التقارير**: مسؤولة عن إنشاء وحفظ التقارير
6. **وحدة واجهة سطر الأوامر**: مسؤولة عن معالجة المدخلات وعرض المخرجات

## تفاصيل الوحدات الوظيفية

### وحدة الطلبات والاتصال

#### الدوال الرئيسية:

- `get_random_user_agent()`: توليد عنوان User-Agent عشوائي لتجنب الحظر
- `make_request(url, timeout, max_retries)`: إجراء طلب HTTP مع آلية إعادة المحاولة
- `normalize_url(url)`: تطبيع عنوان URL
- `get_base_domain(url)`: استخراج النطاق الأساسي من URL

#### آلية إعادة المحاولة:

تستخدم الأداة آلية إعادة المحاولة للتعامل مع فشل الطلبات المؤقت. يتم تحديد عدد المحاولات وفترة الانتظار بين المحاولات.

```python
def make_request(url, timeout=10, max_retries=3):
    # ... implementation details ...
```

### وحدة استخراج البيانات

#### الدوال الرئيسية:

- `extract_metadata(url)`: استخراج البيانات الوصفية من الموقع
- `extract_links(url, base_domain)`: استخراج الروابط من الموقع

#### استخراج البيانات الوصفية:

تستخدم الأداة مكتبة BeautifulSoup لتحليل HTML واستخراج البيانات الوصفية مثل العنوان والوصف والكلمات المفتاحية والتقنيات المستخدمة.

```python
def extract_metadata(url):
    # ... implementation details ...
```

#### اكتشاف التقنيات:

تستخدم الأداة أنماط محددة للكشف عن التقنيات المستخدمة في الموقع، مثل أطر العمل ونظم إدارة المحتوى.

```python
tech_patterns = {
    'WordPress': ['wp-content', 'wp-includes', 'wordpress'],
    'Joomla': ['joomla', 'com_content', 'com_users'],
    # ... more patterns ...
}
```

### وحدة فحص DNS وWHOIS

#### الدوال الرئيسية:

- `dns_enumeration(domain)`: إجراء فحص DNS للنطاق
- `get_whois_info(domain)`: الحصول على معلومات WHOIS للنطاق

#### فحص DNS:

تستخدم الأداة مكتبة dnspython للحصول على سجلات DNS المختلفة (A, AAAA, MX, NS, TXT, CNAME, SOA).

```python
def dns_enumeration(domain):
    # ... implementation details ...
```

### وحدة فحص الأمان

#### الدوال الرئيسية:

- `check_security_headers(url)`: فحص رؤوس الأمان
- `check_vulnerabilities(url, metadata, security_headers)`: فحص الثغرات الشائعة
- `check_misconfigurations(url)`: فحص الأخطاء في الإعدادات

#### فحص رؤوس الأمان:

تتحقق الأداة من وجود رؤوس الأمان الشائعة مثل:

- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- X-XSS-Protection
- Referrer-Policy
- Feature-Policy
- Permissions-Policy

```python
def check_security_headers(url):
    # ... implementation details ...
```

#### فحص الثغرات:

تفحص الأداة الثغرات الشائعة مثل:

- مشاكل SSL/TLS
- رؤوس الأمان المفقودة
- الإفصاح عن المعلومات في رؤوس HTTP
- قائمة الدليل المفعلة
- معلومات حساسة في ملف robots.txt

```python
def check_vulnerabilities(url, metadata, security_headers):
    # ... implementation details ...
```

#### فحص الأخطاء في الإعدادات:

تفحص الأداة الأخطاء الشائعة في الإعدادات مثل:

- تعرض مستودع Git
- تعرض ملف البيئة (.env)
- تعرض ملفات التكوين
- تعرض معلومات PHP
- تعرض ملفات النسخ الاحتياطي
- صفحات تسجيل الدخول الافتراضية

```python
def check_misconfigurations(url):
    # ... implementation details ...
```

### وحدة التقارير

#### الدوال الرئيسية:

- `save_results(target, results, output_dir)`: حفظ نتائج الفحص في ملف
- `print_summary(results)`: طباعة ملخص النتائج

#### تنسيق التقرير:

يتم حفظ التقارير بتنسيق JSON مع الهيكل التالي:

```json
{
    "target": "http://example.com",
    "base_domain": "example.com",
    "scan_date": "2023-01-01 12:00:00",
    "metadata": { ... },
    "whois": { ... },
    "dns": { ... },
    "security_headers": { ... },
    "links": { ... },
    "vulnerabilities": [ ... ],
    "misconfigurations": [ ... ]
}
```

### وحدة واجهة سطر الأوامر

#### الدالة الرئيسية:

- `main()`: نقطة الدخول الرئيسية للأداة

#### معالجة المدخلات:

تستخدم الأداة مكتبة argparse لمعالجة مدخلات سطر الأوامر.

```python
def main():
    parser = argparse.ArgumentParser(description='Site Analyzer Tool')
    parser.add_argument('-t', '--target', required=True, help='Target URL or domain')
    # ... more arguments ...
    
    args = parser.parse_args()
    # ... implementation details ...
```

## تفاصيل التنفيذ

### التزامن والأداء

تستخدم الأداة مكتبة `concurrent.futures` لتنفيذ العمليات بشكل متزامن، مما يحسن الأداء عند زحف المواقع الكبيرة.

```python
with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
    future_to_url = {executor.submit(extract_links, url, base_domain): url for url in urls_to_crawl if url not in crawled_urls}
    # ... implementation details ...
```

### التعامل مع الأخطاء

تستخدم الأداة بنية try/except للتعامل مع الأخطاء المحتملة أثناء التنفيذ.

```python
try:
    # ... implementation details ...
except KeyboardInterrupt:
    # Handle user interruption
except Exception as e:
    # Handle general exceptions
```

### تقدم العملية

تستخدم الأداة مكتبة `tqdm` لعرض شريط تقدم أثناء زحف المواقع.

```python
with tqdm(total=len(urls_to_crawl), desc="Crawling", unit="url") as pbar:
    # ... implementation details ...
    pbar.update(1)
```

## تصميم الأمان

### تدوير User-Agent

تستخدم الأداة آلية تدوير User-Agent لتجنب الحظر من قبل المواقع.

```python
def get_random_user_agent():
    # ... implementation details ...
```

### التعامل مع SSL

تتحقق الأداة من تكوين SSL/TLS للمواقع وتكتشف المشاكل المحتملة.

```python
context = ssl.create_default_context()
with socket.create_connection((domain, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=domain) as ssock:
        cert = ssock.getpeercert()
        # ... implementation details ...
```

## الاعتبارات المستقبلية

### التحسينات المقترحة

1. **دعم المصادقة**: إضافة دعم للمواقع التي تتطلب المصادقة
2. **فحص API**: إضافة دعم لفحص واجهات API
3. **تحليل JavaScript**: تحسين القدرة على تحليل تطبيقات JavaScript الديناميكية
4. **قاعدة بيانات الثغرات**: ربط الأداة بقواعد بيانات الثغرات المعروفة مثل CVE
5. **واجهة مستخدم رسومية**: إضافة واجهة مستخدم رسومية لتسهيل الاستخدام
6. **تقارير PDF**: إضافة دعم لتصدير التقارير بتنسيق PDF
7. **مقارنة الفحوصات**: إضافة القدرة على مقارنة نتائج الفحوصات المتعددة

### تحديات معروفة

1. **تطبيقات SPA**: قد تواجه الأداة صعوبة في تحليل تطبيقات الصفحة الواحدة (SPA)
2. **محتوى ديناميكي**: قد لا تتمكن الأداة من الوصول إلى المحتوى الذي يتم إنشاؤه ديناميكياً بواسطة JavaScript
3. **حماية من الزحف**: قد تحظر بعض المواقع الزحف باستخدام تقنيات مثل CAPTCHA
4. **تقييد معدل الطلبات**: قد تقيد بعض المواقع معدل الطلبات

## الخلاصة

توفر أداة Site Analyzer إطاراً قوياً لتحليل المواقع واكتشاف الثغرات الأمنية. تم تصميم الأداة بطريقة قابلة للتوسيع، مما يسمح بإضافة وحدات جديدة بسهولة. يمكن استخدام هذا التوثيق الفني كمرجع للمطورين الذين يرغبون في فهم الأداة أو المساهمة في تطويرها.