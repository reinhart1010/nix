---
layout: page
title: common/git-cherry-pick (Indonesia)
description: "Lakukan perubahan yang tercatat pada komit-komit saat ini menuju cabang saat ini."
content_hash: 6dc09d6a6c2f472750d8c5ae004b446386ab0a8c
last_modified_at: 2024-09-11
related_topics:
  - title: বাংলা version
    url: /bn/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-cherry-pick.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-cherry-pick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git cherry-pick

Lakukan perubahan yang tercatat pada komit-komit saat ini menuju cabang saat ini.
Gunakan `git checkout` terlebih dahulu jika hendak melakukan perubahan pada cabang lainnya.
Informasi lebih lanjut: <https://git-scm.com/docs/git-cherry-pick>.

- Lakukan perubahan menurut suatu komit terhadap cabang saat ini:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit</span>

- Lakukan perubahan berdasarkan urutan komit terhadap cabang saat ini (lihat juga `git rebase --onto`):

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit_awal</span>`~..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit_akhir</span>

- Lakukan perubahan berdasarkan kumpulan komit (tak berurut) terhadap cabang saat ini:

`git cherry-pick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit1 komit2 ...</span>

- Lakukan perubahan pada direktori kerja saat ini tanpa mencatat komit baru:

`git cherry-pick --no-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit</span>
