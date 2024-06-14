---
layout: page
title: linux/dnsdomainname (Nederlands)
description: "Toon de DNS-domeinnaam van het systeem."
content_hash: 909db0e6f40aaceb5da14b9c2e522e1eb44a1016
last_modified_at: 2024-06-14
related_topics:
  - title: English version
    url: /en/linux/dnsdomainname.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnsdomainname

Toon de DNS-domeinnaam van het systeem.
Let op: de tool gebruikt `gethostname` om de hostnaam van het systeem op te halen en vervolgens `getaddrinfo` om deze om te zetten in een gecanoniseerde naam.
Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/dnsdomainname-invocation.html>.

- Toon de DNS-domeinnaam van het systeem:

`dnsdomainname`
