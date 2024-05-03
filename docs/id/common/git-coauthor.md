---
layout: page
title: common/git-coauthor (Indonesia)
description: "Tambahkan penulis komit baru dalam komit terkini. Perintah ini menulis ulang riwayat perubahan pada Git, karena itu opsi `--force` akan dibutuhkan saat melakukan pendorongan perubahan (push) di lain waktu."
content_hash: 6b0a703a34f930666c20ccc49d4dcd17e83bacc8
last_modified_at: 2024-05-03
related_topics:
  - title: English version
    url: /en/common/git-coauthor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-coauthor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git coauthor

Tambahkan penulis komit baru dalam komit terkini. Perintah ini menulis ulang riwayat perubahan pada Git, karena itu opsi `--force` akan dibutuhkan saat melakukan pendorongan perubahan (push) di lain waktu.
Bagian dari `git extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-coauthor>.

- Tambahkan penulis baru terkadap komit Git terakhir:

`git coauthor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama@example.com</span>
