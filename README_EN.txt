# Website Analysis and Security Testing Tools

Developed by: Saudi Crackers
Email: SaudiLinux7@gmail.com

## Contents
1. About the Tools
2. System Requirements
3. Installation
4. How to Use Site Analyzer
5. How to Use Vulnerability Exploiter
6. Typical Workflow
7. Security Notes

## 1. About the Tools

### Site Analyzer
A powerful tool written in Python that crawls target websites and performs comprehensive analysis. The tool extracts metadata, website files, links, and discovers potential security vulnerabilities.

### Vulnerability Exploiter
An advanced tool written in Python that tests and exploits security vulnerabilities discovered in target websites. This tool is designed to complement the Site Analyzer and provides practical methods for testing vulnerabilities and generating proof of concept (PoC).

## 2. System Requirements

- Python 3.6 or newer
- The following libraries:
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

## 3. Installation

1. Download or clone the project:

```
git clone https://github.com/SaudiCrackers/site-analyzer.git
cd site-analyzer
```

2. Install the requirements:

```
pip install -r requirements.txt
```

3. Alternative installation using setup.py:

```
python setup.py install
```

## 4. How to Use Site Analyzer

### Basic Commands

```
python site_analyzer.py -t example.com
```

### Advanced Options

```
python site_analyzer.py -t example.com -o custom_reports -d 2 -v --threads 10
```

### Available Options

- `-t, --target`: Target URL or domain name (required)
- `-o, --output`: Output folder for reports (default: reports)
- `-d, --depth`: Crawl depth (default: 1)
- `-v, --verbose`: Enable verbose output
- `--no-color`: Disable colored output
- `--timeout`: Request timeout in seconds (default: 10)
- `--threads`: Number of threads for concurrent operations (default: 5)

### Examples

#### Simple Website Scan
```
python site_analyzer.py -t example.com
```

#### Deep Crawl Website Scan
```
python site_analyzer.py -t example.com -d 3 --threads 10
```

#### Save Report to Custom Folder
```
python site_analyzer.py -t example.com -o my_reports
```

## 5. How to Use Vulnerability Exploiter

### Basic Commands

```
python vulnerability_exploiter.py -t example.com --all
```

### Using Site Analysis Results

```
python vulnerability_exploiter.py -t example.com -i reports/example.com_20230101_120000.json --all
```

### Available Options

- `-t, --target`: Target URL or domain name (required)
- `-i, --input`: Input file with vulnerabilities (from site_analyzer)
- `-o, --output`: Output file for exploitation results
- `--xss`: Test XSS vulnerabilities
- `--sqli`: Test SQL Injection vulnerabilities
- `--csrf`: Test CSRF vulnerabilities
- `--lfi`: Test LFI/RFI vulnerabilities
- `--cmdi`: Test Command Injection vulnerabilities
- `--all`: Test all vulnerabilities
- `--cookies`: Cookies to use (format: name1=value1; name2=value2)
- `--proxy`: Proxy to use (format: http://127.0.0.1:8080)
- `--timeout`: Request timeout in seconds (default: 10)
- `--no-color`: Disable colored output
- `--verbose`: Enable verbose output

### Examples

#### Test All Vulnerabilities
```
python vulnerability_exploiter.py -t example.com --all
```

#### Test XSS Vulnerabilities Only
```
python vulnerability_exploiter.py -t example.com --xss
```

#### Use Proxy and Test SQL Injection Vulnerabilities
```
python vulnerability_exploiter.py -t example.com --sqli --proxy http://127.0.0.1:8080
```

## 6. Typical Workflow

1. First, analyze the target website using the Site Analyzer:

```
python site_analyzer.py -t example.com -o reports
```

2. Use the analysis results as input for the Vulnerability Exploiter:

```
python vulnerability_exploiter.py -t example.com -i reports/example.com_20230101_120000.json --all
```

3. Review the result reports for detailed information about discovered vulnerabilities and exploitation methods.

## 7. Security Notes

- Use these tools only on websites that you have legal permission to scan
- Using these tools on websites without permission may violate local laws
- The developer is not responsible for any illegal use of these tools
- Some exploitation methods may cause damage to target systems, use them with caution

## License

This project is licensed under the MIT License. See the LICENSE file for details.