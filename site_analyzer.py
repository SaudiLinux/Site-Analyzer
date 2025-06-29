#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Site Analyzer Tool
Developed by: Saudi Crackers
Email: SaudiLinux7@gmail.com

This tool performs comprehensive website analysis including:
- Metadata extraction
- File enumeration
- Link discovery
- Vulnerability scanning
"""

import argparse
import concurrent.futures
import dns.resolver
import json
import os
import random
import re
import requests
import socket
import ssl
import sys
import time
import urllib.parse
import whois
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
from datetime import datetime
from fake_useragent import UserAgent
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

# Banner
def print_banner():
    banner = f'''
{Fore.GREEN}╔═══════════════════════════════════════════════════════════════════════╗
{Fore.GREEN}║ {Fore.YELLOW}███████╗██╗████████╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗{Fore.GREEN} ║
{Fore.GREEN}║ {Fore.YELLOW}██╔════╝██║╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║{Fore.GREEN} ║
{Fore.GREEN}║ {Fore.YELLOW}███████╗██║   ██║   █████╗      ███████╗██║     ███████║██╔██╗ ██║{Fore.GREEN} ║
{Fore.GREEN}║ {Fore.YELLOW}╚════██║██║   ██║   ██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║{Fore.GREEN} ║
{Fore.GREEN}║ {Fore.YELLOW}███████║██║   ██║   ███████╗    ███████║╚██████╗██║  ██║██║ ╚████║{Fore.GREEN} ║
{Fore.GREEN}║ {Fore.YELLOW}╚══════╝╚═╝   ╚═╝   ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝{Fore.GREEN} ║
{Fore.GREEN}╠═══════════════════════════════════════════════════════════════════════╣
{Fore.GREEN}║ {Fore.CYAN}                      Site Analyzer Tool v1.0                      {Fore.GREEN} ║
{Fore.GREEN}║ {Fore.CYAN}                  Developed by: Saudi Crackers                    {Fore.GREEN} ║
{Fore.GREEN}║ {Fore.CYAN}                  Email: SaudiLinux7@gmail.com                    {Fore.GREEN} ║
{Fore.GREEN}╚═══════════════════════════════════════════════════════════════════════╝
'''
    print(banner)

# User-Agent rotation
def get_random_user_agent():
    try:
        ua = UserAgent()
        return ua.random
    except:
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
        ]
        return random.choice(user_agents)

# Request handler with retry mechanism
def make_request(url, timeout=10, max_retries=3):
    headers = {
        'User-Agent': get_random_user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout, verify=False, allow_redirects=True)
            return response
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                print(f"{Fore.RED}[!] Error accessing {url}: {str(e)}")
                return None
            time.sleep(2)  # Wait before retrying
    return None

# Normalize URL
def normalize_url(url):
    if not url.startswith('http'):
        url = 'http://' + url
    return url

# Extract base domain from URL
def get_base_domain(url):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.netloc

# Extract metadata from website
def extract_metadata(url):
    print(f"\n{Fore.CYAN}[*] Extracting metadata from {url}...")
    metadata = {
        'title': None,
        'description': None,
        'keywords': None,
        'generator': None,
        'robots': None,
        'author': None,
        'server': None,
        'technologies': [],
        'headers': {}
    }
    
    response = make_request(url)
    if not response:
        return metadata
    
    # Extract HTTP headers
    for header, value in response.headers.items():
        metadata['headers'][header] = value
        
        # Detect server technology
        if header.lower() == 'server':
            metadata['server'] = value
        elif header.lower() == 'x-powered-by':
            metadata['technologies'].append(value)
    
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title_tag = soup.find('title')
        if title_tag:
            metadata['title'] = title_tag.text.strip()
        
        # Extract meta tags
        for meta in soup.find_all('meta'):
            if meta.get('name') and meta.get('content'):
                name = meta.get('name').lower()
                content = meta.get('content')
                
                if name == 'description':
                    metadata['description'] = content
                elif name == 'keywords':
                    metadata['keywords'] = content
                elif name == 'author':
                    metadata['author'] = content
                elif name == 'generator':
                    metadata['generator'] = content
                    metadata['technologies'].append(content)
                elif name == 'robots':
                    metadata['robots'] = content
        
        # Detect common technologies
        tech_patterns = {
            'WordPress': ['wp-content', 'wp-includes', 'wordpress'],
            'Joomla': ['joomla', 'com_content', 'com_users'],
            'Drupal': ['drupal', 'sites/all', 'sites/default'],
            'Magento': ['magento', 'skin/frontend', 'Mage.Cookies'],
            'Bootstrap': ['bootstrap.min.css', 'bootstrap.min.js'],
            'jQuery': ['jquery.min.js', 'jquery-'],
            'React': ['react.js', 'react-dom.js', 'react.min.js'],
            'Angular': ['angular.js', 'ng-app', 'ng-controller'],
            'Vue.js': ['vue.js', 'vue.min.js', 'v-bind', 'v-on'],
            'PHP': ['php', '.php'],
            'ASP.NET': ['.aspx', '.ashx', 'asp.net'],
            'Laravel': ['laravel', 'csrf-token'],
        }
        
        page_text = response.text.lower()
        for tech, patterns in tech_patterns.items():
            for pattern in patterns:
                if pattern.lower() in page_text:
                    if tech not in metadata['technologies']:
                        metadata['technologies'].append(tech)
                    break
        
    except Exception as e:
        print(f"{Fore.RED}[!] Error parsing HTML: {str(e)}")
    
    return metadata

# Extract all links from website
def extract_links(url, base_domain=None):
    print(f"\n{Fore.CYAN}[*] Extracting links from {url}...")
    if not base_domain:
        base_domain = get_base_domain(url)
    
    internal_links = set()
    external_links = set()
    resource_links = set()
    
    response = make_request(url)
    if not response:
        return internal_links, external_links, resource_links
    
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all links
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            absolute_url = urllib.parse.urljoin(url, href)
            
            # Skip fragment links and javascript
            if href.startswith('#') or href.startswith('javascript:'):
                continue
                
            # Categorize links
            if get_base_domain(absolute_url) == base_domain:
                internal_links.add(absolute_url)
            else:
                external_links.add(absolute_url)
        
        # Extract resource links (CSS, JS, images, etc.)
        resource_tags = {
            'link': 'href',  # CSS
            'script': 'src',  # JavaScript
            'img': 'src',     # Images
            'video': 'src',   # Videos
            'audio': 'src',   # Audio
            'source': 'src',  # Media source
        }
        
        for tag, attr in resource_tags.items():
            for element in soup.find_all(tag):
                if element.get(attr):
                    resource_url = urllib.parse.urljoin(url, element[attr])
                    resource_links.add(resource_url)
                    
    except Exception as e:
        print(f"{Fore.RED}[!] Error extracting links: {str(e)}")
    
    return internal_links, external_links, resource_links

# Perform DNS enumeration
def dns_enumeration(domain):
    print(f"\n{Fore.CYAN}[*] Performing DNS enumeration for {domain}...")
    dns_records = {
        'A': [],
        'AAAA': [],
        'MX': [],
        'NS': [],
        'TXT': [],
        'CNAME': [],
        'SOA': [],
    }
    
    for record_type in dns_records.keys():
        try:
            answers = dns.resolver.resolve(domain, record_type)
            for answer in answers:
                dns_records[record_type].append(str(answer))
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.exception.Timeout):
            pass
        except Exception as e:
            print(f"{Fore.RED}[!] Error retrieving {record_type} records: {str(e)}")
    
    return dns_records

# Get WHOIS information
def get_whois_info(domain):
    print(f"\n{Fore.CYAN}[*] Retrieving WHOIS information for {domain}...")
    whois_info = {}
    
    try:
        w = whois.whois(domain)
        whois_info = w
    except Exception as e:
        print(f"{Fore.RED}[!] Error retrieving WHOIS information: {str(e)}")
    
    return whois_info

# Check for common security headers
def check_security_headers(url):
    print(f"\n{Fore.CYAN}[*] Checking security headers for {url}...")
    security_headers = {
        'Strict-Transport-Security': {'present': False, 'value': None},
        'Content-Security-Policy': {'present': False, 'value': None},
        'X-Content-Type-Options': {'present': False, 'value': None},
        'X-Frame-Options': {'present': False, 'value': None},
        'X-XSS-Protection': {'present': False, 'value': None},
        'Referrer-Policy': {'present': False, 'value': None},
        'Feature-Policy': {'present': False, 'value': None},
        'Permissions-Policy': {'present': False, 'value': None},
    }
    
    response = make_request(url)
    if not response:
        return security_headers
    
    for header in security_headers.keys():
        if header in response.headers:
            security_headers[header]['present'] = True
            security_headers[header]['value'] = response.headers[header]
    
    return security_headers

# Check for common vulnerabilities
def check_vulnerabilities(url, metadata, security_headers):
    print(f"\n{Fore.CYAN}[*] Checking for common vulnerabilities on {url}...")
    vulnerabilities = []
    
    # Check for SSL/TLS issues
    if url.startswith('https'):
        try:
            domain = get_base_domain(url)
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    # Check certificate expiration
                    expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    days_to_expire = (expire_date - datetime.now()).days
                    
                    if days_to_expire < 30:
                        vulnerabilities.append({
                            'name': 'SSL Certificate Expiring Soon',
                            'severity': 'Medium',
                            'description': f'SSL certificate will expire in {days_to_expire} days',
                            'recommendation': 'Renew the SSL certificate before it expires'
                        })
                        
                    # Check for weak cipher suites (simplified check)
                    cipher = ssock.cipher()
                    if cipher and ('RC4' in cipher[0] or 'DES' in cipher[0] or 'MD5' in cipher[0]):
                        vulnerabilities.append({
                            'name': 'Weak SSL/TLS Cipher Suite',
                            'severity': 'High',
                            'description': f'Weak cipher suite detected: {cipher[0]}',
                            'recommendation': 'Configure server to use strong cipher suites only'
                        })
        except Exception as e:
            vulnerabilities.append({
                'name': 'SSL/TLS Configuration Issue',
                'severity': 'Medium',
                'description': f'Error checking SSL/TLS configuration: {str(e)}',
                'recommendation': 'Verify SSL/TLS configuration on the server'
            })
    else:
        vulnerabilities.append({
            'name': 'No SSL/TLS',
            'severity': 'High',
            'description': 'Website does not use HTTPS',
            'recommendation': 'Implement HTTPS with a valid SSL certificate'
        })
    
    # Check for missing security headers
    for header, info in security_headers.items():
        if not info['present']:
            severity = 'Medium'
            if header in ['Strict-Transport-Security', 'Content-Security-Policy']:
                severity = 'High'
            elif header in ['X-XSS-Protection', 'Feature-Policy', 'Permissions-Policy']:
                severity = 'Low'
                
            vulnerabilities.append({
                'name': f'Missing {header} Header',
                'severity': severity,
                'description': f'The {header} security header is not set',
                'recommendation': f'Implement the {header} header to enhance security'
            })
    
    # Check for information disclosure in HTTP headers
    sensitive_headers = ['Server', 'X-Powered-By', 'X-AspNet-Version', 'X-AspNetMvc-Version']
    for header in sensitive_headers:
        if header in metadata['headers']:
            vulnerabilities.append({
                'name': 'Information Disclosure in HTTP Headers',
                'severity': 'Low',
                'description': f'The {header} header reveals technology information: {metadata["headers"][header]}',
                'recommendation': f'Configure server to remove or obfuscate the {header} header'
            })
    
    # Check for directory listing
    common_dirs = ['images/', 'css/', 'js/', 'backup/', 'admin/', 'uploads/', 'temp/']
    for directory in common_dirs:
        dir_url = urllib.parse.urljoin(url, directory)
        response = make_request(dir_url)
        
        if response and response.status_code == 200:
            # Simple heuristic to detect directory listing
            if 'Index of' in response.text or 'Directory Listing' in response.text:
                vulnerabilities.append({
                    'name': 'Directory Listing Enabled',
                    'severity': 'Medium',
                    'description': f'Directory listing is enabled at {dir_url}',
                    'recommendation': 'Disable directory listing on the web server'
                })
                break
    
    # Check for robots.txt and sensitive information
    robots_url = urllib.parse.urljoin(url, 'robots.txt')
    response = make_request(robots_url)
    
    if response and response.status_code == 200:
        sensitive_patterns = ['admin', 'backup', 'wp-admin', 'phpMyAdmin', 'config', 'database', 'secret']
        for pattern in sensitive_patterns:
            if pattern in response.text:
                vulnerabilities.append({
                    'name': 'Sensitive Information in robots.txt',
                    'severity': 'Medium',
                    'description': f'robots.txt contains potentially sensitive paths with keyword: {pattern}',
                    'recommendation': 'Review and remove sensitive paths from robots.txt'
                })
                break
    
    return vulnerabilities

# Check for common misconfigurations
def check_misconfigurations(url):
    print(f"\n{Fore.CYAN}[*] Checking for common misconfigurations on {url}...")
    misconfigurations = []
    
    # Check for common sensitive files
    sensitive_files = [
        '.git/HEAD',
        '.env',
        'config.php',
        'wp-config.php',
        'config.js',
        'database.yml',
        'credentials.xml',
        'sitemap.xml',
        'crossdomain.xml',
        'phpinfo.php',
        'test.php',
        'backup.sql',
        'backup.zip',
        'backup.tar.gz',
    ]
    
    for file in sensitive_files:
        file_url = urllib.parse.urljoin(url, file)
        response = make_request(file_url)
        
        if response and response.status_code == 200:
            # Simple check to avoid false positives
            if file == '.git/HEAD' and 'ref:' in response.text:
                misconfigurations.append({
                    'name': 'Git Repository Exposure',
                    'severity': 'High',
                    'description': f'Git repository information is exposed at {file_url}',
                    'recommendation': 'Restrict access to .git directory using .htaccess or web server configuration'
                })
            elif file == '.env' and ('DB_' in response.text or 'API_' in response.text or 'SECRET' in response.text):
                misconfigurations.append({
                    'name': 'Environment File Exposure',
                    'severity': 'Critical',
                    'description': f'Environment file with potential secrets is exposed at {file_url}',
                    'recommendation': 'Remove or restrict access to .env file immediately'
                })
            elif file == 'phpinfo.php' and 'PHP Version' in response.text:
                misconfigurations.append({
                    'name': 'PHP Information Disclosure',
                    'severity': 'High',
                    'description': f'PHP configuration information is exposed at {file_url}',
                    'recommendation': 'Remove phpinfo.php file from production environment'
                })
            elif file.endswith(('.zip', '.tar.gz', '.sql')):
                misconfigurations.append({
                    'name': 'Backup File Exposure',
                    'severity': 'High',
                    'description': f'Potential backup file is accessible at {file_url}',
                    'recommendation': 'Remove backup files from web-accessible directories'
                })
            elif 'config' in file and ('DB_' in response.text or 'database' in response.text.lower() or 'password' in response.text.lower()):
                misconfigurations.append({
                    'name': 'Configuration File Exposure',
                    'severity': 'Critical',
                    'description': f'Configuration file with potential secrets is exposed at {file_url}',
                    'recommendation': 'Remove or restrict access to configuration files'
                })
    
    # Check for default credentials
    default_login_paths = [
        'wp-login.php',  # WordPress
        'administrator',  # Joomla
        'admin',  # Generic
        'login',  # Generic
        'user/login',  # Drupal
        'panel',  # Generic
        'cpanel',  # cPanel
        'phpmyadmin',  # phpMyAdmin
    ]
    
    for path in default_login_paths:
        login_url = urllib.parse.urljoin(url, path)
        response = make_request(login_url)
        
        if response and response.status_code == 200 and ('login' in response.text.lower() or 'password' in response.text.lower()):
            misconfigurations.append({
                'name': 'Default Login Page Accessible',
                'severity': 'Medium',
                'description': f'Default login page is accessible at {login_url}',
                'recommendation': 'Consider restricting access to admin pages or changing their URL'
            })
    
    return misconfigurations

# Save results to file
def save_results(target, results, output_dir="reports"):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create filename based on target and timestamp
    base_domain = get_base_domain(target)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}/{base_domain}_{timestamp}.json"
    
    # Save results to file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, default=str)
    
    print(f"\n{Fore.GREEN}[+] Results saved to {filename}")
    return filename

# Print summary of results
def print_summary(results):
    print(f"\n{Fore.YELLOW}{'=' * 60}")
    print(f"{Fore.YELLOW}[+] SCAN SUMMARY")
    print(f"{Fore.YELLOW}{'=' * 60}")
    
    # Target information
    print(f"{Fore.CYAN}[*] Target: {results['target']}")
    print(f"{Fore.CYAN}[*] Scan Date: {results['scan_date']}")
    
    # Metadata
    if results['metadata']['title']:
        print(f"{Fore.CYAN}[*] Site Title: {results['metadata']['title']}")
    
    # Technologies
    if results['metadata']['technologies']:
        print(f"{Fore.CYAN}[*] Detected Technologies: {', '.join(results['metadata']['technologies'])}")
    
    # Links
    print(f"{Fore.CYAN}[*] Internal Links: {len(results['links']['internal'])}")
    print(f"{Fore.CYAN}[*] External Links: {len(results['links']['external'])}")
    print(f"{Fore.CYAN}[*] Resource Links: {len(results['links']['resources'])}")
    
    # Vulnerabilities
    if results['vulnerabilities']:
        print(f"\n{Fore.RED}[!] Vulnerabilities Found: {len(results['vulnerabilities'])}")
        for i, vuln in enumerate(results['vulnerabilities'], 1):
            severity_color = Fore.YELLOW
            if vuln['severity'] == 'Critical':
                severity_color = Fore.RED + Style.BRIGHT
            elif vuln['severity'] == 'High':
                severity_color = Fore.RED
            elif vuln['severity'] == 'Medium':
                severity_color = Fore.YELLOW
            elif vuln['severity'] == 'Low':
                severity_color = Fore.GREEN
                
            print(f"  {i}. {vuln['name']} - {severity_color}{vuln['severity']}")
    else:
        print(f"\n{Fore.GREEN}[+] No vulnerabilities found")
    
    # Misconfigurations
    if results['misconfigurations']:
        print(f"\n{Fore.RED}[!] Misconfigurations Found: {len(results['misconfigurations'])}")
        for i, misconf in enumerate(results['misconfigurations'], 1):
            severity_color = Fore.YELLOW
            if misconf['severity'] == 'Critical':
                severity_color = Fore.RED + Style.BRIGHT
            elif misconf['severity'] == 'High':
                severity_color = Fore.RED
            elif misconf['severity'] == 'Medium':
                severity_color = Fore.YELLOW
            elif misconf['severity'] == 'Low':
                severity_color = Fore.GREEN
                
            print(f"  {i}. {misconf['name']} - {severity_color}{misconf['severity']}")
    else:
        print(f"\n{Fore.GREEN}[+] No misconfigurations found")
    
    print(f"\n{Fore.YELLOW}{'=' * 60}")

# Main function
def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Site Analyzer Tool - Comprehensive website analysis and vulnerability scanner')
    parser.add_argument('-t', '--target', required=True, help='Target URL or domain')
    parser.add_argument('-o', '--output', default='reports', help='Output directory for reports (default: reports)')
    parser.add_argument('-d', '--depth', type=int, default=1, help='Crawling depth (default: 1)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds (default: 10)')
    parser.add_argument('--threads', type=int, default=5, help='Number of threads for concurrent operations (default: 5)')
    
    args = parser.parse_args()
    
    # Disable colored output if requested
    if args.no_color:
        init(autoreset=True, strip=True)
    
    # Print banner
    print_banner()
    
    # Normalize target URL
    target = normalize_url(args.target)
    base_domain = get_base_domain(target)
    
    print(f"{Fore.GREEN}[+] Starting scan of {target}")
    print(f"{Fore.GREEN}[+] Base domain: {base_domain}")
    
    # Initialize results dictionary
    results = {
        'target': target,
        'base_domain': base_domain,
        'scan_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'metadata': {},
        'whois': {},
        'dns': {},
        'security_headers': {},
        'links': {
            'internal': [],
            'external': [],
            'resources': []
        },
        'vulnerabilities': [],
        'misconfigurations': []
    }
    
    try:
        # Extract metadata
        results['metadata'] = extract_metadata(target)
        
        # Get WHOIS information
        results['whois'] = get_whois_info(base_domain)
        
        # Perform DNS enumeration
        results['dns'] = dns_enumeration(base_domain)
        
        # Check security headers
        results['security_headers'] = check_security_headers(target)
        
        # Extract links
        internal_links, external_links, resource_links = extract_links(target, base_domain)
        results['links']['internal'] = list(internal_links)
        results['links']['external'] = list(external_links)
        results['links']['resources'] = list(resource_links)
        
        # Crawl internal links up to specified depth
        if args.depth > 1 and internal_links:
            print(f"\n{Fore.CYAN}[*] Crawling internal links (depth: {args.depth})...")
            crawled_urls = {target}
            urls_to_crawl = list(internal_links)
            
            with tqdm(total=len(urls_to_crawl), desc="Crawling", unit="url") as pbar:
                for current_depth in range(1, args.depth):
                    if not urls_to_crawl:
                        break
                        
                    new_urls = []
                    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
                        future_to_url = {executor.submit(extract_links, url, base_domain): url for url in urls_to_crawl if url not in crawled_urls}
                        
                        for future in concurrent.futures.as_completed(future_to_url):
                            url = future_to_url[future]
                            crawled_urls.add(url)
                            pbar.update(1)
                            
                            try:
                                int_links, ext_links, res_links = future.result()
                                
                                # Add new links to results
                                for link in int_links:
                                    if link not in results['links']['internal']:
                                        results['links']['internal'].append(link)
                                        if link not in crawled_urls:
                                            new_urls.append(link)
                                            
                                for link in ext_links:
                                    if link not in results['links']['external']:
                                        results['links']['external'].append(link)
                                        
                                for link in res_links:
                                    if link not in results['links']['resources']:
                                        results['links']['resources'].append(link)
                                        
                            except Exception as e:
                                if args.verbose:
                                    print(f"{Fore.RED}[!] Error crawling {url}: {str(e)}")
                    
                    urls_to_crawl = new_urls
                    if args.verbose:
                        print(f"{Fore.CYAN}[*] Depth {current_depth} completed. Found {len(new_urls)} new URLs to crawl.")
        
        # Check for vulnerabilities
        results['vulnerabilities'] = check_vulnerabilities(target, results['metadata'], results['security_headers'])
        
        # Check for misconfigurations
        results['misconfigurations'] = check_misconfigurations(target)
        
        # Save results to file
        output_file = save_results(target, results, args.output)
        
        # Print summary
        print_summary(results)
        
        print(f"\n{Fore.GREEN}[+] Scan completed successfully. Full report saved to {output_file}")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan interrupted by user")
        # Save partial results
        output_file = save_results(target, results, args.output)
        print(f"{Fore.YELLOW}[!] Partial results saved to {output_file}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] An error occurred during the scan: {str(e)}")
        if args.verbose:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    # Disable SSL warnings
    try:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    except ImportError:
        pass
    
    main()