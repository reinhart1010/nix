---
layout: page
title: common/history (Indonesia)
description: "Sejarah command-line."
content_hash: b0ce93541fd0cd1f17a8de4083c4e4b6e59c976d
last_modified_at: 2024-03-10
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
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/history.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/history.html
    icon: bi bi-globe
tldri18n_status: 2
---
# history

Sejarah command-line.
Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Tampilkan sejarah perintah-perintah dengan angka baris:

`history`

- Tampilkan 20 perintah-perintah terakhir (di Zsh perintah ini menampilkan semua perintah-perintah sejak dari baris ke-20):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Hapus sejarah perintah-perintah (hanya untuk sesi shell Bash saat ini):

`history -c`

- Tulis ulang file sejarah dengan sejarah sesi shell Bash saat ini (seringkali dikombinasikan dengan `history -c` untuk menghapus sejarah):

`history -w`

- Hapus entri sejarah pada offset tertentu:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">offset</span>
