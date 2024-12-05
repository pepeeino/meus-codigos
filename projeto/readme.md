## Dork Tester

To use the Dork Tester, you will need an API key, which can be obtained from either Google or Bing. You can choose the one that fits your needs.

---

### Scripts in `requisição.js`

**choose which one you would use best**

#### 1. `validate_site()`

- **Purpose**: Checks if a website is accessible and attempts to detect Cloudflare cookies.
- **How it works**:
  - Sends a `GET` request to the provided URL.
  - Checks for a `200 OK` response status.
  - Searches for cookies containing "cf" (indicating Cloudflare protection).
  - Displays the response status and whether Cloudflare cookies were found.

#### 2. `ping_site()`

- **Purpose**: Performs a lightweight "ping" check to see if a website is responding.
- **How it works**:
  - Sends a `HEAD` request to the site.
  - Checks if the response status is between `200` and `299` (indicating success).
  - Displays the response status.

---

### Differences:

- **`validate_site()`**: More comprehensive — checks both cookies and website availability.
- **`ping_site()`**: Simpler and faster — checks only if the site is available without downloading full content.

---

### CORS Handling

If you plan to use the Cloudflare cookie finder (`validate_site()`), you will need a **server** to bypass CORS restrictions. This is because browser-based requests may not allow cross-origin access to certain resources due to security policies.

---

### XSS-TESTER

xss-tester needs a lot of adjustments, mainly because I try to use js and python together, and as I don't know Python very well I used an AI for the codes, this could have caused a lot of confusion for me, which could have caused a lot of errors scripts

ps: if you want to help me with that there are my discord: bom_d_mais_ser_monogamico or pepeeino

---
