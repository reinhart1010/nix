---
layout: page
title: common/git-check-ref-format (Indonesia)
description: "Cek apakah nama suatu referensi (refname) sesuai syarat, dan keluar dengan nilai status di luar angka nol jika tidak."
content_hash: 3528605739a3076bd8a43330090f780112df9f23
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/git-check-ref-format.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-ref-format.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-check-ref-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git check-ref-format

Cek apakah nama suatu referensi (refname) sesuai syarat, dan keluar dengan nilai status di luar angka nol jika tidak.
Informasi lebih lanjut: <https://git-scm.com/docs/git-check-ref-format>.

- Cek kesesuaian format suatu nama referensi:

`git check-ref-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>

- Cetak nama cabang yang terakhir kali diperiksa sebelum mengganti ke cabang saat ini:

`git check-ref-format --branch @{-1}`

- Lakukan normalisasi terhadap nama referensi:

`git check-ref-format --normalize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">refs/head/refname</span>
