# Broken Access Control - Walkthroughs

```mermaid
graph TD
    Root["Broken Access Control"]
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
    Root --> L12["Lab 13"]
    click L12 href "#lab-13"
```

## Lab 01: Unprotected admin function
<a id="lab-01"></a>

Target Goal - Find the admin panel and delete the user carlos

## Analysis


---

## Lab 02: Unprotected admin functionality with unpredictable URL
<a id="lab-02"></a>

Target Goal - Find the admin panel and delete the user carlos.

## Analysis


---

## Lab 03: User role controlled by request parameter
<a id="lab-03"></a>

Target Goal - Access admin panel and use it to delete the user carlos.

creds: wiener:peter

## Analysis


---

## Lab 04: User role can be modified in user profile
<a id="lab-04"></a>

Target Goal - Access admin panel and use it to delete the user carlos.

creds: wiener:peter

Steps to script:
1. Login as the wiener user
2. Change the role id of the user to 2
3. Access the admin panel and delete the user

---

## Lab 05: URL-based access control can be circumvented
<a id="lab-05"></a>

Target Goal - Access the admin panel and delete the Carlos user


---

## Lab 06: Method-based access control can be circumvented
<a id="lab-06"></a>

Target Goal - Promote user to become administrator

creds: administrator:admin, wiener:peter

Steps to exploit:


---

## Lab 07: User ID controlled by request parameter
<a id="lab-07"></a>

Target Goal - Obtain API key for the user carlos and submit it as a olution

creds: wiener:peter

Steps to exploit:

---

## Lab 08: User ID controlled by request parameter, with unpredictable user IDs
<a id="lab-08"></a>

Target Goal - Find the GUID for carlos and compromise his account

creds: wiener:peter

Steps to exploit:

1. Log into the wiener account
2. Loop through all the posts and identify which one is written by the carlos user
3. Extract the GUID
4. Access the Carlos user account
5. Extract the API key of Carlos.

---

## Lab 09: User ID controlled by request parameter with data leakage in redirect
<a id="lab-09"></a>

Target Goal - Obtain the API key for the carlos user.

creds: wiener:peter

Steps to exploit:

---

## Lab 10: User ID controlled by request parameter with password disclosure
<a id="lab-10"></a>

Target Goal - Retrieve the administrator's password and delete the user carlos.

creds: wiener:peter

Steps to exploit:

1. Log into the wiener account
2. Exploit access control vulnerability to obtain the administrator's password
3. Login as the administrator user
4. Delete the carlos user


---

## Lab 11: Insecure direct object references
<a id="lab-11"></a>

Target Goal - Find the Carlos user password and log into his account.


Steps to exploit:


---

## Lab 12: Multi-step process with no access control on one step
<a id="lab-12"></a>

Target Goal - Exploit the access control flaw to promote the wiener user to administrator

creds: administrator:admin, wiener:peter

Steps to exploit:

---

## Lab 13: Referer-based access control
<a id="lab-13"></a>

Target Goal - Promote the wiener user to administrator

creds: adminstrator:admin, wiener:peter

Steps to exploit:

---

