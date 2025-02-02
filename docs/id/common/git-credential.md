---
layout: page
title: common/git-credential (Indonesia)
description: "Terima dan simpan kredensial pengguna."
content_hash: 50fb4821158b610b07b773db82d6fbb332091c12
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/git-credential.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-credential.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-credential.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git credential

Terima dan simpan kredensial pengguna.
Informasi lebih lanjut: <https://git-scm.com/docs/git-credential>.

- Tampilkan informasi suatu kredensial, termasuk username dan kata sandi dari berkas-berkas konfigurasi:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential fill`

- Kirim informasi kredensial menuju seluruh piranti pembantu (credential helper) yang disetel untuk disimpan dan digunakan pada lain waktu:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential approve`

- Hapus suatu informasi kredensial dari penyimpanan seluruh piranti pembantu:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url=http://example.com</span>`" | git credential reject`
