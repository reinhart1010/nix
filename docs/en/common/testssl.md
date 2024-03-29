---
layout: page
title: common/testssl (English)
description: "Check SSL/TLS protocols and ciphers supported by a server."
content_hash: 6762c7305d2094075f8d7e2df3ac4d4360ab9c44
last_modified_at: 2024-02-16
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

- Test other STARTTLS enabled protocols:

`testssl --starttls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp|smtp|pop3|imap|xmpp|sieve|xmpp-server|telnet|ldap|irc|lmtp|nntp|postgres|mysql</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>
