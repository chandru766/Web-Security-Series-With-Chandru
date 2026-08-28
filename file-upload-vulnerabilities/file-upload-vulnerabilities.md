# File Upload Vulnerabilities - Walkthroughs

```mermaid
graph TD
    Root["File Upload Vulnerabilities"]
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

## Lab 01: Remote code execution via web shell upload
<a id="lab-01"></a>

Target Goal - Exploit the file upload vulnerability to exfiltrate the contents of the file /home/carlos/secret

Creds - wiener:peter

## Analysis

---

## Lab 02: Web shell upload via Content-Type restriction bypass
<a id="lab-02"></a>

Target Goal - Exploit the file upload vulnerability to exfiltrate the contents of the file /home/carlos/secret

Creds - wiener:peter

## Analysis


---

## Lab 03: Web shell upload via path traversal
<a id="lab-03"></a>

Target Goal - Exploit file upload vulnerability to upload a PHP web shell and exfiltrate the contents of the /home/carlos/secret

Creds - wiener:peter


## Analysis


---

## Lab 04: Web shell upload via extension blacklist bypass
<a id="lab-04"></a>

Target Goal - Bypass blacklist defense and upload a PHP web shell to exfitrate the contents of the file /home/carlos/secret

Creds - wiener:peter

## Analysis



---

## Lab 05: Web shell upload via obfuscated file extension
<a id="lab-05"></a>

Target Goal - Exploit a file upload vulnerability to upload a web shell and exfiltrate the contents of the file /home/carlos/secret

Creds - wiener:peter

## Analysis





---

## Lab 06: Remote code execution via polyglot web shell upload
<a id="lab-06"></a>

Target Goal - Exploit file upload vulnerability to exfiltrate the contents of the /home/carlos/secret

Creds - wiener:peter

## Analysis


---

## Lab 07: Web shell upload via race condition
<a id="lab-07"></a>

Target Goal - Exploit file upload vulnerability to exfiltrate the contents of the /home/carlos/secret

Creds - wiener:peter

## Analysis

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=10,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    request1 = '''
<add post request here>
'''

    
    request2 = '''
<add get request here>
\r\n
'''

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    engine.queue(request1, gate='race1')
    for i in range(9):
        engine.queue(request2, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)


---

