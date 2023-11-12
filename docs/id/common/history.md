---
layout: page
title: common/history (Indonesia)
description: "Sejarah command-line."
content_hash: 049a8ae167cc68199c86bf5cfbc8fda54e2013b1
last_modified_at: 2023-11-12
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

- Menampilkan sejarah perintah-perintah dengan angka baris:

`history`

- Menampilkan 20 perintah-perintah terakhir (di `zsh` perintah ini menampilkan semua perintah-perintah sejak dari baris ke-20):

`history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Menghapus sejarah perintah-perintah (hanya untuk sesi shell `bash` saat ini):

`history -c`

- Menulis ulang file sejarah dengan sejarah sesi shell `bash` saat ini (seringkali dikombinasikan dengan `history -c` untuk menghapus sejarah):

`history -w`

- Menghapus entri sejarah pada offset tertentu:

`history -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">offset</span>
