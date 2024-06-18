---
layout: page
title: common/argon2 (Indonesia)
description: "Hitung kode hash menggunakan algoritma kriptografi Argon2."
content_hash: bfe224ab42102f637e515e30419f3fbdc0a77638
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/argon2.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/argon2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/argon2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/argon2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># argon2

Hitung kode hash menggunakan algoritma kriptografi Argon2.
Informasi lebih lanjut: <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Hitung kode hash dari suatu kata kunci (password) dengan suatu kata garam (salt) menggunakan parameter kriptografi bawaan:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_garam</span>`"`

- Hitung kode hash dengan algoritma tertentu:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_garam</span>`" -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|i|id</span>

- Jangan tampilkan informasi tambahan selain hasil kode hash:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_garam</span>`" -e`

- Hitung kode hash dengan konfigurasi wak[t]u, pemanfaatan [m]emori (RAM), dan [p]aralelisme pada pemrosesan kriptografi secara tertentu:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>`" | argon2 "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_garam</span>`" -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
