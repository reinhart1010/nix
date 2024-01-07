---
layout: page
title: common/git-cherry (Indonesia)
description: "Cari komit yang belum dimasukkan kepada hulu (upstream)."
content_hash: 35e82bd7826a0ddb294a4c6560bd609974fbf7c1
last_modified_at: 2024-01-07
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
tldri18n_status: 2
---
# git cherry

Cari komit yang belum dimasukkan kepada hulu (upstream).
Informasi lebih lanjut: <https://git-scm.com/docs/git-cherry>.

- Lihat daftar komit (beserta pesannya) dengan komit-komit serupa pada hulu (upstream):

`git cherry -v`

- Gunakan sumber hulu dan cabang topik yang lain:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topik</span>

- Tampilkan hanya komit yang muncul hingga komit ini:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hingga_komit_ini</span>
