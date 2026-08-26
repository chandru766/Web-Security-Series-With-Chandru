# Directory Traversal - Walkthroughs

```mermaid
graph TD
    Root["Directory Traversal"]
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
```

## Lab 01: File path traversal, simple case
<a id="lab-01"></a>

Target Goal - Retrieve the contents of the /etc/passwd file.

## Analysis

/var/www/images/65.jpg

/etc/passwd

---

## Lab 02: File path traversal, traversal sequences blocked with absolute path bypass
<a id="lab-02"></a>

Target Goal - Retrieve the contents of the /etc/passwd file.

## Analysis


---

## Lab 03: File path traversal, traversal sequences stripped non-recursively
<a id="lab-03"></a>

Target Goal - Retrieve the contents of the /etc/passwd file.

## Analysis

/etc/passwd
../../../../etc/passwd
....//....//....//....//etc/passwd

../

---

## Lab 04: File path traversal, traversal sequences stripped with superfluous URL-decode
<a id="lab-04"></a>

Target Goal - Retrieve the contents of the /etc/passwd file.

## Analysis

../

---

## Lab 05: File path traversal, validation of start of path
<a id="lab-05"></a>

Target Goal - Retrieve the contents of the /etc/passwd file.

## Analysis

/var/www/images/67.jpg

---

## Lab 06: File path traversal, validation of file extension with null byte bypass
<a id="lab-06"></a>

Target Goal - Retrieve the contents of the /etc/passwd file.

## Analysis


---

