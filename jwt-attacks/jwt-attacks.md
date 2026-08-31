# Jwt Attacks - Walkthroughs

```mermaid
graph TD
    Root["Jwt Attacks"]
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
```

## Lab 01: JWT authentication bypass via unverified signature
<a id="lab-01"></a>

## Vulnerability
JWT

## Goal
modify the session token to gain access to the /admin panel and delete the user carlos

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
- Check if the JWT signature is verified

---

## Lab 02: JWT authentication bypass via flawed signature verification
<a id="lab-02"></a>

## Vulnerability
JWT

## Goal
modify the session token to gain access to the /admin panel and delete the user carlos

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
1) Check if the JWT signature is verified.
2) Check if the application accepts an unsigned JWT / none algorithm

---

## Lab 03: JWT authentication bypass via weak signing key
<a id="lab-03"></a>

## Vulnerability
JWT

## Goal
Brute-force the website's secret key, use it to craft an administrator JWT and delete the user carlos.

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
1) Check if the JWT signature is verified.
2) Check if the application accepts an unsigned JWT / none algorithm
3) Check for weak signing key / brute forcable secret key (symmetric)

---

## Lab 04: JWT authentication bypass via jwk header injection
<a id="lab-04"></a>

## Vulnerability
JWT

## Goal
modify and sign the JWT and delete the user carlos

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
1) Check if the JWT signature is verified.
2) Check if the application accepts an unsigned JWT / none algorithm
3) Check for weak signing key / brute-force secret key (symmetric)
4) Check if the application accepts an arbitrary injected jwk header / jwk injection (public-key)

---

## Lab 05: JWT authentication bypass via jku header injection
<a id="lab-05"></a>

## Vulnerability
JWT

## Goal
Forge a JWT by adding the jku parameter and delete the user carlos

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
1) Check if the JWT signature is verified.
2) Check if the application accepts an unsigned JWT / none algorithm
3) Check for weak signing key / brute-force secret key
4) Check if the application accepts an arbitrary injected jwk parameter
5) Check if the application accepts an arbitrary jku parameter


- Generate our RSA key
- Add the public key in the exploit server
- Modify the JWT to include the jku parameter and the subject administrator
- sign the jwt using the private key 

---

## Lab 06: JWT authentication bypass via kid header path traversal
<a id="lab-06"></a>

## Vulnerability
JWT

## Goal
modify and sign the JWT and delete the user carlos

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
1) Check if the JWT signature is verified.
2) Check if the application accepts an unsigned JWT / none algorithm
3) Check for weak signing key / brute-force secret key
4) Check if the application accepts an arbitrary injected jwk header
5) Check if the application accepts an arbitrary jku header
6) Check if the kid parameter is vulnerable to path traversal.


/dev/null

---

## Lab 07: JWT authentication bypass via algorithm confusion
<a id="lab-07"></a>

## Vulnerability
JWT

## Goal
modify and sign the JWT and delete the user carlos

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
1) Check if the JWT signature is verified.
2) Check if the application accepts an unsigned JWT / none algorithm
3) Check for weak signing key / brute-force secret key
4) Check if the application accepts an arbitrary injected jwk header
5) Check if the application accepts an arbitrary jku header
6) Check if the kid parameter is vulnerable to path traversal.
7) Check if the application is vulnerable to algorithm confusion.

1. Symmetric algorithms - one key is used to both sign and verify the signature of the token.

2. Asymmetric algorithms - 2 keys.
  - one is used to sign the token (private key)
  - another key that is used to verify the token (public key)

---

## Lab 08: JWT authentication bypass via algorithm confusion with no exposed key
<a id="lab-08"></a>

## Vulnerability
JWT

## Goal
modify and sign the JWT and delete the user carlos

## Credentials
`wiener:peter`

## Analysis

Testing for JWT vulnerabilities:
1) Check if the JWT signature is verified.
2) Check if the application accepts an unsigned JWT / none algorithm
3) Check for weak signing key / brute-force secret key
4) Check if the application accepts an arbitrary injected jwk header
5) Check if the application accepts an arbitrary jku header
6) Check if the kid parameter is vulnerable to path traversal.
7) Check if the application is vulnerable to algorithm confusion.

1 - Symmetric algorithm - one key
2 - Asymmetric algorithms - 2 keys
    - sign token / private key
    - verify token / public key

---

