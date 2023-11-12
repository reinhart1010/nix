---
layout: page
title: common/testssl (English)
description: "Check SSL/TLS protocols and ciphers supported by a server."
content_hash: 397d4c5ea5d4af29b3208bd264f794a8a4c825ff
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# testssl

Check SSL/TLS protocols and ciphers supported by a server.
More information: <https://testssl.sh/>.

- Test a server (run every check) on port 443:

`testssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Test a different port:

`testssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com:465</span>

- Only check available protocols:

`testssl --protocols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Only check vulnerabilities:

`testssl --vulnerable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Only check HTTP security headers:

`testssl --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
