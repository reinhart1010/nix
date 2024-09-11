---
layout: page
title: common/git-push (Indonesia)
description: "Dorong kumpulan komit menuju suatu repositori jarak jauh (remote)."
content_hash: 89ec9441ecd45c476427e7cbe3864a1210361391
last_modified_at: 2024-09-11
related_topics:
  - title: Deutsch version
    url: /de/common/git-push.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-push.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-push.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-push.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-push.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-push.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-push.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-push.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git push

Dorong kumpulan komit menuju suatu repositori jarak jauh (remote).
Informasi lebih lanjut: <https://git-scm.com/docs/git-push>.

- Kirim perubahan lokal dari cabang (branch) saat ini menuju cabang yang sepadan pada repositori tujuan:

`git push`

- Kirim perubahan dari cabang lokal yang ditentukan menuju cabang yang sepadan pada repositori tujuan:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cabang_lokal</span>

- Kirim perubahan dari cabang lokal yang ditentukan menuju cabang sepadan pada repositori tujuan, dan simpan remote sebagai target operasi dorong (push) dan tarik (pull) bagi cabang lokal tersebut:

`git push -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cabang_lokal</span>

- Kirim perubahan dari suatu cabang lokal menuju suatu cabang remote secara spesifik:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cabang_lokal</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cabang_remote</span>

- Kirim perubahan dari setiap cabang lokal menuju cabang-cabang sepadan dalam repositori tujuan:

`git push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama-remote</span>

- Hapus suatu cabang dalam suatu repositori remote:

`git push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cabang_remote</span>

- Hapus cabang-cabang remote yang tidak memiliki padanan pada repositori lokal:

`git push --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>

- Publikasikan kumpulan tag komit yang belum dipublikasikan dalam repositori remote:

`git push --tags`
