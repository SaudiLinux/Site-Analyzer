# أمثلة على اختبارات أدوات تحليل وفحص أمان المواقع

**المطور:** Saudi Crackers  
**البريد الإلكتروني:** SaudiLinux7@gmail.com

هذا الملف يحتوي على أمثلة للاختبارات التي يمكن استخدامها للتحقق من صحة عمل أدوات تحليل وفحص أمان المواقع. يمكن استخدام هذه الاختبارات أثناء تطوير ميزات جديدة أو إصلاح الأخطاء.

## اختبارات أداة تحليل المواقع (Site Analyzer)

### اختبار استخراج البيانات الوصفية

```python
import unittest
from site_analyzer import SiteAnalyzer

class MetadataExtractionTest(unittest.TestCase):
    def setUp(self):
        self.analyzer = SiteAnalyzer("https://example.com", depth=1, timeout=10)
    
    def test_extract_metadata(self):
        metadata = self.analyzer.extract_metadata()
        self.assertIsNotNone(metadata)
        self.assertIn("title", metadata)
        self.assertIn("description", metadata)

    def test_extract_technologies(self):
        technologies = self.analyzer.extract_technologies()
        self.assertIsInstance(technologies, list)
```

### اختبار استخراج الروابط

```python
import unittest
from site_analyzer import SiteAnalyzer

class LinkExtractionTest(unittest.TestCase):
    def setUp(self):
        self.analyzer = SiteAnalyzer("https://example.com", depth=1, timeout=10)
    
    def test_extract_internal_links(self):
        links = self.analyzer.extract_internal_links()
        self.assertIsInstance(links, list)
        
    def test_extract_external_links(self):
        links = self.analyzer.extract_external_links()
        self.assertIsInstance(links, list)
        
    def test_extract_resource_links(self):
        links = self.analyzer.extract_resource_links()
        self.assertIsInstance(links, list)
        self.assertTrue(any(link.endswith(('.js', '.css', '.png', '.jpg', '.jpeg', '.gif')) for link in links))
```

### اختبار فحص الثغرات

```python
import unittest
from site_analyzer import SiteAnalyzer

class VulnerabilityCheckTest(unittest.TestCase):
    def setUp(self):
        self.analyzer = SiteAnalyzer("https://example.com", depth=1, timeout=10)
    
    def test_check_security_headers(self):
        headers = self.analyzer.check_security_headers()
        self.assertIsInstance(headers, dict)
        self.assertIn("X-XSS-Protection", headers)
        self.assertIn("Content-Security-Policy", headers)
        
    def test_check_ssl_tls(self):
        ssl_issues = self.analyzer.check_ssl_tls()
        self.assertIsInstance(ssl_issues, list)
        
    def test_check_common_misconfigurations(self):
        misconfigurations = self.analyzer.check_common_misconfigurations()
        self.assertIsInstance(misconfigurations, list)
```

## اختبارات أداة استغلال الثغرات (Vulnerability Exploiter)

### اختبار تحميل الثغرات

```python
import unittest
import json
import tempfile
from vulnerability_exploiter import VulnerabilityExploiter

class LoadVulnerabilitiesTest(unittest.TestCase):
    def setUp(self):
        # إنشاء ملف مؤقت يحتوي على بيانات الثغرات
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        vulnerabilities = {
            "vulnerabilities": [
                {
                    "type": "XSS",
                    "url": "https://example.com/search?q=test",
                    "severity": "High",
                    "description": "Reflected XSS in search parameter"
                },
                {
                    "type": "SQL Injection",
                    "url": "https://example.com/product?id=1",
                    "severity": "Critical",
                    "description": "SQL Injection in product ID parameter"
                }
            ]
        }
        self.temp_file.write(json.dumps(vulnerabilities).encode())
        self.temp_file.close()
        self.exploiter = VulnerabilityExploiter()
    
    def test_load_vulnerabilities(self):
        result = self.exploiter.load_vulnerabilities(self.temp_file.name)
        self.assertTrue(result)
        self.assertEqual(len(self.exploiter.vulnerabilities), 2)
        self.assertEqual(self.exploiter.vulnerabilities[0]["type"], "XSS")
        self.assertEqual(self.exploiter.vulnerabilities[1]["type"], "SQL Injection")
```

### اختبار تقنيات الاستغلال

```python
import unittest
from unittest.mock import patch
from vulnerability_exploiter import VulnerabilityExploiter

class ExploitationTechniquesTest(unittest.TestCase):
    def setUp(self):
        self.exploiter = VulnerabilityExploiter()
        self.exploiter.vulnerabilities = [
            {
                "type": "XSS",
                "url": "https://example.com/search?q=test",
                "severity": "High",
                "description": "Reflected XSS in search parameter"
            },
            {
                "type": "SQL Injection",
                "url": "https://example.com/product?id=1",
                "severity": "Critical",
                "description": "SQL Injection in product ID parameter"
            }
        ]
    
    @patch('vulnerability_exploiter.VulnerabilityExploiter.send_request')
    def test_exploit_xss(self, mock_send_request):
        # تهيئة المحاكاة لإرجاع استجابة تحتوي على حمولة XSS
        mock_response = type('obj', (object,), {
            'status_code': 200,
            'text': '<html><body>test<script>alert(1)</script></body></html>'
        })
        mock_send_request.return_value = mock_response
        
        result = self.exploiter.exploit_xss(self.exploiter.vulnerabilities[0])
        self.assertTrue(result["success"])
        self.assertIn("payload", result)
        self.assertIn("evidence", result)
    
    @patch('vulnerability_exploiter.VulnerabilityExploiter.send_request')
    def test_exploit_sql_injection(self, mock_send_request):
        # تهيئة المحاكاة لإرجاع استجابة تحتوي على خطأ SQL
        mock_response = type('obj', (object,), {
            'status_code': 200,
            'text': 'Error: You have an error in your SQL syntax'
        })
        mock_send_request.return_value = mock_response
        
        result = self.exploiter.exploit_sql_injection(self.exploiter.vulnerabilities[1])
        self.assertTrue(result["success"])
        self.assertIn("payload", result)
        self.assertIn("evidence", result)
```

## كيفية تشغيل الاختبارات

يمكن تشغيل الاختبارات باستخدام الأمر التالي:

```bash
python -m unittest discover -s tests
```

أو باستخدام pytest:

```bash
pytest tests/
```

## إضافة اختبارات جديدة

عند إضافة ميزات جديدة أو إصلاح الأخطاء، يجب إضافة اختبارات جديدة للتحقق من صحة التغييرات. اتبع الإرشادات التالية:

1. قم بإنشاء ملف اختبار جديد في مجلد `tests/`
2. اتبع نمط الاختبارات الحالية
3. تأكد من تغطية جميع الحالات المحتملة
4. قم بتشغيل الاختبارات للتأكد من نجاحها

## اختبارات التكامل

بالإضافة إلى اختبارات الوحدة، يجب إجراء اختبارات التكامل للتأكد من أن الأدوات تعمل بشكل صحيح معًا. يمكن إنشاء اختبارات التكامل في مجلد `tests/integration/`.

```python
import unittest
from site_analyzer import SiteAnalyzer
from vulnerability_exploiter import VulnerabilityExploiter
import os
import json

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.target_url = "https://example.com"
        self.analyzer = SiteAnalyzer(self.target_url, depth=1, timeout=10)
        self.exploiter = VulnerabilityExploiter()
    
    def test_full_workflow(self):
        # تحليل الموقع
        self.analyzer.scan()
        
        # حفظ النتائج في ملف مؤقت
        report_file = "temp_report.json"
        self.analyzer.save_report(report_file)
        
        # التحقق من وجود الملف
        self.assertTrue(os.path.exists(report_file))
        
        # تحميل الثغرات من التقرير
        self.exploiter.load_vulnerabilities(report_file)
        
        # التحقق من تحميل الثغرات بنجاح
        self.assertIsInstance(self.exploiter.vulnerabilities, list)
        
        # استغلال الثغرات
        exploitation_report = self.exploiter.exploit_all()
        
        # التحقق من تقرير الاستغلال
        self.assertIsInstance(exploitation_report, dict)
        self.assertIn("exploited_vulnerabilities", exploitation_report)
        
        # تنظيف
        os.remove(report_file)
```

## تغطية الاختبارات

يمكن استخدام أداة `coverage` لقياس تغطية الاختبارات للكود:

```bash
coverage run -m unittest discover
coverage report
coverage html  # لإنشاء تقرير HTML
```

يجب أن تكون تغطية الاختبارات على الأقل 80% من الكود.