---
layout: page
title: common/git-cherry (Indonesia)
description: "Cari komit yang belum dimasukkan kepada hulu (upstream)."
content_hash: 35e82bd7826a0ddb294a4c6560bd609974fbf7c1
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-cherry.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git cherry

Cari komit yang belum dimasukkan kepada hulu (upstream).
Informasi lebih lanjut: <https://git-scm.com/docs/git-cherry>.

- Lihat daftar komit (beserta pesannya) dengan komit-komit serupa pada hulu (upstream):

`git cherry -v`

- Gunakan sumber hulu dan cabang topik yang lain:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topik</span>

- Tampilkan hanya komit yang muncul hingga komit ini:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hingga_komit_ini</span>
