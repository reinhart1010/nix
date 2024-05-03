---
layout: page
title: common/git-cola (Indonesia)
description: "Tampilan antarmuka grafis (GUI) untuk Git yang kuat, apik, dan intuitif."
content_hash: 8a5280de4eea46b40cbace6922bd9952fb791fe0
last_modified_at: 2024-05-03
related_topics:
  - title: English version
    url: /en/common/git-cola.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git-cola.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-cola.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git cola

Tampilan antarmuka grafis (GUI) untuk Git yang kuat, apik, dan intuitif.
Informasi lebih lanjut: <https://git-cola.readthedocs.io>.

- Jalankan program GUI:

`git cola`

- Jalankan GUI pada mode perubahan (amend):

`git cola --amend`

- Jalankan dengan meminta program menanyakan repositori Git yang akan dilihat. Jika tidak didefinisikan, maka program ini akan melihat direktori saat ini:

`git cola --prompt`

- Jalankan dengan membuka repositori Git dengan alamat yang ditentukan:

`git cola --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/repositori-git</span>

- Terapkan filter jalur ke dalam widget status:

`git cola --status-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter</span>
