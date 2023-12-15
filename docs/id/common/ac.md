---
layout: page
title: common/ac (Indonesia)
description: "Tampilkan statistik mengenai lama waktu pengguna sistem operasi yang terhubung."
content_hash: 6e9d0f54ecc91548b66482ed8a70cec673cfce06
last_modified_at: 2023-12-15
related_topics:
  - title: বাংলা version
    url: /bn/common/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ac.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ac.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ac

Tampilkan statistik mengenai lama waktu pengguna sistem operasi yang terhubung.
Informasi lebih lanjut: <https://man.openbsd.org/ac>.

- Tampilkan berapa lama pengguna saat ini telah terhubung dengan sistem operasi, dalam hitungan jam:

`ac`

- Tampilkan informasi yang sama untuk setiap pengguna:

`ac -p`

- Tampilkan informasi yang sama untuk pengguna yang ditentukan:

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>

- Tampilkan informasi yang sama untuk pengguna yang ditentukan, dan dengan rincian per hari:

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>
