---
layout: page
title: common/alex (Indonesia)
description: "Alat untuk menangkal karya tulis bahasa Inggris yang ditulis secara tidak sensitif dan berpengertian."
content_hash: 46e0f2f440606c6e4bd9c5e9f74ee98aa617fbd8
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/alex.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># alex

Alat untuk menangkal karya tulis bahasa Inggris yang ditulis secara tidak sensitif dan berpengertian.
Alat ini dapat menemukan kata dan frasa bahasa Inggris yang berkaitan kuat dengan gender, polarisasi, ras, agama, dan frasa-frasa sensitif lainnya.
Informasi lebih lanjut: <https://github.com/get-alex/alex>.

- Analisa teks dari `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- Analisa teks dari seluruh file dalam direktori saat ini:

`alex`

- Analisa teks dari suatu file:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.md</span>

- Analisa seluruh file Markdown (`.md`) kecuali `contoh.md`:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contoh.md</span>
