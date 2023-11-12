---
layout: page
title: linux/dnsdomainname (English)
description: "Show the system's DNS domain name."
content_hash: 95a95c5e6739d41b58da53a9e09b33122e03d703
last_modified_at: 2023-11-12
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dnsdomainname

Show the system's DNS domain name.
Note: The tool uses `gethostname` to get the hostname of the system and then `getaddrinfo` to resolve it into a canonical name.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/dnsdomainname-invocation.html>.

- Show the system's DNS domain name:

`dnsdomainname`
