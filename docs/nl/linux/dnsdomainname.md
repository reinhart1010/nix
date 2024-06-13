---
layout: page
title: linux/dnsdomainname (Nederlands)
description: "Toon de DNS-domeinnaam van het systeem."
content_hash: 909db0e6f40aaceb5da14b9c2e522e1eb44a1016
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/linux/dnsdomainname.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnsdomainname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnsdomainname

Toon de DNS-domeinnaam van het systeem.
Let op: de tool gebruikt `gethostname` om de hostnaam van het systeem op te halen en vervolgens `getaddrinfo` om deze om te zetten in een gecanoniseerde naam.
Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/dnsdomainname-invocation.html>.

- Toon de DNS-domeinnaam van het systeem:

`dnsdomainname`
