---
layout: page
title: common/whois (Indonesia)
description: "Program klien antarmuka baris perintah bagi protokol informasi WHOIS (RFC 3912)."
content_hash: 4520178d5b64bdacc4a20653055e746d05218dce
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/common/whois.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/whois.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/whois.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/whois.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whois

Program klien antarmuka baris perintah bagi protokol informasi WHOIS (RFC 3912).
Informasi lebih lanjut: <https://github.com/rfc1036/whois>.

- Dapatkan informasi kepemilikan bagi suatu nama domain:

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Dapatkan informasi kepemilikan bagi suatu alamat IP:

`whois `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Dapatkan informasi kontak penyalahgunaan bagi suatu alamat IP:

`whois -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>
