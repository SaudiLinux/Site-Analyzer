#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test suite for Site Analyzer Tool
Developed by: Saudi Crackers
Email: SaudiLinux7@gmail.com
"""

import unittest
import os
import sys
import json
from unittest.mock import patch, MagicMock
from datetime import datetime

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import functions from site_analyzer.py
from site_analyzer import (
    normalize_url,
    get_base_domain,
    get_random_user_agent,
    make_request,
    extract_metadata,
    extract_links,
    dns_enumeration,
    get_whois_info,
    check_security_headers,
    check_vulnerabilities,
    check_misconfigurations,
    save_results
)


class TestSiteAnalyzer(unittest.TestCase):
    """Test cases for Site Analyzer Tool"""

    def setUp(self):
        """Set up test environment"""
        self.test_url = "http://example.com"
        self.test_domain = "example.com"
        self.test_output_dir = "test_reports"
        
        # Create test output directory if it doesn't exist
        if not os.path.exists(self.test_output_dir):
            os.makedirs(self.test_output_dir)

    def tearDown(self):
        """Clean up test environment"""
        # Remove test files
        for file in os.listdir(self.test_output_dir):
            file_path = os.path.join(self.test_output_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        
        # Remove test directory
        if os.path.exists(self.test_output_dir):
            os.rmdir(self.test_output_dir)

    def test_normalize_url(self):
        """Test URL normalization"""
        self.assertEqual(normalize_url("example.com"), "http://example.com")
        self.assertEqual(normalize_url("http://example.com"), "http://example.com")
        self.assertEqual(normalize_url("https://example.com"), "https://example.com")

    def test_get_base_domain(self):
        """Test base domain extraction"""
        self.assertEqual(get_base_domain("http://example.com"), "example.com")
        self.assertEqual(get_base_domain("https://example.com/page"), "example.com")
        self.assertEqual(get_base_domain("http://sub.example.com"), "sub.example.com")

    def test_get_random_user_agent(self):
        """Test random user agent generation"""
        user_agent = get_random_user_agent()
        self.assertIsInstance(user_agent, str)
        self.assertTrue(len(user_agent) > 0)

    @patch('requests.get')
    def test_make_request(self, mock_get):
        """Test request handling"""
        # Mock successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Test</body></html>"
        mock_get.return_value = mock_response
        
        response = make_request(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "<html><body>Test</body></html>")
        
        # Mock request exception
        mock_get.side_effect = Exception("Test exception")
        response = make_request(self.test_url)
        self.assertIsNone(response)

    @patch('site_analyzer.make_request')
    def test_extract_metadata(self, mock_make_request):
        """Test metadata extraction"""
        # Mock response with metadata
        mock_response = MagicMock()
        mock_response.text = """
        <html>
            <head>
                <title>Test Title</title>
                <meta name="description" content="Test Description">
                <meta name="keywords" content="test, keywords">
                <meta name="author" content="Test Author">
                <meta name="generator" content="Test Generator">
                <meta name="robots" content="index, follow">
            </head>
            <body>Test</body>
        </html>
        """
        mock_response.headers = {
            'Server': 'Test Server',
            'X-Powered-By': 'Test Framework'
        }
        mock_make_request.return_value = mock_response
        
        metadata = extract_metadata(self.test_url)
        
        self.assertEqual(metadata['title'], "Test Title")
        self.assertEqual(metadata['description'], "Test Description")
        self.assertEqual(metadata['keywords'], "test, keywords")
        self.assertEqual(metadata['author'], "Test Author")
        self.assertEqual(metadata['generator'], "Test Generator")
        self.assertEqual(metadata['robots'], "index, follow")
        self.assertEqual(metadata['server'], "Test Server")
        self.assertIn("Test Framework", metadata['technologies'])

    @patch('site_analyzer.make_request')
    def test_extract_links(self, mock_make_request):
        """Test link extraction"""
        # Mock response with links
        mock_response = MagicMock()
        mock_response.text = """
        <html>
            <body>
                <a href="/page1">Page 1</a>
                <a href="https://example.com/page2">Page 2</a>
                <a href="https://external.com">External</a>
                <link href="/style.css" rel="stylesheet">
                <script src="/script.js"></script>
                <img src="/image.jpg">
            </body>
        </html>
        """
        mock_make_request.return_value = mock_response
        
        internal_links, external_links, resource_links = extract_links(self.test_url, self.test_domain)
        
        self.assertEqual(len(internal_links), 2)
        self.assertEqual(len(external_links), 1)
        self.assertEqual(len(resource_links), 3)
        
        self.assertIn("http://example.com/page1", internal_links)
        self.assertIn("https://example.com/page2", internal_links)
        self.assertIn("https://external.com", external_links)
        self.assertIn("http://example.com/style.css", resource_links)
        self.assertIn("http://example.com/script.js", resource_links)
        self.assertIn("http://example.com/image.jpg", resource_links)

    @patch('dns.resolver.resolve')
    def test_dns_enumeration(self, mock_resolve):
        """Test DNS enumeration"""
        # Mock DNS resolver
        mock_answer = MagicMock()
        mock_answer.__str__ = lambda self: "192.0.2.1"
        mock_resolve.return_value = [mock_answer]
        
        dns_records = dns_enumeration(self.test_domain)
        
        self.assertIsInstance(dns_records, dict)
        self.assertIn('A', dns_records)
        self.assertEqual(dns_records['A'], ["192.0.2.1"])

    @patch('whois.whois')
    def test_get_whois_info(self, mock_whois):
        """Test WHOIS information retrieval"""
        # Mock WHOIS response
        mock_whois.return_value = {
            'domain_name': 'EXAMPLE.COM',
            'registrar': 'Test Registrar',
            'creation_date': datetime.now(),
            'expiration_date': datetime.now(),
        }
        
        whois_info = get_whois_info(self.test_domain)
        
        self.assertIsInstance(whois_info, dict)
        self.assertEqual(whois_info['domain_name'], 'EXAMPLE.COM')
        self.assertEqual(whois_info['registrar'], 'Test Registrar')

    @patch('site_analyzer.make_request')
    def test_check_security_headers(self, mock_make_request):
        """Test security header checking"""
        # Mock response with security headers
        mock_response = MagicMock()
        mock_response.headers = {
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            'Content-Security-Policy': "default-src 'self'",
            'X-Content-Type-Options': 'nosniff',
        }
        mock_make_request.return_value = mock_response
        
        security_headers = check_security_headers(self.test_url)
        
        self.assertTrue(security_headers['Strict-Transport-Security']['present'])
        self.assertTrue(security_headers['Content-Security-Policy']['present'])
        self.assertTrue(security_headers['X-Content-Type-Options']['present'])
        self.assertFalse(security_headers['X-Frame-Options']['present'])

    @patch('site_analyzer.make_request')
    def test_check_vulnerabilities(self, mock_make_request):
        """Test vulnerability checking"""
        # Mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Index of /</body></html>"
        mock_make_request.return_value = mock_response
        
        # Mock metadata and security headers
        metadata = {
            'headers': {
                'Server': 'Apache/2.4.1',
                'X-Powered-By': 'PHP/7.2.1'
            }
        }
        
        security_headers = {
            'Strict-Transport-Security': {'present': False, 'value': None},
            'Content-Security-Policy': {'present': False, 'value': None},
        }
        
        vulnerabilities = check_vulnerabilities("http://example.com", metadata, security_headers)
        
        self.assertIsInstance(vulnerabilities, list)
        self.assertTrue(len(vulnerabilities) > 0)
        
        # Check if information disclosure vulnerability is detected
        info_disclosure_found = False
        for vuln in vulnerabilities:
            if "Information Disclosure" in vuln['name']:
                info_disclosure_found = True
                break
        
        self.assertTrue(info_disclosure_found)

    @patch('site_analyzer.make_request')
    def test_check_misconfigurations(self, mock_make_request):
        """Test misconfiguration checking"""
        # Mock response for sensitive files
        def mock_response_generator(url):
            response = MagicMock()
            response.status_code = 404
            response.text = ""
            
            # Mock .git/HEAD response
            if ".git/HEAD" in url:
                response.status_code = 200
                response.text = "ref: refs/heads/master"
            
            # Mock phpinfo.php response
            elif "phpinfo.php" in url:
                response.status_code = 200
                response.text = "<title>PHP Version 7.4.1</title>"
            
            return response
        
        mock_make_request.side_effect = mock_response_generator
        
        misconfigurations = check_misconfigurations(self.test_url)
        
        self.assertIsInstance(misconfigurations, list)
        self.assertTrue(len(misconfigurations) > 0)
        
        # Check if Git repository exposure is detected
        git_exposure_found = False
        for misconf in misconfigurations:
            if "Git Repository Exposure" in misconf['name']:
                git_exposure_found = True
                break
        
        self.assertTrue(git_exposure_found)

    def test_save_results(self):
        """Test results saving"""
        # Create test results
        results = {
            'target': self.test_url,
            'base_domain': self.test_domain,
            'scan_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'metadata': {'title': 'Test Title'},
            'vulnerabilities': [{'name': 'Test Vulnerability', 'severity': 'High'}]
        }
        
        # Save results
        output_file = save_results(self.test_url, results, self.test_output_dir)
        
        # Check if file exists
        self.assertTrue(os.path.exists(output_file))
        
        # Check file content
        with open(output_file, 'r') as f:
            saved_results = json.load(f)
        
        self.assertEqual(saved_results['target'], self.test_url)
        self.assertEqual(saved_results['base_domain'], self.test_domain)
        self.assertEqual(saved_results['metadata']['title'], 'Test Title')


if __name__ == '__main__':
    unittest.main()