---
layout: page
title: common/git-clone (Indonesia)
description: "Gandakan repositori dari lokasi luar/remote menuju lokal."
content_hash: 90736b2e4549542412baa7805b02cd99138fe2ec
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/common/git-clone.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-clone.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clone.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clone.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clone.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clone.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-clone.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clone.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clone.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-clone.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-clone.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clone

Gandakan repositori dari lokasi luar/remote menuju lokal.
Informasi lebih lanjut: <https://git-scm.com/docs/git-clone>.

- Gandakan repositori yang ada ke direktori tertentu:

`git clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Gandakan repositori yang ada dan submodulnya:

`git clone --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>

- Gandakan hanya direktori `.git` pada repositori saat ini:

`git clone --no-checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>

- Gandakan repositori lokal:

`git clone --local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/repositori/lokal</span>

- Gandakan dengan senyap:

`git clone --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>

- Gandakan repositori yang sudah ada dengan hanya mengambil 10 komit paling baru pada branch bawaan (berguna untuk menghemat waktu):

`git clone --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>

- Gandakan repositori yang sudah ada dengan hanya mengambil dari cabang tertentu:

`git clone --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --single-branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>

- Gandakan repositori yang sudah ada menggunakan perintah SSH tertentu:

`git clone --config core.sshCommand="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh -i jalan/menuju/kunci_ssh_privat</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_repositori_remote</span>
