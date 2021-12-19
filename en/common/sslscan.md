---
layout: page
title: common/sslscan (English)
description: "Check SSL/TLS protocols and ciphers supported by a server."
content_hash: b41767923273b5377d0e7ef52e8cd2002f4b8ae9
---
# sslscan

Check SSL/TLS protocols and ciphers supported by a server.
More information: <https://github.com/rbsec/sslscan>.

- Test a server on port 443:

`sslscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Test a specified port:

`sslscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">465</span>

- Show certificate information:

`testssl --show-certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
