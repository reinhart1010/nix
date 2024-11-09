---
layout: page
title: common/history (Indonesia)
description: "Tampilkan riwayat penugasan baris perintah (command-line)."
content_hash: 1f6c01a9eb61202f5ed2407c73a77f7b6b5ceeeb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/history.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/history.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># history

Tampilkan riwayat penugasan baris perintah (command-line).
Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Tampilkan riwayat penugasan baris perintah beserta angka baris:

`history`

- Tampilkan 20 perintah tugas terakhir (di Zsh perintah ini menampilkan semua perintah-perintah sejak dari baris ke-20):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Tampilkan riwayat dengan format tanggal dan waktu tertentu (hanya tersedia dalam Zsh):

`history -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d|f|i|E</span>

- Hapus seluruh riwayat perintah penugasan (hanya untuk sesi shell Bash saat ini):

`history -c`

- Tulis ulang berkas dengan riwayat sesi shell Bash saat ini (seringkali dikombinasikan dengan `history -c` untuk menghapus riwayat):

`history -w`

- Hapus entri riwayat pada offset tertentu:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">offset</span>
