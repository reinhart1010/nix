---
layout: page
title: common/archwiki-rs (Indonesia)
description: "Baca, cari, dan unduh artikel dari situs ArchWiki."
content_hash: 321ad1f158bfee2ce355222d795c5382c972a5af
last_modified_at: 2024-06-14
related_topics:
  - title: English version
    url: /en/common/archwiki-rs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/archwiki-rs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/archwiki-rs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># archwiki-rs

Baca, cari, dan unduh artikel dari situs ArchWiki.
Informasi lebih lanjut: <https://gitlab.com/lucifayr/archwiki-rs>.

- Baca suatu artikel dari situs ArchWiki:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">judul_artikel</span>

- Baca suatu artikel dari ArchWiki dengan format tertentu:

`archwiki-rs read-page `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">judul_artikel</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>

- Cari artikel dalam ArchWiki yang mengandung teks tertentu:

`archwiki-rs search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks_yang_dicari</span>`" --text-search`

- Unduh seluruh artikel dari situs ArchWiki ke dalam suatu direktori:

`archwiki-rs local-wiki `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/jalan/menuju/wiki_lokal</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain-text|markdown|html</span>
