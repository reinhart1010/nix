---
layout: page
title: common/git-browse-ci (Indonesia)
description: "Buka laman sistem CI yang dipakai dalam repositori `git` pada aplikasi peramban web (web browser) default."
content_hash: a535e54dc1d58eb1f25851f8c7dfb873879e8941
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/git-browse-ci.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-browse-ci.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git browse-ci

Buka laman sistem CI yang dipakai dalam repositori `git` pada aplikasi peramban web (web browser) default.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-browse-ci>.

- Buka konfigurasi CI repositori saat ini pada situs web yang memiliki sumber/hulu jauh (upstream remote) utama:

`git browse-ci`

- Buka konfigurasi CI repositori saat ini pada situs web yang memiliki sumber/hulu jauh (upstream remote) tertentu:

`git browse-ci `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hulu_jauh</span>
