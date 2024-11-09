---
layout: page
title: common/brew-search (Indonesia)
description: "Cari kumpulan paket cask dan formula."
content_hash: 7d692981c09cee81d04657b77032881f23eb0b94
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/brew-search.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew-search.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-search.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew search

Cari kumpulan paket cask dan formula.
Informasi lebih lanjut: <https://docs.brew.sh/Manpage#search--s-options-textregex->.

- Cari kumpulan cask dan formula menggunakan suatu kata kunci:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Cari kumpulan cask dan formula menggunakan ekspresi reguler (regex):

`brew search /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>`/`

- Cari pula menurut deskripsi paket:

`brew search --desc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Hanya cari kumpulan paket formula:

`brew search --formula `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Hanya cari kumpulan paket cask:

`brew search --cask `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>
