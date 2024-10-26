---
layout: page
title: common/cancel (Indonesia)
description: "Batalkan penugasan pencetakan dokumen terhadap mesin-mesin pencetak (printer)."
content_hash: 2aa267bdb9e589ac0fb7ee5ae8a3d74c990bb4e7
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/cancel.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cancel.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cancel.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cancel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cancel

Batalkan penugasan pencetakan dokumen terhadap mesin-mesin pencetak (printer).
Lihat juga: `lp`, `lpmove`, `lpstat`.
Informasi lebih lanjut: <https://openprinting.github.io/cups/doc/man-cancel.html>.

- Batalkan pekerjaan yang sedang dikerjakan ke dalam mesin pencetak yang diatur sebagai tujuan bawaan (atur mesin tujuan bawaan dengan perintah `lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pencetak</span>):

`cancel`

- Batalkan pekerjaan yang sedang dikerjakan ke dalam mesin pencetak yang diatur sebagai tujuan bawaan menurut pengaturan suatu pengguna ([u]ser):

`cancel -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Batalkan pekerjaan yang sedang dikerjakan ke dalam suatu mesin pencetak:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pencetak</span>

- Batalkan suatu pekerjaan yang sedang dikerjakan ke dalam suatu mesin pencetak:

`cancel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pencetak</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_induk_pekerjaan</span>

- Batalkan semu[a] pekerjaan yang sedang dan akan dikerjakan oleh mesin pencetak apapun:

`cancel -a`

- Batalkan semu[a] pekerjaan yang sedang dan akan dikerjakan oleh suatu mesin pencetak:

`cancel -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pencetak</span>

- Batalkan pekerjaan yang sedang ditangani oleh suatu peladen (server) layanan pencetak, kemudian hapus ([x]) berkas-berkas data pendukung pekerjaan:

`cancel -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">peladen</span>` -x`
