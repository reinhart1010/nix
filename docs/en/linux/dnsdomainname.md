---
layout: page
title: linux/dnsdomainname (English)
description: "Show the system's DNS domain name."
content_hash: 95a95c5e6739d41b58da53a9e09b33122e03d703
last_modified_at: 2023-11-20
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnsdomainname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnsdomainname

Show the system's DNS domain name.
Note: The tool uses `gethostname` to get the hostname of the system and then `getaddrinfo` to resolve it into a canonical name.
More information: <https://www.gnu.org/software/inetutils/manual/html_node/dnsdomainname-invocation.html>.

- Show the system's DNS domain name:

`dnsdomainname`
