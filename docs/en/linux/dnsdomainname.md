---
layout: page
title: linux/dnsdomainname (English)
description: "Show the system's DNS domain name."
content_hash: 95a95c5e6739d41b58da53a9e09b33122e03d703
last_modified_at: 2023-11-26
tldri18n_status: 2
---
# dnsdomainname

Show the system's DNS domain name.
Note: The tool uses `gethostname` to get the hostname of the system and then `getaddrinfo` to resolve it into a canonical name.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/dnsdomainname-invocation.html>.

- Show the system's DNS domain name:

`dnsdomainname`
