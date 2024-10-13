---
layout: page
title: common/git-cherry (Indonesia)
description: "Cari komit yang belum dimasukkan kepada hulu (upstream)."
content_hash: 34d1fe7b65d58543366160974a3c6bf2a702a8aa
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-cherry.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-cherry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry

Cari komit yang belum dimasukkan kepada hulu (upstream).
Informasi lebih lanjut: <https://git-scm.com/docs/git-cherry>.

- Lihat daftar komit (beserta pesannya) dengan komit-komit serupa pada hulu (upstream):

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- Gunakan sumber hulu dan cabang topik yang lain:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topik</span>

- Tampilkan hanya komit yang muncul hingga komit ini:

`git cherry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">topic</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hingga_komit_ini</span>
