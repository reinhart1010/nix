---
layout: page
title: common/afconvert (Indonesia)
description: "Ubah format file antara AFF dan file baku/raw."
content_hash: 713a03247edda8be25fc7dd5f4e469d8bda52e63
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/afconvert.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/afconvert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/afconvert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/afconvert.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/afconvert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/afconvert.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/afconvert.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/afconvert.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># afconvert

Ubah format file antara AFF dan file baku/raw.
Informasi lebih lanjut: <https://manned.org/afconvert.1>.

- Pakai nama ekstensi output (default: `aff`):

`afconvert -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekstensi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_output1 jalan/menuju/file_output2 ...</span>

- Gunakan tingkat kompresi file (default: `7`):

`afconvert -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0..7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_input</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_output1 jalan/menuju/file_output2 ...</span>
