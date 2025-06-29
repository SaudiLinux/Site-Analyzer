# استخدام Site Analyzer كمكتبة في مشاريع Python

بالإضافة إلى استخدام Site Analyzer كأداة سطر أوامر، يمكنك أيضاً استخدامها كمكتبة في مشاريع Python الخاصة بك. يوضح هذا الدليل كيفية استخدام وظائف Site Analyzer في التطبيقات والسكريبتات الخاصة بك.

## التثبيت

قبل استخدام Site Analyzer كمكتبة، تأكد من تثبيتها في بيئتك:

```bash
pip install -r requirements.txt
# أو إذا قمت بتثبيتها كحزمة
pip install site-analyzer
```

## استيراد المكتبة

```python
# استيراد الوحدة الرئيسية
from site_analyzer import SiteAnalyzer

# استيراد وحدات محددة
from site_analyzer import (
    metadata_extractor,
    link_discoverer,
    dns_checker,
    whois_checker,
    security_headers_checker,
    vulnerability_scanner
)
```

## استخدام الفئة الرئيسية SiteAnalyzer

### إنشاء مثيل جديد

```python
from site_analyzer import SiteAnalyzer

# إنشاء مثيل جديد مع الإعدادات الافتراضية
analyzer = SiteAnalyzer(target="example.com")

# إنشاء مثيل جديد مع إعدادات مخصصة
analyzer = SiteAnalyzer(
    target="example.com",
    depth=2,
    timeout=15,
    threads=10,
    verbose=True,
    output_dir="my_reports",
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    proxy="http://127.0.0.1:8080"
)
```

### تنفيذ الفحص الكامل

```python
# تنفيذ الفحص الكامل وإرجاع النتائج كقاموس
results = analyzer.scan()

# طباعة النتائج
print(f"Target: {results['target']['url']}")
print(f"Title: {results['metadata']['title']}")
print(f"IP Address: {results['dns_info']['ip_address']}")
print(f"Found {len(results['links'])} unique links")
print(f"Found {len(results['vulnerabilities'])} potential vulnerabilities")
```

### تنفيذ فحوصات محددة

```python
# فحص البيانات الوصفية فقط
metadata = analyzer.extract_metadata()
print(f"Title: {metadata['title']}")
print(f"Description: {metadata['description']}")

# فحص الروابط فقط
links = analyzer.discover_links()
for link in links:
    print(f"Found link: {link}")

# فحص معلومات DNS فقط
dns_info = analyzer.check_dns()
print(f"IP Address: {dns_info['ip_address']}")
print(f"DNS Records: {dns_info['records']}")

# فحص معلومات WHOIS فقط
whois_info = analyzer.check_whois()
print(f"Registrar: {whois_info['registrar']}")
print(f"Creation Date: {whois_info['creation_date']}")

# فحص رؤوس الأمان فقط
headers = analyzer.check_security_headers()
for header, status in headers.items():
    print(f"{header}: {status}")

# فحص الثغرات فقط
vulnerabilities = analyzer.scan_vulnerabilities()
for vuln in vulnerabilities:
    print(f"[{vuln['severity']}] {vuln['name']}: {vuln['description']}")
```

### حفظ النتائج

```python
# حفظ النتائج في ملف JSON
analyzer.save_results(results, "my_scan_results.json")

# حفظ النتائج في ملف JSON مع تحديد المجلد
analyzer.save_results(results, "scan_results.json", "my_reports")
```

## استخدام الوحدات الفردية

### استخدام وحدة استخراج البيانات الوصفية

```python
from site_analyzer.metadata_extractor import extract_metadata

# استخراج البيانات الوصفية من URL
metadata = extract_metadata("https://example.com")
print(f"Title: {metadata['title']}")
print(f"Description: {metadata['description']}")
print(f"Keywords: {metadata['keywords']}")
```

### استخدام وحدة اكتشاف الروابط

```python
from site_analyzer.link_discoverer import discover_links

# اكتشاف الروابط في URL
links = discover_links("https://example.com", depth=1)
for link in links:
    print(f"Found link: {link}")
```

### استخدام وحدة فحص DNS

```python
from site_analyzer.dns_checker import check_dns

# فحص معلومات DNS لنطاق
dns_info = check_dns("example.com")
print(f"IP Address: {dns_info['ip_address']}")
print(f"DNS Records:")
for record_type, records in dns_info['records'].items():
    print(f"  {record_type}: {records}")
```

### استخدام وحدة فحص WHOIS

```python
from site_analyzer.whois_checker import check_whois

# فحص معلومات WHOIS لنطاق
whois_info = check_whois("example.com")
print(f"Registrar: {whois_info['registrar']}")
print(f"Creation Date: {whois_info['creation_date']}")
print(f"Expiration Date: {whois_info['expiration_date']}")
```

### استخدام وحدة فحص رؤوس الأمان

```python
from site_analyzer.security_headers_checker import check_security_headers

# فحص رؤوس الأمان لموقع
headers = check_security_headers("https://example.com")
for header, status in headers.items():
    if status['present']:
        print(f"[+] {header}: {status['value']}")
    else:
        print(f"[-] Missing: {header}")
```

### استخدام وحدة فحص الثغرات

```python
from site_analyzer.vulnerability_scanner import scan_vulnerabilities

# فحص الثغرات في موقع
vulnerabilities = scan_vulnerabilities("https://example.com")
for vuln in vulnerabilities:
    print(f"[{vuln['severity']}] {vuln['name']}")
    print(f"  Description: {vuln['description']}")
    print(f"  Recommendation: {vuln['recommendation']}")
```

## أمثلة متقدمة

### فحص متعدد المواقع

```python
from site_analyzer import SiteAnalyzer
import json

def scan_multiple_sites(sites, output_dir="reports"):
    results = {}
    for site in sites:
        print(f"Scanning {site}...")
        analyzer = SiteAnalyzer(target=site, output_dir=output_dir)
        results[site] = analyzer.scan()
    
    # حفظ النتائج المجمعة
    with open(f"{output_dir}/multiple_sites_scan.json", "w") as f:
        json.dump(results, f, indent=4)
    
    return results

# استخدام الدالة
sites = ["example.com", "example.org", "example.net"]
results = scan_multiple_sites(sites)
```

### فحص مخصص مع تصفية النتائج

```python
from site_analyzer import SiteAnalyzer

def custom_scan(target, severity_filter="Medium"):
    analyzer = SiteAnalyzer(target=target)
    results = analyzer.scan()
    
    # تصفية الثغرات حسب مستوى الخطورة
    severity_levels = {"Critical": 4, "High": 3, "Medium": 2, "Low": 1, "Info": 0}
    min_severity = severity_levels.get(severity_filter, 0)
    
    filtered_vulnerabilities = []
    for vuln in results["vulnerabilities"]:
        if severity_levels.get(vuln["severity"], 0) >= min_severity:
            filtered_vulnerabilities.append(vuln)
    
    results["vulnerabilities"] = filtered_vulnerabilities
    return results

# استخدام الدالة
results = custom_scan("example.com", "High")
print(f"Found {len(results['vulnerabilities'])} high or critical vulnerabilities")
```

### استخدام الأداة في تطبيق ويب

```python
from flask import Flask, request, jsonify
from site_analyzer import SiteAnalyzer

app = Flask(__name__)

@app.route('/api/scan', methods=['POST'])
def scan_site():
    data = request.json
    target = data.get('target')
    
    if not target:
        return jsonify({"error": "Target URL is required"}), 400
    
    try:
        analyzer = SiteAnalyzer(
            target=target,
            depth=data.get('depth', 1),
            timeout=data.get('timeout', 10),
            threads=data.get('threads', 5)
        )
        
        results = analyzer.scan()
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

## معالجة الأخطاء

```python
from site_analyzer import SiteAnalyzer
import requests.exceptions

try:
    analyzer = SiteAnalyzer(target="example.com")
    results = analyzer.scan()
    print("Scan completed successfully!")
    
    # حفظ النتائج
    analyzer.save_results(results)
    
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the target site")
    
except requests.exceptions.Timeout:
    print("Error: Request timed out")
    
except requests.exceptions.TooManyRedirects:
    print("Error: Too many redirects")
    
except Exception as e:
    print(f"Error: {str(e)}")
```

## تخصيص الفحص

### إضافة User-Agent مخصص

```python
from site_analyzer import SiteAnalyzer

# تحديد User-Agent مخصص
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

analyzer = SiteAnalyzer(
    target="example.com",
    user_agent=user_agent
)

results = analyzer.scan()
```

### استخدام وكيل (Proxy)

```python
from site_analyzer import SiteAnalyzer

# استخدام وكيل HTTP
analyzer = SiteAnalyzer(
    target="example.com",
    proxy="http://127.0.0.1:8080"
)

# استخدام وكيل SOCKS
analyzer = SiteAnalyzer(
    target="example.com",
    proxy="socks5://127.0.0.1:9050"
)

results = analyzer.scan()
```

### استخدام الكوكيز للمصادقة

```python
from site_analyzer import SiteAnalyzer

# تحديد الكوكيز كقاموس
cookies = {
    "session_id": "abc123",
    "user_id": "456"
}

analyzer = SiteAnalyzer(
    target="example.com",
    cookies=cookies
)

results = analyzer.scan()
```

## ملاحظات هامة

1. **الاستخدام المسؤول**: استخدم هذه المكتبة فقط على المواقع التي لديك إذن قانوني لفحصها.

2. **معالجة الأخطاء**: قم دائماً بتضمين معالجة الأخطاء في التطبيقات التي تستخدم هذه المكتبة، حيث قد تحدث أخطاء مختلفة أثناء الفحص.

3. **الأداء**: قد تستغرق عمليات الفحص العميقة وقتاً طويلاً وتستهلك موارد كبيرة. ضع ذلك في اعتبارك عند استخدام المكتبة في تطبيقات الإنتاج.

4. **التحديثات**: تحقق دائماً من وجود تحديثات للمكتبة، حيث قد تتضمن التحديثات إصلاحات للأخطاء وتحسينات في الأداء وميزات جديدة.

5. **التوثيق**: راجع ملفات التوثيق الأخرى للحصول على معلومات مفصلة حول كل وحدة ووظيفة.

## المساهمة

إذا وجدت أي أخطاء أو كان لديك اقتراحات لتحسين المكتبة، يرجى فتح مشكلة (Issue) أو إرسال طلب سحب (Pull Request) في مستودع GitHub.