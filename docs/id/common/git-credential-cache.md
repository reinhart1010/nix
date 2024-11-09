---
layout: page
title: common/git-credential-cache (Indonesia)
description: "Pembantu Git untuk menyimpan kata sandi secara sementara pada memori."
content_hash: 51cc9f4cb5434b5db5c3811145b624865ae17bd1
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/git-credential-cache.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-credential-cache.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-credential-cache.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git credential-cache

Pembantu Git untuk menyimpan kata sandi secara sementara pada memori.
Informasi lebih lanjut: <https://git-scm.com/docs/git-credential-cache>.

- Simpan kredensial Git untuk jangka waktu yang ditentukan:

`git config credential.helper 'cache --timeout=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">waktu_dalam_hitungan_detik</span>`'`
