
# ZAP Scanning Report




## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 1 |
| Medium | 1 |
| Low | 2 |
| Informational | 1 |

## Alert Detail


  
  
  
### SQL Injection
##### High (Medium)
  
  
  
  
#### Description
<p>SQL injection may be possible.</p>
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `submit`
  
  
  * Attack: `Sign Up' OR '1'='1' -- `
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `csrf_token`
  
  
  * Attack: `IjVhYzkxZDQyZGNlY2FmZDc0ZmE5ODk4NDMwYTVmZjhkMWE3NWQ3Mjki.XebAyA.TALe4QOxOflnGA-pE-b4MwRwU6c' AND '1'='1' -- `
  
  
  
  
Instances: 2
  
### Solution
<p>Do not trust client side input, even if there is client side validation in place.  </p><p>In general, type check all data on the server side.</p><p>If the application uses JDBC, use PreparedStatement or CallableStatement, with parameters passed by '?'</p><p>If the application uses ASP, use ADO Command Objects with strong type checking and parameterized queries.</p><p>If database Stored Procedures can be used, use them.</p><p>Do *not* concatenate strings into queries in the stored procedure, or use 'exec', 'exec immediate', or equivalent functionality!</p><p>Do not create dynamic SQL queries using simple string concatenation.</p><p>Escape all data received from the client.</p><p>Apply a 'whitelist' of allowed characters, or a 'blacklist' of disallowed characters in user input.</p><p>Apply the principle of least privilege by using the least privileged database user possible.</p><p>In particular, avoid using the 'sa' or 'db-owner' database users. This does not eliminate SQL injection, but minimizes its impact.</p><p>Grant the minimum database access that is necessary for the application.</p>
  
### Other information
<p>The page results were successfully manipulated using the boolean conditions [Sign Up' AND '1'='1' -- ] and [Sign Up' OR '1'='1' -- ]</p><p>The parameter value being modified was NOT stripped from the HTML output for the purposes of the comparison</p><p>Data was NOT returned for the original parameter.</p><p>The vulnerability was detected by successfully retrieving more data than originally returned, by manipulating the parameter</p>
  
### Reference
* https://www.owasp.org/index.php/Top_10_2010-A1
* https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet

  
#### CWE Id : 89
  
#### WASC Id : 19
  
#### Source ID : 1

  
  
  
### X-Frame-Options Header Not Set
##### Medium (Medium)
  
  
  
  
#### Description
<p>X-Frame-Options header is not included in the HTTP response to protect against 'ClickJacking' attacks.</p>
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://localhost:5000/home](http://localhost:5000/home)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://localhost:5000](http://localhost:5000)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://localhost:5000/](http://localhost:5000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
* URL: [http://localhost:5000/about](http://localhost:5000/about)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Frame-Options`
  
  
  
  
Instances: 8
  
### Solution
<p>Most modern Web browsers support the X-Frame-Options HTTP header. Ensure it's set on all web pages returned by your site (if you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. ALLOW-FROM allows specific websites to frame the web page in supported web browsers).</p>
  
### Reference
* http://blogs.msdn.com/b/ieinternals/archive/2010/03/30/combating-clickjacking-with-x-frame-options.aspx

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Web Browser XSS Protection Not Enabled
##### Low (Medium)
  
  
  
  
#### Description
<p>Web Browser XSS Protection is not enabled, or is disabled by the configuration of the 'X-XSS-Protection' HTTP response header on the web server</p>
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/robots.txt](http://localhost:5000/robots.txt)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000](http://localhost:5000)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/](http://localhost:5000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/about](http://localhost:5000/about)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/sitemap.xml](http://localhost:5000/sitemap.xml)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/static](http://localhost:5000/static)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
* URL: [http://localhost:5000/home](http://localhost:5000/home)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-XSS-Protection`
  
  
  
  
Instances: 11
  
### Solution
<p>Ensure that the web browser's XSS filter is enabled, by setting the X-XSS-Protection HTTP response header to '1'.</p>
  
### Other information
<p>The X-XSS-Protection HTTP response header allows the web server to enable or disable the web browser's XSS protection mechanism. The following values would attempt to enable it: </p><p>X-XSS-Protection: 1; mode=block</p><p>X-XSS-Protection: 1; report=http://www.example.com/xss</p><p>The following values would disable it:</p><p>X-XSS-Protection: 0</p><p>The X-XSS-Protection HTTP response header is currently supported on Internet Explorer, Chrome and Safari (WebKit).</p><p>Note that this alert is only raised if the response body could potentially contain an XSS payload (with a text-based content type, with a non-zero length).</p>
  
### Reference
* https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet
* https://www.veracode.com/blog/2014/03/guidelines-for-setting-security-headers/

  
#### CWE Id : 933
  
#### WASC Id : 14
  
#### Source ID : 3

  
  
  
### X-Content-Type-Options Header Missing
##### Low (Medium)
  
  
  
  
#### Description
<p>The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.</p>
  
  
  
* URL: [http://localhost:5000/](http://localhost:5000/)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000](http://localhost:5000)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000/home](http://localhost:5000/home)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000/static/main.css](http://localhost:5000/static/main.css)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000/about](http://localhost:5000/about)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `POST`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `GET`
  
  
  * Parameter: `X-Content-Type-Options`
  
  
  
  
Instances: 9
  
### Solution
<p>Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.</p><p>If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.</p>
  
### Other information
<p>This issue still applies to error type pages (401, 403, 500, etc) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.</p><p>At "High" threshold this scanner will not alert on client or server error responses.</p>
  
### Reference
* http://msdn.microsoft.com/en-us/library/ie/gg622941%28v=vs.85%29.aspx
* https://www.owasp.org/index.php/List_of_useful_HTTP_headers

  
#### CWE Id : 16
  
#### WASC Id : 15
  
#### Source ID : 3

  
  
  
### Loosely Scoped Cookie
##### Informational (Low)
  
  
  
  
#### Description
<p>Cookies can be scoped by domain or path. This check is only concerned with domain scope.The domain scope applied to a cookie determines which domains can access it. For example, a cookie can be scoped strictly to a subdomain e.g. www.nottrusted.com, or loosely scoped to a parent domain e.g. nottrusted.com. In the latter case, any subdomain of nottrusted.com can access the cookie. Loosely scoped cookies are common in mega-applications like google.com and live.com. Cookies set from a subdomain like app.foo.bar are transmitted only to that domain by the browser. However, cookies scoped to a parent-level domain may be transmitted to the parent, or any subdomain of the parent.</p>
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `POST`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `GET`
  
  
  
  
* URL: [http://localhost:5000/](http://localhost:5000/)
  
  
  * Method: `GET`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `GET`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `GET`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `POST`
  
  
  
  
* URL: [http://localhost:5000/register](http://localhost:5000/register)
  
  
  * Method: `GET`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `POST`
  
  
  
  
* URL: [http://localhost:5000/login](http://localhost:5000/login)
  
  
  * Method: `POST`
  
  
  
  
Instances: 9
  
### Solution
<p>Always scope cookies to a FQDN (Fully Qualified Domain Name).</p>
  
### Other information
<p>The origin domain used for comparison was: </p><p>localhost</p><p>session=eyJfZnJlc2giOmZhbHNlLCJjc3JmX3Rva2VuIjoiYjUzZDBkM2E1OWYzYTc4N2NhNmU0Zjg2ZWY5OWRmYzk3ZDFkNGY5MyJ9.XebMmg.SHka_nXmXsb2UOjBWUsB14-9xGQ</p><p></p>
  
### Reference
* https://tools.ietf.org/html/rfc6265#section-4.1
* https://www.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002)
* http://code.google.com/p/browsersec/wiki/Part2#Same-origin_policy_for_cookies

  
#### CWE Id : 565
  
#### WASC Id : 15
  
#### Source ID : 3
