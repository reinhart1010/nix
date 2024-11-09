---
layout: page
title: common/git-credential-store (Indonesia)
description: "Pembantu Git untuk menyimpan kata sandi pada perangkat penyimpanan."
content_hash: 702861280869cca456bf6ac4f92aa9d5f9d26fe7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/git-credential-store.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-credential-store.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-credential-store.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git credential-store

Pembantu Git untuk menyimpan kata sandi pada perangkat penyimpanan.
Informasi lebih lanjut: <https://git-scm.com/docs/git-credential-store>.

- Simpan kredensial-kredensial Git pada suatu berkas:

`git config credential.helper 'store --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>`'`
