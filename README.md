<h1>VUT BPC-AKR Project: Seclab (Security Laboratory)</h1>
<p>Seclab is a website application for searching devices on the internet with vulnerability summarization and exploits demonstration.</p>
<p>Main goal of this project is vulnerability visualization, especially for Apache servers and demonstration of some specific exploits.</p>

<h2>Project structure</h2>
<pre>
bpc-akr-python
├── app                     # Web app backend
│   ├── exploits            # Exploit files (dos, ddtrav, sqli, vulnscan, xss)
│   └── migrations          # Migration system 
├── seclab                  # Web app settings and routing
├── static                  # Web app frontend
│   ├── assets              # CSS, JavaScript, images
│   └── templates           # View templates
├── README.md               # Readme file
├── __init__.py             # Python convention (package)
├── db.sqlite3              # Local database
├── manage.py               # Command-line utility for administrative tasks
└── requirements.txt        # File with all dependencies
</pre>

<h2>Dependencies</h2>
<ul>
<li>bs4</li>
<li>dj-database-url</li>
<li>Django</li>
<li>requests</li>
<li>shodan</li>
<li>urllib3</li>
</ul>

<h2>Installation</h2>
<p>1. Clone repository:</p>
<pre>git clone https://github.com/larescze/bpc-akr-python.git</pre>
<p>2. Install all required libraries from root directory:</p>
<pre>pip install -r requirements.txt</pre>
<p>3. Fill Shodan REST API key into constant API_KEY in <a href="app/exploits/vulnscan.py">./app/exploits/vulnscan.py)</a>:</p>
<pre>
# Shodan Rest API key
API_KEY = ""
</pre>
<p>4. Run development server:</p>
<pre>python manage.py runserver</pre>
<p>5. Server should be running on http://127.0.0.1:8000/.</p>

<h2>How to use</h2>
<h3>Searching</h3>
<p>1. Enter some keyword. For example <code>apache</code>.</p>
<p>2. Select summary filters, chart and results display limit (optional).</p>
<p>3. Click on <code>🔍</code> or press ENTER.</p>
<p>4. Explore search results, TOP 5 charts.</p>
<p>Note: If vulnerabilities summary was selected, you can visit TOP 5 CVEs details on <a href="https://nvd.nist.gov/">NIST</a> (National Institute of Standards and Technology). By clicking on the host IP, you will be redirected to <a href="https://www.shodan.io/">shodan.io</a> for more details.</p>

<h3>Exploits</h3>
<p>1. Login to access <em>Exploits</em> page:</p>
<ul>
<li>Username: <strong>xguest20</strong></li>
<li>Password: <strong>bpc-akr-2020</strong></li>
</ul>
<p>2. Move to <em>Exploits</em> page.</p>
<p>3. Select exploit, read description and fill out input fiels.</p>
<p>Note: We recommend to use live website demo from this <a href="https://github.com/larescze/bpc-akr-web">repository</a>:</p>
<p>
Apache version 2.2.34 (vulnerable): <code>http://apache1.willilazarov.cz</code>.<br>
Apache version 2.4.43 (vulnerable): <code>http://apache2.willilazarov.cz</code>.<br>
Apache version 2.4.43 (secure): <code>https://apache3.willilazarov.cz</code>.
</p>
<p>4. Launch attack and wait for results.</p>
<p><strong>:warning: WARNING: Use all exploits only for educational purposes!</strong></p>

<h2>About searching and exploits</h2>

<h3>Shodan</h3>
<p>Shodan is search engine for Internet-connected devices (webcams, routers, servers, etc.). Shodan provides banners which are information about device (IP address, software, version, server, serial number, location, vulnerabilities, etc.) through the REST API.</p>
<h4>REST API</h4>
<p>The REST API provides methods to search Shodan, look up hosts, get summary information on queries, get information about number of results, narrow search results by filters, search for devices with default passwords, look up devices vulnerable to certain exploits or get port numbers that the crawlers are looking for.</p>
<h3>Exploits</h3>

<h4>Directory Traversal</h4>
<p>Directory traversal is a type of HTTP exploit that allows attackers to gain unauthorized access to restricted directories and files outside of root directory. An attacker may manipulate a URL with special characters “../” to bypass security filters.</p>

<h4>DoS</h4>
<p>Denial of service (DoS) is an attack targeting the availability of web applications. Rather than to steal information the goal of a DoS attack is to slow down or take down a website. A DoS attack exhaust computing resources of a target by generating high or slow rate traffic. Constant flooding of targeted network with traffic prevents legitimate users from accessing the website. </p>
<p>This attack floods the HTTP or HTTPS ports with get requests or floods the website forms with random data. </p>

<h4>SQL Injection</h4>
<p>SQL injection is code injection attack, in which part of SQL statement is inserted into an entry field in an application connected to database. If application is vulnerable to this exploit the SQL statement is executed. SQL statement can allow access to sensitive data form the database, modify the database data or delete the whole table.</p>
<p>This SQL injection enters short string into a login form and if statement is executed, attacker gets logged in as first user in database table.</p>

<h4>XSS</h4>
<p>Cross-Site Scripting is code injection attack, in which malicious code (usually JavaScript) is inserted into source code of a website by user input. The attack occurs when the victim opens the website which executes the malicious code. A website is vulnerable to XSS attack if it uses unsanitized user input in the output that it generates e.g comment fields.</p>
<p>This attack uses JavaScript code which is inserted into website forms coded in HTML language.</p>
