---
layout: page
title: common/aws-google-auth (Indonesia)
description: "Dapatkan kredensial sementara (STS) bagi AWS menggunakan Google Apps sebagai penyedia akun layanan terfederasi (Single Sign-On)."
content_hash: c248bdd5333f326b3c1e589c5782246fa726023f
last_modified_at: 2024-10-25
related_topics:
  - title: Deutsch version
    url: /de/common/aws-google-auth.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-google-auth.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-google-auth.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-google-auth.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-google-auth.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-google-auth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws-google-auth

Dapatkan kredensial sementara (STS) bagi AWS menggunakan Google Apps sebagai penyedia akun layanan terfederasi (Single Sign-On).
Informasi lebih lanjut: <https://github.com/cevoaustralia/aws-google-auth>.

- Masuk menggunakan akun SSO Google dengan data pengenal [u]sername, [I]DP, dan [S]P, kemudian atur [d]urasi akses kredensial sementara selama satu jam ke depan:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Masuk dengan men[a]nyakan peran (role) yang hendak digunakan dalam membuat kredensial (bila terdapat beberapa peran SAML yang tersedia):

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a`

- Selesaikan kumpulan alias bagi akun AWS:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a --resolve-aliases`

- Tampilkan bantuan:

`aws-google-auth -h`
