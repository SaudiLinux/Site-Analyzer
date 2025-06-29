# دليل تطوير أداة Site Analyzer

هذا الدليل مخصص للمطورين الذين يرغبون في المساهمة في تطوير أداة Site Analyzer أو إضافة وحدات ووظائف جديدة إليها. يوفر هذا الدليل نظرة عامة على بنية الكود وكيفية تنظيمه، بالإضافة إلى إرشادات حول كيفية إضافة ميزات جديدة.

## نظرة عامة على بنية المشروع

### هيكل الملفات

```
site_analyzer/
├── site_analyzer.py        # الملف الرئيسي للأداة
├── requirements.txt        # متطلبات المكتبات
├── setup.py               # ملف الإعداد للتثبيت كحزمة
├── tests.py               # اختبارات الوحدة
├── README.md              # توثيق عام للمشروع
├── CONTRIBUTING.md        # إرشادات المساهمة
├── LICENSE                # ترخيص المشروع
├── CHANGELOG.md           # سجل التغييرات
├── ROADMAP.md             # خطة التطوير المستقبلية
└── docs/                  # مستندات إضافية
    ├── API_USAGE.md       # توثيق استخدام API
    ├── CLI_USAGE.md       # توثيق استخدام واجهة سطر الأوامر
    ├── TECHNICAL_DOCS.md  # توثيق تقني
    └── examples.md        # أمثلة على الاستخدام
```

### بنية الكود

تتكون أداة Site Analyzer من عدة وحدات رئيسية:

1. **وحدة الطلبات والاتصال**: مسؤولة عن إجراء طلبات HTTP وإدارة الاتصالات مع المواقع المستهدفة.
2. **وحدة استخراج البيانات**: مسؤولة عن استخراج البيانات الوصفية والروابط والمحتوى من صفحات الويب.
3. **وحدة DNS وWHOIS**: مسؤولة عن جمع معلومات DNS وWHOIS للنطاقات المستهدفة.
4. **وحدة فحص الأمان**: مسؤولة عن فحص رؤوس الأمان واكتشاف الثغرات والأخطاء في الإعدادات.
5. **وحدة التقارير**: مسؤولة عن إنشاء وحفظ تقارير الفحص.
6. **وحدة واجهة سطر الأوامر**: مسؤولة عن معالجة مدخلات المستخدم وعرض النتائج.

## إضافة وحدة جديدة

لإضافة وحدة جديدة إلى أداة Site Analyzer، اتبع الخطوات التالية:

### 1. إنشاء ملف الوحدة

إذا كنت تضيف وحدة كبيرة، فقد ترغب في إنشاء ملف منفصل لها. على سبيل المثال، لإضافة وحدة لفحص ثغرات XSS:

```python
# xss_scanner.py

def scan_xss_vulnerabilities(url, headers=None, cookies=None, timeout=10):
    """
    فحص ثغرات XSS في موقع ويب.
    
    Args:
        url (str): عنوان URL المستهدف
        headers (dict, optional): رؤوس HTTP مخصصة
        cookies (dict, optional): كوكيز للمصادقة
        timeout (int, optional): مهلة الطلب بالثواني
        
    Returns:
        list: قائمة بالثغرات المكتشفة
    """
    vulnerabilities = []
    
    # تنفيذ منطق فحص XSS هنا
    # 1. تحديد نقاط الإدخال (نماذج، معلمات URL، إلخ)
    # 2. اختبار سلاسل XSS المختلفة
    # 3. تحليل الاستجابات للكشف عن الثغرات
    
    return vulnerabilities


def get_input_points(html_content):
    """
    تحديد نقاط الإدخال المحتملة في صفحة HTML.
    
    Args:
        html_content (str): محتوى HTML للصفحة
        
    Returns:
        dict: قاموس بنقاط الإدخال المكتشفة
    """
    input_points = {
        'forms': [],
        'url_params': [],
        'input_fields': []
    }
    
    # تنفيذ منطق تحديد نقاط الإدخال هنا
    
    return input_points


def test_xss_payload(url, input_point, payload, headers=None, cookies=None, timeout=10):
    """
    اختبار سلسلة XSS على نقطة إدخال محددة.
    
    Args:
        url (str): عنوان URL المستهدف
        input_point (dict): معلومات عن نقطة الإدخال
        payload (str): سلسلة XSS للاختبار
        headers (dict, optional): رؤوس HTTP مخصصة
        cookies (dict, optional): كوكيز للمصادقة
        timeout (int, optional): مهلة الطلب بالثواني
        
    Returns:
        bool: True إذا تم اكتشاف ثغرة، False خلاف ذلك
    """
    # تنفيذ منطق اختبار سلسلة XSS هنا
    
    return False
```

### 2. دمج الوحدة في الملف الرئيسي

بعد إنشاء الوحدة، قم بدمجها في الملف الرئيسي `site_analyzer.py`:

```python
# استيراد الوحدة الجديدة
from xss_scanner import scan_xss_vulnerabilities

# إضافة الوحدة إلى فئة SiteAnalyzer
class SiteAnalyzer:
    # ... الكود الحالي ...
    
    def scan_xss(self):
        """
        فحص ثغرات XSS في الموقع المستهدف.
        
        Returns:
            list: قائمة بثغرات XSS المكتشفة
        """
        self._print_status("Scanning for XSS vulnerabilities...")
        vulnerabilities = scan_xss_vulnerabilities(
            self.target_url,
            headers=self.headers,
            cookies=self.cookies,
            timeout=self.timeout
        )
        
        if vulnerabilities:
            self._print_status(f"Found {len(vulnerabilities)} potential XSS vulnerabilities", "warning")
        else:
            self._print_status("No XSS vulnerabilities found")
            
        return vulnerabilities
    
    def scan(self):
        # ... الكود الحالي ...
        
        # إضافة فحص XSS إلى الفحص الشامل
        if not self.disable_xss:
            results["xss_vulnerabilities"] = self.scan_xss()
        
        # ... الكود الحالي ...
        
        return results
```

### 3. إضافة خيارات سطر الأوامر

إضافة خيارات سطر الأوامر للوحدة الجديدة:

```python
def parse_arguments():
    # ... الكود الحالي ...
    
    # إضافة خيارات للوحدة الجديدة
    parser.add_argument("--disable-xss", action="store_true", help="Disable XSS vulnerability scanning")
    parser.add_argument("--xss-payloads", type=str, help="Path to custom XSS payloads file")
    
    # ... الكود الحالي ...
    
    return parser.parse_args()
```

### 4. تحديث التوثيق

تحديث ملفات التوثيق لتشمل الوحدة الجديدة:

- إضافة وصف للوحدة في `README.md`
- إضافة أمثلة على الاستخدام في `examples.md`
- إضافة توثيق تقني في `TECHNICAL_DOCS.md`
- تحديث `CHANGELOG.md` لتوثيق الإضافة الجديدة

### 5. إضافة اختبارات

إضافة اختبارات للوحدة الجديدة في `tests.py`:

```python
def test_xss_scanner():
    # اختبار وحدة فحص XSS
    from xss_scanner import scan_xss_vulnerabilities, get_input_points, test_xss_payload
    
    # اختبار تحديد نقاط الإدخال
    html_content = "<form action=\"test.php\"><input type=\"text\" name=\"search\"></form>"
    input_points = get_input_points(html_content)
    assert len(input_points["forms"]) == 1
    assert len(input_points["input_fields"]) == 1
    
    # اختبار اكتشاف الثغرات (باستخدام موقع اختبار)
    vulnerabilities = scan_xss_vulnerabilities("http://testphp.vulnweb.com/search.php")
    assert len(vulnerabilities) > 0
```

## إضافة فحص أمان جديد

لإضافة فحص أمان جديد إلى وحدة فحص الأمان الحالية، اتبع الخطوات التالية:

### 1. إضافة دالة الفحص

```python
def check_csrf_protection(url, headers=None, cookies=None, timeout=10):
    """
    فحص حماية CSRF في موقع ويب.
    
    Args:
        url (str): عنوان URL المستهدف
        headers (dict, optional): رؤوس HTTP مخصصة
        cookies (dict, optional): كوكيز للمصادقة
        timeout (int, optional): مهلة الطلب بالثواني
        
    Returns:
        dict: نتائج فحص حماية CSRF
    """
    result = {
        "has_csrf_protection": False,
        "csrf_implementation": None,
        "forms_with_csrf": 0,
        "forms_without_csrf": 0,
        "details": []
    }
    
    # تنفيذ منطق فحص حماية CSRF هنا
    # 1. تحليل النماذج في الصفحة
    # 2. البحث عن رموز CSRF
    # 3. فحص رؤوس الأمان المتعلقة بـ CSRF
    
    return result
```

### 2. دمج الفحص في وحدة فحص الأمان

```python
def scan_vulnerabilities(url, options=None):
    # ... الكود الحالي ...
    
    # إضافة فحص حماية CSRF
    if not options.get("disable_csrf", False):
        vulnerabilities["csrf"] = check_csrf_protection(
            url,
            headers=options.get("headers"),
            cookies=options.get("cookies"),
            timeout=options.get("timeout", 10)
        )
        
        # تحليل النتائج وإضافة الثغرات المكتشفة
        if not vulnerabilities["csrf"]["has_csrf_protection"]:
            results.append({
                "name": "Missing CSRF Protection",
                "description": "The website does not implement CSRF protection, which could allow attackers to perform actions on behalf of authenticated users.",
                "severity": "High",
                "evidence": f"Found {vulnerabilities['csrf']['forms_without_csrf']} forms without CSRF tokens.",
                "recommendation": "Implement CSRF protection using tokens or same-site cookies."
            })
    
    # ... الكود الحالي ...
    
    return results
```

## تحسين وحدة موجودة

لتحسين وحدة موجودة، اتبع الخطوات التالية:

### 1. تحديد الوحدة التي تريد تحسينها

على سبيل المثال، لتحسين وحدة استخراج الروابط:

```python
# الدالة الحالية لاستخراج الروابط
def discover_links(url, depth=1, options=None):
    # ... الكود الحالي ...
    
    # تحسين: إضافة دعم لاستخراج الروابط من JavaScript
    if options.get("parse_javascript", False):
        js_links = extract_links_from_javascript(html_content)
        links.extend(js_links)
    
    # تحسين: إضافة دعم لاستخراج الروابط من CSS
    if options.get("parse_css", False):
        css_links = extract_links_from_css(html_content)
        links.extend(css_links)
    
    # ... الكود الحالي ...
    
    return links

# دالة جديدة لاستخراج الروابط من JavaScript
def extract_links_from_javascript(html_content):
    """
    استخراج الروابط من كود JavaScript.
    
    Args:
        html_content (str): محتوى HTML للصفحة
        
    Returns:
        list: قائمة بالروابط المستخرجة من JavaScript
    """
    links = []
    
    # استخراج كود JavaScript من وسوم <script>
    script_pattern = re.compile(r'<script[^>]*>(.*?)</script>', re.DOTALL)
    scripts = script_pattern.findall(html_content)
    
    # أنماط للبحث عن الروابط في كود JavaScript
    url_patterns = [
        re.compile(r'(?:url|href|src)\s*:\s*["\']([^"\']*)["\\']'),
        re.compile(r'(?:url|href|src)\s*=\s*["\']([^"\']*)["\\']'),
        re.compile(r'["\\']([^"\']*\.(?:html|php|asp|aspx|jsp|do)[^"\']*)["\']')
    ]
    
    for script in scripts:
        for pattern in url_patterns:
            script_links = pattern.findall(script)
            links.extend(script_links)
    
    return links
```

### 2. إضافة خيارات جديدة

```python
def parse_arguments():
    # ... الكود الحالي ...
    
    # إضافة خيارات جديدة للوحدة المحسنة
    parser.add_argument("--parse-javascript", action="store_true", help="Extract links from JavaScript code")
    parser.add_argument("--parse-css", action="store_true", help="Extract links from CSS code")
    
    # ... الكود الحالي ...
    
    return parser.parse_args()
```

## إضافة دعم لتنسيق تقرير جديد

لإضافة دعم لتنسيق تقرير جديد (مثل HTML)، اتبع الخطوات التالية:

### 1. إنشاء دالة لإنشاء التقرير

```python
def generate_html_report(results, output_file):
    """
    إنشاء تقرير HTML من نتائج الفحص.
    
    Args:
        results (dict): نتائج الفحص
        output_file (str): مسار ملف الإخراج
        
    Returns:
        bool: True إذا تم إنشاء التقرير بنجاح، False خلاف ذلك
    """
    try:
        # إنشاء قالب HTML
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Site Analyzer Report - {target}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; }}
                h1 {{ color: #333; }}
                .section {{ margin-bottom: 20px; }}
                .vulnerability {{ margin-bottom: 10px; padding: 10px; border-left: 4px solid #ccc; }}
                .critical {{ border-color: #ff0000; background-color: #ffeeee; }}
                .high {{ border-color: #ff9900; background-color: #fff6ee; }}
                .medium {{ border-color: #ffcc00; background-color: #fffbee; }}
                .low {{ border-color: #00cc00; background-color: #eeffee; }}
                .info {{ border-color: #0099ff; background-color: #eef6ff; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Site Analyzer Report</h1>
            <div class="section">
                <h2>Scan Information</h2>
                <table>
                    <tr><th>Target</th><td>{target}</td></tr>
                    <tr><th>Scan Date</th><td>{scan_date}</td></tr>
                    <tr><th>Scan Duration</th><td>{scan_duration}</td></tr>
                </table>
            </div>
            
            <div class="section">
                <h2>Vulnerabilities</h2>
                {vulnerabilities_html}
            </div>
            
            <div class="section">
                <h2>Metadata</h2>
                {metadata_html}
            </div>
            
            <div class="section">
                <h2>Links</h2>
                {links_html}
            </div>
            
            <div class="section">
                <h2>DNS Information</h2>
                {dns_html}
            </div>
            
            <div class="section">
                <h2>WHOIS Information</h2>
                {whois_html}
            </div>
            
            <div class="section">
                <h2>Security Headers</h2>
                {headers_html}
            </div>
            
            <footer>
                <p>Generated by Site Analyzer v1.0.0 by Saudi Crackers</p>
            </footer>
        </body>
        </html>
        """
        
        # إنشاء HTML للثغرات
        vulnerabilities_html = ""
        for vuln in results.get("vulnerabilities", []):
            severity_class = vuln["severity"].lower()
            vulnerabilities_html += f"""
            <div class="vulnerability {severity_class}">
                <h3>{vuln['name']} ({vuln['severity']})</h3>
                <p><strong>Description:</strong> {vuln['description']}</p>
                <p><strong>Evidence:</strong> {vuln['evidence']}</p>
                <p><strong>Recommendation:</strong> {vuln['recommendation']}</p>
            </div>
            """
        
        # إنشاء HTML للبيانات الوصفية
        metadata_html = "<table>"
        for key, value in results.get("metadata", {}).items():
            metadata_html += f"<tr><th>{key}</th><td>{value}</td></tr>"
        metadata_html += "</table>"
        
        # إنشاء HTML للروابط
        links_html = "<ul>"
        for link in results.get("links", []):
            links_html += f"<li><a href=\"{link}\" target=\"_blank\">{link}</a></li>"
        links_html += "</ul>"
        
        # إنشاء HTML لمعلومات DNS
        dns_html = "<table>"
        for key, value in results.get("dns_info", {}).items():
            if isinstance(value, dict):
                dns_html += f"<tr><th>{key}</th><td><pre>{json.dumps(value, indent=2)}</pre></td></tr>"
            else:
                dns_html += f"<tr><th>{key}</th><td>{value}</td></tr>"
        dns_html += "</table>"
        
        # إنشاء HTML لمعلومات WHOIS
        whois_html = "<table>"
        for key, value in results.get("whois_info", {}).items():
            whois_html += f"<tr><th>{key}</th><td>{value}</td></tr>"
        whois_html += "</table>"
        
        # إنشاء HTML لرؤوس الأمان
        headers_html = "<table>"
        headers_html += "<tr><th>Header</th><th>Status</th><th>Value</th></tr>"
        for header, info in results.get("security_headers", {}).items():
            status = "Present" if info.get("present", False) else "Missing"
            value = info.get("value", "")
            headers_html += f"<tr><th>{header}</th><td>{status}</td><td>{value}</td></tr>"
        headers_html += "</table>"
        
        # تجميع التقرير النهائي
        html_report = html_template.format(
            target=results.get("target", {}).get("url", ""),
            scan_date=results.get("scan_info", {}).get("date", ""),
            scan_duration=results.get("scan_info", {}).get("duration", ""),
            vulnerabilities_html=vulnerabilities_html,
            metadata_html=metadata_html,
            links_html=links_html,
            dns_html=dns_html,
            whois_html=whois_html,
            headers_html=headers_html
        )
        
        # حفظ التقرير في ملف
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_report)
        
        return True
    
    except Exception as e:
        print(f"Error generating HTML report: {str(e)}")
        return False
```

### 2. إضافة الدالة إلى وحدة التقارير

```python
def save_results(results, filename=None, output_dir="reports", report_format="json"):
    # ... الكود الحالي ...
    
    # إنشاء اسم الملف إذا لم يتم تحديده
    if filename is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        target_domain = results.get("target", {}).get("domain", "unknown")
        filename = f"{target_domain}_{timestamp}"
    
    # إنشاء مجلد الإخراج إذا لم يكن موجوداً
    os.makedirs(output_dir, exist_ok=True)
    
    # تحديد مسار الملف بناءً على تنسيق التقرير
    if report_format.lower() == "json":
        output_file = os.path.join(output_dir, f"{filename}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
    
    elif report_format.lower() == "html":
        output_file = os.path.join(output_dir, f"{filename}.html")
        generate_html_report(results, output_file)
    
    elif report_format.lower() == "csv":
        # تنفيذ منطق إنشاء تقرير CSV هنا
        pass
    
    else:
        print(f"Unsupported report format: {report_format}")
        return None
    
    print(f"Report saved to: {output_file}")
    return output_file
```

### 3. إضافة خيار لتنسيق التقرير

```python
def parse_arguments():
    # ... الكود الحالي ...
    
    # إضافة خيار لتنسيق التقرير
    parser.add_argument("--report-format", type=str, choices=["json", "html", "csv"], default="json",
                        help="Report format (json, html, csv)")
    
    # ... الكود الحالي ...
    
    return parser.parse_args()
```

## إضافة دعم للمصادقة

لإضافة دعم للمصادقة على المواقع المحمية بكلمة مرور، اتبع الخطوات التالية:

### 1. إنشاء وحدة المصادقة

```python
# authentication.py

def perform_basic_auth(url, username, password, timeout=10):
    """
    إجراء مصادقة أساسية على موقع ويب.
    
    Args:
        url (str): عنوان URL المستهدف
        username (str): اسم المستخدم
        password (str): كلمة المرور
        timeout (int, optional): مهلة الطلب بالثواني
        
    Returns:
        tuple: (نجاح المصادقة, جلسة requests)
    """
    import requests
    from requests.auth import HTTPBasicAuth
    
    session = requests.Session()
    
    try:
        response = session.get(
            url,
            auth=HTTPBasicAuth(username, password),
            timeout=timeout,
            allow_redirects=True
        )
        
        # التحقق من نجاح المصادقة
        if response.status_code == 200:
            return True, session
        else:
            return False, None
    
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        return False, None


def perform_form_auth(url, username_field, password_field, username, password, login_url=None, timeout=10):
    """
    إجراء مصادقة نموذج على موقع ويب.
    
    Args:
        url (str): عنوان URL المستهدف
        username_field (str): اسم حقل اسم المستخدم في النموذج
        password_field (str): اسم حقل كلمة المرور في النموذج
        username (str): اسم المستخدم
        password (str): كلمة المرور
        login_url (str, optional): عنوان URL لصفحة تسجيل الدخول (إذا كان مختلفاً عن URL المستهدف)
        timeout (int, optional): مهلة الطلب بالثواني
        
    Returns:
        tuple: (نجاح المصادقة, جلسة requests)
    """
    import requests
    from bs4 import BeautifulSoup
    
    session = requests.Session()
    
    try:
        # إذا لم يتم تحديد عنوان URL لصفحة تسجيل الدخول، استخدم URL المستهدف
        if login_url is None:
            login_url = url
        
        # الحصول على صفحة تسجيل الدخول للحصول على أي رموز CSRF
        response = session.get(login_url, timeout=timeout)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # البحث عن نموذج تسجيل الدخول
        login_form = None
        for form in soup.find_all("form"):
            if form.find("input", {"name": username_field}) and form.find("input", {"name": password_field}):
                login_form = form
                break
        
        if login_form is None:
            print("Login form not found")
            return False, None
        
        # استخراج عنوان URL للإرسال
        form_action = login_form.get("action")
        if form_action:
            if form_action.startswith("/"):
                # مسار نسبي
                from urllib.parse import urlparse
                parsed_url = urlparse(login_url)
                submit_url = f"{parsed_url.scheme}://{parsed_url.netloc}{form_action}"
            elif form_action.startswith("http"):
                # عنوان URL مطلق
                submit_url = form_action
            else:
                # مسار نسبي بدون / في البداية
                from urllib.parse import urljoin
                submit_url = urljoin(login_url, form_action)
        else:
            # إذا لم يتم تحديد action، استخدم عنوان URL لصفحة تسجيل الدخول
            submit_url = login_url
        
        # استخراج جميع الحقول المخفية (بما في ذلك رموز CSRF)
        form_data = {}
        for input_field in login_form.find_all("input"):
            input_name = input_field.get("name")
            input_value = input_field.get("value", "")
            input_type = input_field.get("type", "")
            
            if input_name and input_type == "hidden":
                form_data[input_name] = input_value
        
        # إضافة بيانات تسجيل الدخول
        form_data[username_field] = username
        form_data[password_field] = password
        
        # إرسال نموذج تسجيل الدخول
        response = session.post(
            submit_url,
            data=form_data,
            timeout=timeout,
            allow_redirects=True
        )
        
        # التحقق من نجاح المصادقة (هذا قد يختلف حسب الموقع)
        # يمكن التحقق من وجود عناصر معينة في الصفحة بعد تسجيل الدخول
        # أو التحقق من وجود كوكيز معينة
        
        # هنا نفترض أن المصادقة نجحت إذا تم إعادة توجيهنا أو إذا كان الرد 200
        if response.status_code == 200:
            # يمكن إضافة المزيد من التحققات هنا
            return True, session
        else:
            return False, None
    
    except Exception as e:
        print(f"Authentication error: {str(e)}")
        return False, None
```

### 2. دمج وحدة المصادقة في الأداة

```python
# استيراد وحدة المصادقة
from authentication import perform_basic_auth, perform_form_auth

class SiteAnalyzer:
    # ... الكود الحالي ...
    
    def __init__(self, target, **kwargs):
        # ... الكود الحالي ...
        
        # إعدادات المصادقة
        self.auth_type = kwargs.get("auth_type")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.username_field = kwargs.get("username_field")
        self.password_field = kwargs.get("password_field")
        self.login_url = kwargs.get("login_url")
        
        # جلسة requests
        self.session = None
        
        # ... الكود الحالي ...
    
    def authenticate(self):
        """
        إجراء المصادقة على الموقع المستهدف.
        
        Returns:
            bool: True إذا نجحت المصادقة، False خلاف ذلك
        """
        if not self.auth_type or not self.username or not self.password:
            # لا توجد معلومات مصادقة
            return False
        
        self._print_status(f"Authenticating to {self.target_url} using {self.auth_type} authentication...")
        
        if self.auth_type.lower() == "basic":
            success, self.session = perform_basic_auth(
                self.target_url,
                self.username,
                self.password,
                timeout=self.timeout
            )
        
        elif self.auth_type.lower() == "form":
            if not self.username_field or not self.password_field:
                self._print_status("Form authentication requires username_field and password_field", "error")
                return False
            
            success, self.session = perform_form_auth(
                self.target_url,
                self.username_field,
                self.password_field,
                self.username,
                self.password,
                login_url=self.login_url,
                timeout=self.timeout
            )
        
        else:
            self._print_status(f"Unsupported authentication type: {self.auth_type}", "error")
            return False
        
        if success:
            self._print_status("Authentication successful")
            return True
        else:
            self._print_status("Authentication failed", "error")
            return False
    
    def scan(self):
        # ... الكود الحالي ...
        
        # إجراء المصادقة إذا تم تحديد معلومات المصادقة
        if self.auth_type:
            auth_success = self.authenticate()
            results["authentication"] = {
                "type": self.auth_type,
                "success": auth_success
            }
            
            if not auth_success and not self.ignore_auth_failure:
                self._print_status("Aborting scan due to authentication failure", "error")
                return results
        
        # استخدام الجلسة المصادقة في الفحوصات الأخرى
        if self.session:
            # استخدام self.session بدلاً من requests.get في الفحوصات الأخرى
            pass
        
        # ... الكود الحالي ...
        
        return results
```

### 3. إضافة خيارات سطر الأوامر للمصادقة

```python
def parse_arguments():
    # ... الكود الحالي ...
    
    # إضافة مجموعة خيارات للمصادقة
    auth_group = parser.add_argument_group("Authentication Options")
    auth_group.add_argument("--auth-type", type=str, choices=["basic", "form"], help="Authentication type (basic, form)")
    auth_group.add_argument("--username", type=str, help="Username for authentication")
    auth_group.add_argument("--password", type=str, help="Password for authentication")
    auth_group.add_argument("--username-field", type=str, help="Username field name for form authentication")
    auth_group.add_argument("--password-field", type=str, help="Password field name for form authentication")
    auth_group.add_argument("--login-url", type=str, help="Login URL for form authentication")
    auth_group.add_argument("--ignore-auth-failure", action="store_true", help="Continue scanning even if authentication fails")
    
    # ... الكود الحالي ...
    
    return parser.parse_args()
```

## أفضل الممارسات للتطوير

### 1. اتباع معايير الكود

- اتبع معايير PEP 8 لكتابة كود Python نظيف ومتسق.
- استخدم أسماء وصفية للمتغيرات والدوال والفئات.
- أضف تعليقات توثيقية لجميع الدوال والفئات باستخدام صيغة docstring.

### 2. كتابة اختبارات

- اكتب اختبارات وحدة لكل وحدة جديدة تضيفها.
- استخدم إطار عمل pytest أو unittest لكتابة وتشغيل الاختبارات.
- تأكد من تغطية جميع المسارات والحالات الحدية في اختباراتك.

### 3. التعامل مع الأخطاء

- استخدم بلوكات try-except للتعامل مع الأخطاء المحتملة.
- قم بتسجيل رسائل خطأ مفيدة تساعد في تشخيص المشكلات.
- تجنب إخفاء الأخطاء دون معالجتها بشكل صحيح.

### 4. الأمان

- تأكد من أن الكود الذي تضيفه آمن ولا يتسبب في ثغرات أمنية.
- تجنب تخزين بيانات الاعتماد بشكل نصي في الكود.
- استخدم HTTPS للاتصالات الخارجية.

### 5. الأداء

- حسّن أداء الكود قدر الإمكان، خاصة للعمليات المكثفة.
- استخدم التنفيذ المتزامن عند الحاجة لتسريع العمليات.
- تجنب استهلاك الذاكرة بشكل مفرط.

## الخلاصة

يوفر هذا الدليل نظرة عامة على كيفية تطوير وإضافة ميزات جديدة إلى أداة Site Analyzer. باتباع هذه الإرشادات، يمكنك المساهمة في تحسين الأداة وتوسيع وظائفها.

تذكر دائماً اتباع إرشادات المساهمة الموجودة في ملف CONTRIBUTING.md وإضافة اختبارات مناسبة لأي كود جديد تضيفه.

إذا كان لديك أي أسئلة أو اقتراحات، يرجى فتح مشكلة (Issue) في مستودع GitHub أو التواصل مع فريق التطوير.