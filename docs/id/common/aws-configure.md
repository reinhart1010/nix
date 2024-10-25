---
layout: page
title: common/aws-configure (Indonesia)
description: "Atur konfigurasi penggunaan AWS CLI."
content_hash: 72259e5de2fcac73dca8c47aa138e596b152cdf9
last_modified_at: 2024-10-25
related_topics:
  - title: English version
    url: /en/common/aws-configure.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-configure.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws-configure.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-configure.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-configure.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws configure

Atur konfigurasi penggunaan AWS CLI.
Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Atur konfigurasi AWS CLI secara interaktif (akan membuat konfigurasi baru atau memutakhirkan konfigurasi bawaan):

`aws configure`

- Atur konfigurasi bagi suatu profil pengguna AWS CLI (akan membuat profil pengguna baru atau memutakhirkannya):

`aws configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_profil</span>

- Tampilkan nilai terhadap suatu variabel konfigurasi:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_variabel</span>

- Tampilkan nilai terhadap suatu variabel konfigurasi pada suatu profil pengguna:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_variabel</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_profil</span>

- Atur nilai suatu variabel konfigurasi:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_variabel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nilai</span>

- Atur nilai suatu variabel konfigurasi bagi suatu profil pengguna:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_variabel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nilai</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_profil</span>

- Tampilkan seluruh konfigurasi yang disimpan:

`aws configure list`

- Tampilkan seluruh konfigurasi yang disimpan bagi suatu profil pengguna:

`aws configure list --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_profil</span>
