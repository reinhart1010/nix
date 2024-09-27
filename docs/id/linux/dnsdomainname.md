---
layout: page
title: linux/dnsdomainname (Indonesia)
description: "Tampilkan nama domain jaringan yang disetel oleh sistem bagi perangkat komputer ini."
content_hash: 7b2071ffe910d34e9e37c2e2702c9ebd9a356053
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/linux/dnsdomainname.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/dnsdomainname.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnsdomainname.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnsdomainname

Tampilkan nama domain jaringan yang disetel oleh sistem bagi perangkat komputer ini.
Catatan: Program ini menggunakan perintah `gethostname` untuk mendapatkan hostname perangkat serta `getaddrinfo` untuk melakukan resolusi hostname tersebut menuju nama kanonikal.
Informasi lebih lanjut: <https://www.gnu.org/software/inetutils/manual/html_node/dnsdomainname-invocation.html>.

- Tampilkan nama domain DNS atas perangkat ini:

`dnsdomainname`
