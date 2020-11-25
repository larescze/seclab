<h1>BPC-AKR: Web security vulnerabilities</h1>

<p>A website for searching web servers with a type of vulnerability and exploits for testing these vulnerabilities.</p>
<p>Maine goal of this project is vulnerability visualization for Apache servers to specific exploits.</p>
<h2>Project structure</h2>
<ul>
<li>app - web app backend
<ul>
<li>exploits - all exploit scripts</li>
<li>migrations - django migration system</li>
</ul>
</li>
<li>seclab - web app settings</li>
<li>static - web app frontend
<ul>
<li>assets - css, images, javascript</li>
<li>templates - view templates</li>
</ul>
</li>
</ul>

<h2>Shodan</h2>
<p>Shodan is search engine for Internet-connected devices (webcams, routers, servers, etc.). Shodan provides banners which are information about device (IP address, software, version, server, serial number, location, vulnerabilities, etc.) through the REST API.</p>
<h4>REST API</h4>
<p>The REST API provides methods to search Shodan, look up hosts, get summary information on queries, get information about number of results, narrow search results by filters, search for devices with default passwords, look up devices vulnerable to certain exploits or get port numbers that the crawlers are looking for.</p>
<h2>Exploits</h2>
<h3>Directory Traversal</h3>
<p>Directory traversal is a type of HTTP exploit that allows attackers to gain unauthorized access to restricted directories and files outside of root directory. An attacker may manipulate a URL with special characters “../” to bypass security filters.</p>
<h3>DoS</h3>
<p>Denial of service (DoS) is an attack targeting the availability of web applications. Rather than to steal information the goal of a DoS attack is to slow down or take down a website. A DoS attack exhaust computing resources of a target by generating high or slow rate traffic. Constant flooding of targeted network with traffic prevents legitimate users from accessing the website. </p>
<p>This attack floods the HTTP or HTTPS ports with get requests or floods the website forms with random data. </p>
<h3>SQL Injection</h3>
<p>SQL injection is code injection attack, in which part of SQL statement is inserted into an entry field in an application connected to database. If application is vulnerable to this exploit the SQL statement is executed. SQL statement can allow access to sensitive data form the database, modify the database data or delete the whole table.</p>
<p>This SQL injection enters short string into a login form and if statement is executed, attacker gets logged in as first user in database table.</p>
<h3>XSS</h3>
<p>Cross-Site Scripting is code injection attack, in which malicious code (usually JavaScript) is inserted into source code of a website by user input. The attack occurs when the victim opens the website which executes the malicious code. A website is vulnerable to XSS attack if it uses unsanitized user input in the output that it generates e.g comment fields.</p>
<p>This attack uses JavaScript code which is inserted into website forms coded in HTML language.</p>
